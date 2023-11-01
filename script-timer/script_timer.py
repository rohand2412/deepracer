import shutil
import signal
import subprocess as sub
import time

#------------------ CONSTANTS ------------------#

SHELL_SCRIPT = "deepracer-for-cloud/bin/activate.sh"
TRAINING_MINUTES = None                                             #<------ SET TRAINING MINUTES

RUN_ENV = [
    "DR_RUN_ID=0",
    "DR_WORLD_NAME=2022_september_open",                            #<------ SET TRACK NAME
    "DR_RACE_TYPE=TIME_TRIAL",
    "DR_CAR_NAME=FastCar",
    "DR_CAR_BODY_SHELL_TYPE=deepracer",
    "DR_CAR_COLOR=Red",
    "DR_DISPLAY_NAME=$DR_CAR_NAME",
    "DR_RACER_NAME=$DR_CAR_NAME",
    "DR_ENABLE_DOMAIN_RANDOMIZATION=False",
    "DR_EVAL_NUMBER_OF_TRIALS=3",
    "DR_EVAL_IS_CONTINUOUS=True",
    "DR_EVAL_MAX_RESETS=100",
    "DR_EVAL_OFF_TRACK_PENALTY=3.0",
    "DR_EVAL_COLLISION_PENALTY=5.0",
    "DR_EVAL_SAVE_MP4=True",
    "DR_EVAL_CHECKPOINT=last",
    "DR_EVAL_OPP_S3_MODEL_PREFIX=rl-deepracer-sagemaker",
    "DR_EVAL_OPP_CAR_BODY_SHELL_TYPE=deepracer",
    "DR_EVAL_OPP_CAR_NAME=FasterCar",
    "DR_EVAL_OPP_DISPLAY_NAME=$DR_EVAL_OPP_CAR_NAME",
    "DR_EVAL_OPP_RACER_NAME=$DR_EVAL_OPP_CAR_NAME",
    "DR_EVAL_DEBUG_REWARD=False",
    "DR_EVAL_RESET_BEHIND_DIST=1.0",
    "#DR_EVAL_RTF=1.0",
    "DR_TRAIN_CHANGE_START_POSITION=True",
    "DR_TRAIN_ALTERNATE_DRIVING_DIRECTION=False",
    "DR_TRAIN_START_POSITION_OFFSET=0.0",
    "DR_TRAIN_ROUND_ROBIN_ADVANCE_DIST=0.05",
    "DR_TRAIN_MULTI_CONFIG=False",
    "DR_TRAIN_MIN_EVAL_TRIALS=5",
    "#DR_TRAIN_RTF=1.0",
    "DR_LOCAL_S3_MODEL_PREFIX=rl-deepracer-sagemaker",              #<------ SET MODEL NAME
    "DR_LOCAL_S3_PRETRAINED=False",
    "DR_LOCAL_S3_PRETRAINED_PREFIX=rl-sagemaker-pretrained",
    "DR_LOCAL_S3_PRETRAINED_CHECKPOINT=last",
    "DR_LOCAL_S3_CUSTOM_FILES_PREFIX=custom_files",
    "DR_LOCAL_S3_TRAINING_PARAMS_FILE=training_params.yaml",
    "DR_LOCAL_S3_EVAL_PARAMS_FILE=evaluation_params.yaml",
    "DR_LOCAL_S3_MODEL_METADATA_KEY=$DR_LOCAL_S3_CUSTOM_FILES_PREFIX/model_metadata.json",
    "DR_LOCAL_S3_HYPERPARAMETERS_KEY=$DR_LOCAL_S3_CUSTOM_FILES_PREFIX/hyperparameters.json",
    "DR_LOCAL_S3_REWARD_KEY=$DR_LOCAL_S3_CUSTOM_FILES_PREFIX/reward_function.py",
    "DR_LOCAL_S3_METRICS_PREFIX=$DR_LOCAL_S3_MODEL_PREFIX/metrics",
    "DR_UPLOAD_S3_PREFIX=$DR_LOCAL_S3_MODEL_PREFIX",
    "DR_OA_NUMBER_OF_OBSTACLES=6",
    "DR_OA_MIN_DISTANCE_BETWEEN_OBSTACLES=2.0",
    "DR_OA_RANDOMIZE_OBSTACLE_LOCATIONS=False",
    "DR_OA_IS_OBSTACLE_BOT_CAR=False",
    "DR_OA_OBJECT_POSITIONS=",
    "DR_H2B_IS_LANE_CHANGE=False",
    "DR_H2B_LOWER_LANE_CHANGE_TIME=3.0",
    "DR_H2B_UPPER_LANE_CHANGE_TIME=5.0",
    "DR_H2B_LANE_CHANGE_DISTANCE=1.0",
    "DR_H2B_NUMBER_OF_BOT_CARS=3",
    "DR_H2B_MIN_DISTANCE_BETWEEN_BOT_CARS=2.0",
    "DR_H2B_RANDOMIZE_BOT_CAR_LOCATIONS=False",
    "DR_H2B_BOT_CAR_SPEED=0.2",
    "DR_H2B_BOT_CAR_PENALTY=5.0",
]

SYSTEM_ENV = [
    "DR_CLOUD=aws",
    "DR_AWS_APP_REGION=us-east-1",
    "DR_UPLOAD_S3_PROFILE=default",
    "DR_UPLOAD_S3_BUCKET=deepracer-bucket-4212",
    "DR_UPLOAD_S3_ROLE=to-be-defined",
    "DR_LOCAL_S3_BUCKET=deepracer-bucket-4212",
    "DR_LOCAL_S3_PROFILE=default",
    "DR_GUI_ENABLE=False",
    "DR_KINESIS_STREAM_NAME=",
    "DR_KINESIS_STREAM_ENABLE=True",
    "DR_SAGEMAKER_IMAGE=5.1.0-gpu",                                 #<------ CHECK FOR ROBOMAKER IMAGE UPDATES
    "DR_ROBOMAKER_IMAGE=5.1.0-cpu-avx2",                            #<------ CHECK FOR ROBOMAKER IMAGE UPDATES
    "DR_ANALYSIS_IMAGE=cpu",
    "DR_COACH_IMAGE=5.0.0",
    "DR_WORKERS=1",
    "DR_ROBOMAKER_MOUNT_LOGS=True",
    "DR_CLOUD_WATCH_ENABLE=False",
    "DR_DOCKER_STYLE=swarm",
    "DR_HOST_X=False",
    "DR_WEBVIEWER_PORT=8100",
    "# DR_DISPLAY=:99",
    "# DR_REMOTE_MINIO_URL=http://mynas:9000",
    "# CUDA_VISIBLE_DEVICES=0",
]

HYPERPARAMETERS_JSON = [
    '{',
    '    "batch_size": 64,',
    '    "beta_entropy": 0.01,',
    '    "discount_factor": 0.999,',
    '    "e_greedy_value": 0.05,',
    '    "epsilon_steps": 10000,',
    '    "exploration_type": "categorical",',
    '    "loss_type": "huber",',
    '    "lr": 0.0003,',
    '    "num_episodes_between_training": 20,',
    '    "num_epochs": 10,',
    '    "stack_size": 1,',
    '    "term_cond_avg_score": 350000000.0,',
    '    "term_cond_max_episodes": 1000000000,',
    '    "sac_alpha": 0.2',
    '}',
]

MODEL_METADATA_JSON = [
    '{',
    '  "action_space" : {',
    '    "steering_angle" : {',
    '      "high" : 30.0,',
    '      "low" : -30.0',
    '    },',
    '    "speed" : {',
    '      "high" : 1.0,',
    '      "low" : 0.5',
    '    }',
    '  },',
    '  "sensor" : [ "FRONT_FACING_CAMERA" ],',
    '  "neural_network" : "DEEP_CONVOLUTIONAL_NETWORK_SHALLOW",',
    '  "version" : "4",',
    '  "training_algorithm" : "clipped_ppo",',
    '  "action_space_type" : "continuous"',
    '}',
]

#------------------ CODE ------------------#

def replace_file(path: str, lines: list) -> None:
    with open(path, "r+") as f:
        f.truncate(0)
        f.seek(0)
        f.write("\n".join(lines))

def run_with_live_stdout(command: str, shell_script: bool = True) -> None:
    print(command)
    if shell_script:
        full_command = 'source {}; {}'.format(SHELL_SCRIPT, command)
    else:
        full_command = command
    proc = sub.Popen(full_command, stdout=sub.PIPE, shell=True, executable='/bin/bash')
    while proc.poll() == None:
        raw = proc.stdout.readline()
        line = raw.decode('utf-8').rstrip('\n')
        if line: print(line)
    proc.stdout.close()

def run_training(command: str) -> bool:
    print(command)
    start = None
    SEC_PER_MIN = 60
    last_line = None
    proc = sub.Popen('source {}; {}'.format(SHELL_SCRIPT, command), stdout=sub.PIPE, shell=True, executable='/bin/bash')
    while proc.poll() == None:
        raw = proc.stdout.readline()
        line = raw.decode('utf-8').rstrip('\n')
        if line:
            print(line)
            last_line = line

        training_line = line[:51] == 'Training> Name=main_level/agent, Worker=0, Episode='
        if training_line and not start:
            start = time.time()

        time_left = not start or time.time() - start < TRAINING_MINUTES * SEC_PER_MIN
        if not time_left and training_line:
            print("sent sigterm: {}s".format(time.time() - start))
            proc.send_signal(signal.SIGTERM)
            break
    while proc.poll() == None: pass
    proc.stdout.close()
    if last_line[:41] == "Selected path s3://deepracer-bucket-4212/":
        print("DELETE S3 MODEL DIRECTORY")
        exit()
    return bool(start)

if TRAINING_MINUTES == None:
    print("SET TRAINING MINUTES")
    exit()

run_with_live_stdout("deepracer-for-cloud/bin/init.sh -c aws -a gpu", False)

replace_file("deepracer-for-cloud/run.env", RUN_ENV)
replace_file("deepracer-for-cloud/system.env", SYSTEM_ENV)

run_with_live_stdout("dr-update")

replace_file("deepracer-for-cloud/custom_files/hyperparameters.json", HYPERPARAMETERS_JSON)
replace_file("deepracer-for-cloud/custom_files/model_metadata.json", MODEL_METADATA_JSON)
shutil.copyfile("src_reward_function.py", "deepracer-for-cloud/custom_files/reward_function.py")

run_with_live_stdout("dr-upload-custom-files")

if not run_training("dr-start-training -v"):
    while not run_training("dr-logs-sagemaker"):
        time.sleep(5)

run_with_live_stdout("dr-stop-training")

print("dr-start-evaluation")
proc = sub.Popen('source {}; dr-start-evaluation'.format(SHELL_SCRIPT), stdout=sub.PIPE, shell=True, executable='/bin/bash')
while proc.poll() == None:
    raw = proc.stdout.readline()
    line = raw.decode('utf-8').rstrip('\n')
    if line: print(line)

    if line[:12] == '\x1b[1mdone\x1b[0m':
        print("sent sigterm")
        proc.send_signal(signal.SIGTERM)
        break
while proc.poll() == None: pass
proc.stdout.close()

run_with_live_stdout("dr-stop-evaluation")
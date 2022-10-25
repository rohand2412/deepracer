import os
import shutil
import tarfile
import argparse
import subprocess as sub

def remove(path):
    removed = False
    try:
        shutil.rmtree(path)
    except (FileNotFoundError, NotADirectoryError):
        pass
    else:
        removed = True

    try:
        os.remove(path)
    except FileNotFoundError:
        pass
    else:
        removed = True

    if removed:
        print("removed: {}".format(path))
    else:
        print("does not exist: {}".format(path))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-name", default=None, type=str, help="name of model to download")
    args = parser.parse_args()

    model_name = args.model_name

    if not model_name:
        print("[ERROR] No model name specified")
        exit()

    valid_model_name = False
    proc = sub.Popen("aws s3 cp s3://deepracer-bucket-4212/{} Logs-{}/ --recursive".format(model_name, model_name), stdout=sub.PIPE, shell=True)
    while proc.poll() == None:
        raw = proc.stdout.readline()
        line = raw.decode('utf-8').rstrip('\n')
        if line:
            print(line)
            valid_model_name = True
    proc.stdout.close()

    if not valid_model_name:
        print("[ERROR] Invalid model name specified")
        remove("Logs-{}".format(model_name))
        exit()

    print("download complete: {}".format(model_name))

    remove("Logs-{}/output.tar.gz".format(model_name))
    remove("Logs-{}/source".format(model_name))
    remove("Logs-{}/model".format(model_name))
    remove("Logs-{}/mp4/camera-45degree".format(model_name))

    with tarfile.open("Logs-{}/model.tar.gz".format(model_name)) as f:
        f.extractall("./Logs-{}/model.tar.gz-extracted".format(model_name))
        print("extracted: Logs-{}/model.tar.gz".format(model_name))

    remove("Logs-{}/model.tar.gz".format(model_name))
    remove("Logs-{}/model.tar.gz-extracted/agent".format(model_name))

    os.mkdir("Logs-{}/model".format(model_name))
    print("created: Logs-{}/model".format(model_name))
    shutil.copy2("Logs-{}/model.tar.gz-extracted/model_metadata.json".format(model_name), "Logs-{}/model".format(model_name))
    print("copied: Logs-{}/model/model_metadata.json".format(model_name))

if __name__ == '__main__':
    main()
import signal
import subprocess as sub
import time

shell_script = "dummy_functions.sh"
training_minutes = 1/12

print("dr-start-training")
start = None
SEC_PER_MIN = 60
proc = sub.Popen('source {}; dr-start-training'.format(shell_script), stdout=sub.PIPE, shell=True, executable='/bin/bash')
while proc.poll() == None:
    raw = proc.stdout.readline()
    line = raw.decode('utf-8').rstrip('\n')
    if line: print(line)

    training_line = line[:51] == 'Training> Name=main_level/agent, Worker=0, Episode='
    if training_line and not start:
        start = time.time()

    time_left = not start or time.time() - start < training_minutes * SEC_PER_MIN
    if not time_left and training_line:
        print("sent sigterm: {}s".format(time.time() - start))
        proc.send_signal(signal.SIGTERM)
        break
while proc.poll() == None: pass
proc.stdout.close()

print("dr-stop-training")
proc = sub.Popen('source {}; dr-stop-training'.format(shell_script), stdout=sub.PIPE, shell=True, executable='/bin/bash')
while proc.poll() == None:
    raw = proc.stdout.readline()
    line = raw.decode('utf-8').rstrip('\n')
    if line: print(line)
proc.stdout.close()

print("dr-start-evaluation")
proc = sub.Popen('source {}; dr-start-evaluation'.format(shell_script), stdout=sub.PIPE, shell=True, executable='/bin/bash')
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

print("dr-stop-evaluation")
proc = sub.Popen('source {}; dr-stop-evaluation'.format(shell_script), stdout=sub.PIPE, shell=True, executable='/bin/bash')
while proc.poll() == None:
    raw = proc.stdout.readline()
    line = raw.decode('utf-8').rstrip('\n')
    if line: print(line)
proc.stdout.close()
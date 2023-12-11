import os
import time


def hello_world(proc_name):
    for x in range(10):
        print(f"{proc_name} proc Pid({os.getpid()}) PPid({os.getppid()}): Hello World x{x}!")
        time.sleep(3)
    exit(123)


def run():
    print(f"Parent process started with Pid({os.getpid()})...")
    child_pid = os.fork()  # copy context, fork and start child process
    if child_pid == 0:  # check if proc is a child, only parent process will receive child pid
        hello_world("child")  # only child will execute this code
    else:
        hello_world("parent")
        exit_codes = os.wait()  # wait for child processes to end, to avoid zombies
        print(f"Child exit codes: {exit_codes}")


if __name__ == "__main__":
    run()
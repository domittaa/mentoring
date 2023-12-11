import signal, os
import time


def child_proc():
    while 1:
        print(f"Child proc Pid({os.getpid()}) PPid({os.getppid()}): Hello World!")
        time.sleep(2)
    print("Kiddo goes to sleep...")  # Won't reach this code...
    exit(0)


KIDDOS = []


def handler(signum, frame):
    signame = signal.Signals(signum).name
    print(f"Signal catched: {signame}!")
    print(f"Stopping child processes...")
    for pid in KIDDOS:
        os.kill(pid, signum)
    exit(0)


def run():
    print(f"Parent process started with Pid({os.getpid()})...")
    signal.signal(signal.SIGINT, handler)
    #signal.signal(signal.SIGKILL, handler)  # SIGKILL CAN'T BE HANDLED!
    signal.signal(signal.SIGTERM, handler)
    for x in range(3):
        child_pid = os.fork()
        if child_pid == 0:
            child_proc()
        else:
            KIDDOS.append(child_pid)
    if KIDDOS:
        for _ in KIDDOS:
            exit_codes = os.wait()
            print(f"Child exit codes: {exit_codes}")


if __name__ == "__main__":
    run()
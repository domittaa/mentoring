import random
import signal, os
import time
from multiprocessing import Semaphore, Value


def child_proc(kiddo_name):
    for x in range(5):
        print(f"{kiddo_name} proc Pid({os.getpid()}) wait to acquire semaphore...")
        SEMAPHORE.acquire()  # Get access to critical section!
        print(f"{kiddo_name} proc Pid({os.getpid()}) current shared value: {SHARED_VALUE.value}")
        SHARED_VALUE.value = random.randint(0, 1000)
        time.sleep(random.randint(1,5))
        print(f"{kiddo_name} proc Pid({os.getpid()}) value changed, releasing semaphore...")
        SEMAPHORE.release()
    print("Kiddo goes to sleep...")
    exit(0)


def child_proc_nonblocking(kiddo_name):
    for x in range(5):
        print(f"{kiddo_name} proc Pid({os.getpid()}) wait to acquire semaphore...")
        while True:
            if SEMAPHORE.acquire(block=False):  # Get access to critical section!
                print(f"{kiddo_name} proc Pid({os.getpid()}) current shared value: {SHARED_VALUE.value}")
                SHARED_VALUE.value = random.randint(0, 1000)
                time.sleep(random.randint(1,5))
                print(f"{kiddo_name} proc Pid({os.getpid()}) value changed, releasing semaphore...")
                SEMAPHORE.release()
                break
            else:
                print(f"{kiddo_name} proc Pid({os.getpid()}) doing other stuff...")
                time.sleep(random.randint(0, 3))
    print("Kiddo goes to sleep...")


KIDDOS = []
SEMAPHORE = Semaphore()
SHARED_VALUE = Value("d", -1)


def run():
    print(f"Parent process started with Pid({os.getpid()})...")
    for x in range(3):
        child_pid = os.fork()
        if child_pid == 0:
            child_proc_nonblocking(f"Kid #{x+1}")
            exit(0)
        else:
            KIDDOS.append(child_pid)
    for _ in KIDDOS:
        exit_code = os.wait()
        print(f"Child exit code: {exit_code}")


if __name__ == "__main__":
    run()
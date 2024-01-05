'''
Zastanów się jak zaimplementować program daemon (działający w tle),
tak aby nie można było uruchomić go poraz kolejny jeżeli już działa?
'''
import os
import subprocess
import sys

import psutil


def infinite_loop():
    x = 0
    while True:
        x += 1
#
#
# if __name__ == '__main__':
#     myname = sys.argv[0]
#     my_pid = os.getpid()
#     for process in psutil.process_iter():
#         # if process.cmdline() == ['python', 'deamon.py', '&']:
#         #     sys.exit('Program already running')
#         if process.pid != my_pid:
#             for path in process.cmdline():
#                 if myname in path:
#                     sys.exit()
#     infinite_loop()

import os
import sys
import fcntl

lock_file = '/var/run/my_daemon.pid'


def check_pid():
    try:
        file = open(lock_file, 'w')
        fcntl.flock(file, fcntl.LOCK_EX | fcntl.LOCK_NB)
        file.write(str(os.getpid()))
        file.flush()
        return file
    except IOError:
        print("Daemon is already running.")
        sys.exit(1)


def cleanup(file):
    fcntl.flock(file, fcntl.LOCK_UN)
    file.close()


if __name__ == '__main__':
    lock = check_pid()
    infinite_loop()
    cleanup(lock)

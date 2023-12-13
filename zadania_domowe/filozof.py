'''
Zaimplementuj program rozwiązujący problem 5 filozofów.
'''
import threading
import time

'''
Semafor-> ogranicza liczbe procesow wchodzacych do sekcji krytycznej
'''


class Semaphore:
    def __init__(self, limit):
        self.lock = threading.Condition(lock=threading.Lock())  # allow thread to wait until notified by another thread
        self.value = limit

    def up(self):
        with self.lock:
            self.value += 1
            self.lock.notify()  # wake up one thread waiting on this condition, if any

    def down(self):
        with self.lock:
            while self.value == 0:
                self.lock.wait()  # Wait until notified or until a timeout occurs.
            self.value -= 1


class Fork:
    def __init__(self, id):
        self.id = id
        self.is_taken = False
        self.philosopher = -1
        self.lock = threading.Condition(threading.Lock())

    def take(self, philosopher):
        with self.lock:
            while self.is_taken:
                self.lock.wait()
            self.philosopher = philosopher
            self.is_taken = True
            print(f"Fork {self.id} taken by philosopher {philosopher}")
            self.lock.notify_all()  # Wake up all threads waiting on this condition.

    def drop(self, philosopher):
        with self.lock:
            while not self.is_taken:
                self.lock.wait()
            self.philosopher = -1
            self.is_taken = False
            print(f"Fork {self.id} dropped by philosopher {philosopher}")
            self.lock.notify_all()


class Philosopher(threading.Thread):
    def __init__(self, id, left_fork_id, right_fork_id, semaphore):
        threading.Thread.__init__(self)
        self.id = id
        self.semaphore = semaphore
        self.left_fork = left_fork_id
        self.right_fork = right_fork_id

    def think(self):
        print(f"Philosopher {self.id} is thinking")
        time.sleep(0.1)

    def eat(self):
        print(f"Philosopher {self.id} is eating")
        time.sleep(0.1)

    def run(self):
        self.semaphore.down()
        self.think()
        self.left_fork.take(self.id)
        self.right_fork.take(self.id)
        self.eat()
        self.left_fork.drop(self.id)
        self.right_fork.drop(self.id)
        self.semaphore.up()
        print(f"Philosopher {self.id} finished eating and thinking")


def main():
    number_of_philosophers = 5
    semaphore = Semaphore(number_of_philosophers)
    forks = [Fork(i) for i in range(number_of_philosophers)]
    philosophers = [
        Philosopher(i, forks[i], forks[(i+1) % number_of_philosophers], semaphore) for i in range(number_of_philosophers)
    ]
    for i in range(number_of_philosophers):
        philosophers[i].run()


if __name__ == '__main__':
    main()

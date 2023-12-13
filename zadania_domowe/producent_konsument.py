'''
Zaimplementuj program symulujący problem producent/konsument.
Liczba producentów, konsumentów i szybkość produkcji/konsumpcji ma być konfigurowalna.
Przetestuj program z różnymi parametrami.
'''
import time
from queue import Queue
from threading import Barrier, Thread


def producer(id,amount, barrier, queue):
    for i in range(amount):  # produce specified amount of things
        thing = f"Something produced by producer number {id}"
        time.sleep(1)
        queue.put(thing)
        print(f"Producer {id} created something")
    barrier.wait()  # wait for all producers
    if id == 0:
        queue.put(None)  # mark end


def consumer(id, queue):
    while True:
        thing = queue.get()
        if not thing:
            queue.put(thing)
            break
        time.sleep(1)
        print(f"Consumer {id} took something")


queue = Queue()

number_of_producers = 5
amount = 20
number_of_consumers = 10

barrier = Barrier(number_of_producers)

consumers = [Thread(target=consumer, args=(i, queue)) for i in range(number_of_consumers)]
producers = [Thread(target=producer, args=(i, amount, barrier, queue)) for i in range(number_of_producers)]

for producer in producers:
    producer.start()

for consumer in consumers:
    consumer.start()

for producers in producers:
    producer.join()

for consumer in consumers:
    consumer.join()


'''
Zaimplementuj program obliczający silnie matematyczną zadanej liczby.
Program ma rozdzielić obliczenia na kilka jednostek przetwarzających.
Zaimplementuj go przy pomocy wątków, procesów i asyncio.
'''
import asyncio
import threading
from multiprocessing import Pool


# n! = (n-1)!*n

def factorial_synchronous_recurrence(n):
    if n == 1:
        return 1
    return factorial_synchronous_recurrence(n-1) * n


def factorial_synchronous_loop(n):
    if n in (0, 1):
        return 1
    for i in range(1, n):
        n *= i
    return n


def partial_factorial_thread(start, end, result_list):
    result = 1
    for i in range(start, end):
        result *= i

    result_list.append(result)


def factorial_thread(n):
    result_list = []
    first_thread = threading.Thread(target=partial_factorial_thread, args=(1, (n//2)+1, result_list))
    second_thread = threading.Thread(target=partial_factorial_thread, args=((n//2)+1, n+1, result_list))
    threads = [first_thread, second_thread]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    final_result = 1
    for partial_result in result_list:
        final_result *= partial_result
    return final_result


def partial_factorial_process(chunks):
    result = 1
    for i in chunks:
        result *= i
    return result


def factorial_process(n, processes):
    numbers = range(1, n + 1)
    chunks = [numbers[i::processes] for i in range(processes)]

    with Pool(processes) as p:
        partial_result = p.map(partial_factorial_process, chunks)

    final_result = 1
    for part_result in partial_result:
        final_result *= part_result
    return final_result


async def partial_factorial_asyncio(start, end):
    result = 1
    for i in range(start, end):
        result *= i
    return result


async def factorial_asyncio(n):
    tasks = [partial_factorial_asyncio(1, (n//2)+1), partial_factorial_asyncio((n//2)+1, n+1)]
    results = await asyncio.gather(*tasks)

    final_result = 1

    for result in results:
        final_result *= result

    return final_result


async def factorial_main(n):
    result = await factorial_asyncio(n)
    return result


if __name__ == "__main__":
    print(f"Silnia rekurencja: {factorial_synchronous_recurrence(50)}")
    print(f"Silnia petla: {factorial_synchronous_loop(50)}")
    print(f"Silnia watki: {factorial_thread(50)}")
    print(f"Silnia procesy: {factorial_process(50, 5)}")
    print(f"Silnia acyncio: {asyncio.run(factorial_main(50))}")

'''
Rozwijasz asynchroniczną aplikację, potrzebujesz jednak modułu,
którego implementacja jest tylko i wyłącznie synchroniczna,
nie posiada on też żadnego asynchronicznego odpowiednika.
W jaki sposób zintegrujesz czasochłonny synchroniczny kod z asynchronicznym.
Zaimplementuj przykładowe rozwiązanie, np. łącząc asyncio i wątki/procesy do obliczeń wymagających dużego zużycia CPU.
'''
import asyncio
import time


def long_running_task():
    time.sleep(5)
    print("Long task finished")


async def main():
    coroutine = asyncio.to_thread(long_running_task)
    task = asyncio.create_task(coroutine)
    await asyncio.sleep(0)
    await task

asyncio.run(main())

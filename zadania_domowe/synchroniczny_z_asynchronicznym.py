'''
Rozwijasz asynchroniczną aplikację, potrzebujesz jednak modułu,
którego implementacja jest tylko i wyłącznie synchroniczna,
nie posiada on też żadnego asynchronicznego odpowiednika.
W jaki sposób zintegrujesz czasochłonny synchroniczny kod z asynchronicznym.
Zaimplementuj przykładowe rozwiązanie, np. łącząc asyncio i wątki/procesy do obliczeń wymagających dużego zużycia CPU.
'''

# async def main():
#     result = await loop.run_in_executor(None, long_running_task)
#     print(result)
#
# loop.run_until_compelete(main())
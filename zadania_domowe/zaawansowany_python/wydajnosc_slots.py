'''
5. Zbadaj w jaki sposób sloty/__slots__ wpływają na wydajność programu.
   W celach testowych zaimplementuj klasę np. Point wykorzystującą normalną przestrzeń nazw i sloty,
   a następnie przeprowadź na jej obiektach wiele operacji odczytu i przypisania.
   Do pomiarów skorzystaj przykładowo z narzędzi: kernprof/line_profiler, memory_profiler, modułu dis i time.
'''
import dis
import time
from memory_profiler import profile
from line_profiler import LineProfiler


class PointWithSlots:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y


class PointWithoutSlots:

    def __init__(self, x, y):
        self.x = x
        self.y = y


@profile
def with_slots():
    points = [PointWithSlots(i, i+1) for i in range(10000)]
    for point in points:
        point.x += 5
        point.y += 10
        total = point.x + point.y


@profile
def without_slots():
    points = [PointWithoutSlots(i, i + 1) for i in range(10000)]
    for point in points:
        point.x += 5
        point.y += 10
        total = point.x + point.y


# print("Analysis with slots:")
# print(dis.dis(with_slots))
# print("------------------")
# print("Analysis without slots:")
# print(dis.dis(without_slots))

# Time comparison
start_time = time.time()
with_slots()
print(f"Time taken with slots: {time.time() - start_time}")

start_time = time.time()
without_slots()
print(f"Time taken without slots: {time.time() - start_time}")

lp = LineProfiler()
lp.add_function(with_slots)
lp.add_function(without_slots)

lp.print_stats()

# Memory comparison (using memory_profiler)
# python3 -m memory_profiler zadania_domowe/zaawansowany_python/wydajnosc_slots.py

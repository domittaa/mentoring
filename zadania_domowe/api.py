'''
Zaimplementuj program, który w jednym wątku/procesie będzie udostępniać API,
a w innych będzie realizować jakieś proste zadania.
API ma udostępniać dane zwrócone przez wątki/procesy oraz ich status.
API ma pozwalać na kontrolowanie stanu procesów roboczych.
'''
import multiprocessing
import uvicorn

'''
Mamy dwa procesy/watki
1- api wystawione na fastapi
2- liczenie po kolei ciagu fibbonaciego

Api jest w stanie wyswietlic na ktorym aktualnie miejscu jestesmy w liczeniu (jaka ostatnia liczba byla wyliczona).
Api moze kontrolowac watek z liczeniem, jeden endpoint start/stop do uruchomienia watku,
drugi do wyswietlenia statusu czyli dziala/ nie dziala i jaki wynik
Przy odpytaniu endpointa watek z wyliczaniem liczb musi byc zatrzymany-> zrobic swoja zmienna warunkowa
'''
from fastapi import FastAPI
import time

app = FastAPI()

is_running = multiprocessing.Value('b', False)
last_calculations = multiprocessing.Value('i', 0)


def fibonacci(status, last_number):
    while True:
        if status.value:
            a, b = 0, 1
            while status.value:
                a, b = b, a + b
                with last_number.get_lock():
                    last_number.value = a
        else:
            time.sleep(1)


@app.get("/start_stop")
def start_stop(status: bool):
    global is_running
    with is_running.get_lock():
        is_running.value = status
    return {"message": f"Calculation {'started' if status else 'stopped'}"}


@app.get("/get_status")
async def status():
    global is_running, last_calculations
    with last_calculations.get_lock():
        return {
            "calculation_status": "running" if is_running.value else "stopped",
            "last_calculated_number": last_calculations.value
        }


if __name__ == "__main__":
    fibonacci_process = multiprocessing.Process(target=fibonacci, args=(is_running, last_calculations))
    fibonacci_process.start()
    uvicorn.run(app, host="localhost", port=8000)

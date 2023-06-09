from threading import Lock, Thread
from heapq import heappush, heappop


class Task:
    def __init__(self, name, pirority):
        self.name = name
        self.pirority = pirority


class Scheduler:
    _instance = None
    _task_queue = []
    _lock = Lock()

    @classmethod
    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                instance = super().__call__(*args, **kwargs)
                cls._instance[cls] = instance

        return cls._instance[cls]

    @classmethod
    def add_task(cls, task, pirority=0):
        heappush(cls._task_queue, (-pirority, task))

    @classmethod
    def execute_task(cls):
        while cls._task_queue:
            task = heappop(cls._task_queue)
            print(task[1])


def test_singleton():
    scheduler = Scheduler()

    print(scheduler)
    scheduler.add_task("task1", 1)
    scheduler.add_task("task2", 2)
    scheduler.add_task("task3", 3)

    scheduler.execute_task()

process1 = Thread(target=test_singleton)
process2 = Thread(target=test_singleton)

process1.start()
process2.start()

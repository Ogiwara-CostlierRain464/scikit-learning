import multiprocessing
import random
import time
from threading import current_thread
import rx
from rx.core import Observer
from rx.operators import subscribe_on, merge
from rx.scheduler import ThreadPoolScheduler
from rx import operators as ops
from enum import Enum

from rx.scheduler.scheduler import Scheduler
from rx.subject import ReplaySubject


class Operation(Enum):
    READ = "r"
    WRITE = "w"


class Data(Enum):
    X = "x"
    Y = "y"
    Z = "z"


class Locking(Enum):
    LOCK = "l"
    UNLOCK = "u"


class Step:
    pass


class Read(Step):
    def __init__(self, trn: int, data: Data):
        self.trn = trn
        self.data = data

    def __repr__(self):
        return f"r{self.trn}({self.data})"


class Write(Step):
    def __init__(self, trn: int, data: Data):
        self.trn = trn
        self.data = data

    def __repr__(self):
        return f"w{self.trn}({self.data})"


class Commit(Step):
    def __init__(self, trn: int):
        self.trn = trn

    def __repr__(self):
        return f"c{self.trn}"


class ReadLock(Step):
    def __init__(self, trn: int, data: Data):
        self.trn = trn
        self.data = data

    def __repr__(self):
        return f"rl{self.trn}({self.data})"


class WriteLock(Step):
    def __init__(self, trn: int, data: Data):
        self.trn = trn
        self.data = data

    def __repr__(self):
        return f"wl{self.trn}({self.data})"


def make_TM(observer: Observer, _: Scheduler):
    observer.on_next(Write(1, "x"))
    observer.on_next(Read(2, "y"))
    observer.on_next(Read(1, "x"))
    observer.on_next(Commit(1))
    observer.on_next(Read(2, "x"))
    observer.on_next(Write(2, "y"))
    observer.on_next(Commit(2))
    return observer


def a(step: Step):
    pass



TM = rx.create(make_TM)
pool = ThreadPoolScheduler(4)

TM.pipe(
    map(a)
).subscribe(
    on_next=lambda e: print(e)
)
#
# TM.pipe(
#     subscribe_on(pool),
# ).subscribe(
#     on_next=lambda e: print(e)
# )


if __name__ == "__main__":
    pass

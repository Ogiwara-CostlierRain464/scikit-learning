import time
from sys import stderr

from rx import create, interval
from rx.core import Observer
from rx.disposable import Disposable
from rx.operators import *
from rx.scheduler.scheduler import Scheduler
from rx.scheduler import ThreadPoolScheduler
from rx.subject import ReplaySubject

flow = ReplaySubject(None)

pool = ThreadPoolScheduler(1)


def on_well(e):
    if e == "Well":
        flow.on_next("E!")


flow.pipe(
    subscribe_on(pool),
    retry(3),
    do_action(on_next=on_well)
).subscribe(
    on_next=lambda s: print(s),
    on_error=lambda e: print(e, file=stderr)
)



while True:
    flow.on_next("Hi")
    time.sleep(1)
    flow.on_next("Well")
    time.sleep(1)
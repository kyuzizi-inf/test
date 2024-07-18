import random

@task(log_prints = True)
def add_int(a, b):
    print("%d 加 %d 是 %d"%(a, b, a + b))

@flow(name="simple_sum_up_test")
def sum_up_task():
    i = 0
    while(i <= 10):
        add_int(random.randint(0,100), random.randint(0,50))

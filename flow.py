from prefect import flow
import random

def add_int(a, b):
    print("%d 加 %d 是 %d"%(a, b, a + b))

@flow(log_prints=True)
def sum_up_task():
    i = 0
    while(i <= 10):
        i += 1 
        add_int(random.randint(0,100), random.randint(0,50))

if __name__ == "__main__":
    sum_up_task.from_source(
            "https://github.com/kyuzizi-inf/test.git",
            entrypoint="flow.py:sum_up_task",
    ). deploy(
        name = "simple-work-pool-test",
        work_pool_name = "developing-work-pool",
    )

from apscheduler.schedulers.blocking import BlockingScheduler
from honey_love import send_loves

# def job_function():
#     print("Hello World")

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
# Flooding love texts
sched.add_job(send_loves, 'interval', seconds=10)

sched.start()
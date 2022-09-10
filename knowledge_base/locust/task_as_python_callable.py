from locust import HttpUser, constant

def _get_task(api):
    def my_task(user):
        user.client.get(api)
    return my_task

def get_task():
    apis = ["/api/v1/Activities", "/api/v1/Authors"]
    tasks = []
    for api in apis:
        tasks.append(_get_task(api))
    return tasks

class MyUser(HttpUser):
    tasks = get_task()
    wait_time = constant(1)
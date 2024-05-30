from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    @task
    def stress_test_prom_client_side(self):
        self.client.get("/")
        self.client.get("/")

from locust import HttpUser, task

class StressTestProm(HttpUser):
    @task
    # Test for front end only
    # def stress_test_prom_client_side(self):
    #     self.client.get("/")
    #     self.client.get("/prom")

    # Test for backend and RDS side
    def stress_test_prom_client_side(self):
        # self.client.get("/")
        self.client.get("/prom")

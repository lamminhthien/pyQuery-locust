import random
from locust import HttpUser, task, between
from pyquery import PyQuery

class StressTestProm(HttpUser):
    wait_time = between(5, 9)
    @task

    # Test for backend and RDS side
    def stress_test_prom_client_side(self):
        # auto load test
        self.client.get("/prom?autoLoadTest=tCU9{Mx")
        # self.client.get("/prom")
        # self.client.get("/")
        # r = self.client.get("/prom")
        # pq = PyQuery(r.content)

        # # Find input email
        # email_input = pq('input[placeholder*="Nhập email"]').eq(0)
        # email_input.val("Thien1234@gmail.com")
        # if (email_input):
        #     print('Have email input')

        # random_number = random.randint(1, 600)

        # # Find input code
        # code_input = pq('input[placeholder*="Nhập mã code"]').eq(0)
        # code_input.val(random_number)
        # if (code_input):
        #     print('Have code input')

        # # Find first people to vote
        # first_person = pq.find('.flex.h-5.w-5.items-center.rounded-full.border.border-violet-600').eq(0)
        # first_person.click()
        # if (first_person):
        #     print('Have First person')

        # # Submit button
        # submit_button = pq.find('button:contains("Bình chọn")').eq(0)
        # submit_button.click()
        # if (submit_button):
        #     print('Bình chọn')

        # Test backend
        self.client.get("/prom")
        self.client.get("/")


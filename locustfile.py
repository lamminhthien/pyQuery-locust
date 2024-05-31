from bs4 import BeautifulSoup
from locust import HttpUser, task, between

class StressTestPROM(HttpUser):
    wait_time = between(1, 8)
    
    def on_start(self):
        self.client.get("/prom?autoLoadTestPass=tCU9{Mx")
    
    def crawl(self, path):
        response = self.client.get(path, name="[Page] "+path)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            
            # Discover linked pages
            links = [a["href"] for a in soup.find_all("a", href=True)]
            for link in links:
                self.crawl(link)
            
            # Load static content (img, css, js)
            resources = [(link["href"], "CSS") for link in soup.find_all("link", href=True)]
            resources += [(script["src"], "JS") for script in soup.find_all("script", src=True)]
            resources += [(img["src"], "IMG") for img in soup.find_all("img", src=True)]

            for resource, res_type in resources:
                print("Debug resource")
                print(resource)
                self.client.get(resource, name=f"[{res_type}] {resource}")
            
        # Go home after submit
        self.client.get("/")
    
    @task(1)
    def stress_test_prom(self):
        self.client.get("/prom?autoLoadTestPass=tCU9{Mx")

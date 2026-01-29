from locust import HttpUser, task, between

class EventsUser(HttpUser):
    host = "http://localhost:8000"   # explicit host
    wait_time = between(0.5, 1.5)    # more realistic traffic

    @task(3)  # higher weight
    def view_events(self):
        with self.client.get(
            "/events?user=locust_user",
            timeout=2,
            catch_response=True
        ) as response:
            if response.status_code != 200:
                response.failure(f"Status code {response.status_code}")
            elif response.elapsed.total_seconds() > 1:
                response.failure("Response too slow")
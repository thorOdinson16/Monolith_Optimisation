from locust import HttpUser, task, between

class MyEventsUser(HttpUser):
    host = "http://localhost:8000"     # always define
    wait_time = between(0.5, 1.5)

    @task
    def view_my_events(self):
        with self.client.get(
            "/my-events?user=locust_user",
            timeout=2,
            catch_response=True
        ) as response:
            if response.status_code != 200:
                response.failure("Non-200 response")
            elif response.elapsed.total_seconds() > 1:
                response.failure("Slow response (>1s)")
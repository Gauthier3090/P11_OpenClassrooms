from locust import HttpUser, task, between
from app import load_clubs, load_competitions


class LocusTest(HttpUser):
    wait_time = between(1, 5)
    competitions = load_competitions()[2]
    clubs = load_clubs()[0]

    def on_start(self):
        self.client.get("/", name="index")
        self.client.post("/show-summary", data={'email': self.clubs["email"]}, name="show_summary")

    @task
    def get_booking(self):
        self.client.get(f"/book/{self.competitions['name']}/{self.clubs['name']}", name="book")

    @task
    def post_booking(self):
        self.client.post(
            "/purchase-places",
            data={
                "places": 0,
                "club": self.clubs["name"],
                "competition": self.competitions["name"]
            }, name="purchase_places")

    @task
    def get_board(self):
        self.client.get("/clubs", name="clubs")

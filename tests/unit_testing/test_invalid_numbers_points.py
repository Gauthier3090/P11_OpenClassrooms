import server
from server import app


class TestInvalidNumbersPoints:
    client = app.test_client()
    competitions = [
        {
            "name": "Test Competition",
            "date": "2022-07-19 13:00:59",
            "numberOfPlaces": "12"
        }
    ]

    clubs = [
        {
            "name": "Test Club",
            "email": "club@gmail.com",
            "points": "10"
        }
    ]

    def init_fake_db(self):
        server.competitions = self.competitions
        server.clubs = self.clubs

    def test_points_allowed(self):
        result = self.client.post(
            "/purchase-places",
            data={
                "places": 3,
                "club": self.clubs[0]["name"],
                "competition": self.competitions[0]["name"]
            }
        )

        assert result.status_code == 200
        assert "Great-booking complete!" in result.data.decode()
        assert int(self.clubs[0]["points"]) >= 0

    def test_points_not_allowed(self):
        result = self.client.post(
            "/purchase-places",
            data={
                "places": 5,
                "club": self.clubs[0]["name"],
                "competition": self.competitions[0]["name"]
            }
        )

        assert result.status_code == 400
        assert "have enough points." in result.data.decode()
        assert int(self.clubs[0]["points"]) >= 0

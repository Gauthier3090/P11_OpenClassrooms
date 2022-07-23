import server
from server import app


class TestMorePointsAllowed:
    client = app.test_client()
    competitions = [
        {
            "name": "Test Competition",
            "date": "2022-07-19 13:00:59",
            "numberOfPlaces": "50"
        }
    ]

    clubs = [
        {
            "name": "Test Club",
            "email": "club@gmail.com",
            "points": "75"
        }
    ]

    places_booked = [
        {
            "competition": "Test Competition",
            "booked": [5, "Test Club"]
        }
    ]

    def init_fake_db(self):
        server.competitions = self.competitions
        server.clubs = self.clubs
        server.places_booked = self.places_booked

    def test_valid_points(self):
        booked = 5

        result = self.client.post(
            "/purchase-places",
            data={
                "places": booked,
                "club": self.clubs[0]["name"],
                "competition": self.competitions[0]["name"]
            }
        )

        assert result.status_code == 200
        assert "Great-booking complete!" in result.data.decode()

    def test_invalid_points(self):
        booked = 13

        result = self.client.post(
            "/purchase-places",
            data={
                "places": booked,
                "club": self.clubs[0]["name"],
                "competition": self.competitions[0]["name"]
            }
        )

        assert result.status_code == 400
        assert "more than 12 places in a competition." in result.data.decode()

    def test_overbooked_competitions(self):
        booked = 8

        result = self.client.post(
            "/purchase-places",
            data={
                "places": booked,
                "club": self.clubs[0]["name"],
                "competition": self.competitions[0]["name"]
            }
        )

        assert result.status_code == 400
        assert "more than 12 places in a competition." in result.data.decode()

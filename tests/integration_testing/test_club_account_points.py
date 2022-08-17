import server
from server import app


class TestClubAccountPoints:
    client = app.test_client()
    competitions = [
        {
            "name": "Test Competition",
            "date": "2023-03-27 10:00:00",
            "numberOfPlaces": "25"
        }
    ]

    clubs = [
        {
            "name": "Test club",
            "email": "testclub@gmail.com",
            "points": "10"
        }
    ]

    def setup_method(self):
        server.competitions = self.competitions
        server.clubs = self.clubs

    def test_points_update(self):
        club_points_before = int(self.clubs[0]["points"])
        places_booked = 1

        self.client.post(
            "/purchase-places",
            data={
                "places": places_booked,
                "club": self.clubs[0]["name"],
                "competition": self.competitions[0]["name"]
            }
        )

        result = self.client.get("/clubs")

        assert result.status_code == 200
        assert f"<td>{self.clubs[0]['name']}</td>" in result.data.decode()
        assert f"<td>{club_points_before - places_booked * 3}</td>" in result.data.decode()

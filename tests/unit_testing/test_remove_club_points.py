from server import app
import server


class TestRemoveClubPoints:
    client = app.test_client()
    competitions = [
        {
            "name": "Competition Test",
            "date": "2023-03-27 10:00:00",
            "numberOfPlaces": "25"
        }
    ]

    clubs = [
        {
            "name": "Club Test",
            "email": "ClubTest@gmail.com",
            "points": "10"
        }
    ]

    def setup_method(self):
        server.competitions = self.competitions
        server.clubs = self.clubs

    def test_deduct_points(self):
        club_points_before = int(self.clubs[0]["points"])
        places_booked = 3

        result = self.client.post(
            "/purchase-places",
            data={
                "places": places_booked,
                "club": self.clubs[0]["name"],
                "competition": self.competitions[0]["name"]
            }
        )

        assert result.status_code == 200
        assert "Great-booking complete!" in result.data.decode()
        assert int(self.clubs[0]["points"]) == club_points_before - places_booked * 3

    def test_empty_field(self):
        places_booked = ""

        result = self.client.post(
            "/purchase-places",
            data={
                "places": places_booked,
                "club": self.clubs[0]["name"],
                "competition": self.competitions[0]["name"]
            }
        )

        assert result.status_code == 400
        assert "Please enter a number between 0 and 12." in result.data.decode()

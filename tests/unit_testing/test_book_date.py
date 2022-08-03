import server
from server import app


class TestBookDate:
    client = app.test_client()

    competitions = [
        {
            "name": "Competition Closed",
            "date": "2019-04-27 10:00:00",
            "numberOfPlaces": "20"
        },
        {
            "name": "Competition Open",
            "date": "2023-11-06 10:00:00",
            "numberOfPlaces": "20"
        }
    ]

    clubs = [
        {
            "name": "Club Test",
            "email": "testclub@email.com",
            "points": "15"
        }
    ]

    def setup_method(self):
        server.competitions = self.competitions
        server.clubs = self.clubs

    def test_book_is_closed(self):
        result = self.client.get(
            f"/book/{self.competitions[0]['name']}/{self.clubs[0]['name']}"
        )
        assert result.status_code == 400
        assert "This competition is over." in result.data.decode()

    def test_book_is_open(self):
        result = self.client.get(
            f"/book/{self.competitions[1]['name']}/{self.clubs[0]['name']}"
        )
        assert result.status_code == 200

    def test_book_is_invalid(self):
        result = self.client.get(
            f"/book/fake-club/{self.clubs[0]['name']}"
        )
        assert result.status_code == 404
        assert "Something went wrong-please try again" in result.data.decode()

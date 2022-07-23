import server
from server import app


class TestLoginEmail:
    client = app.test_client()

    def test_valid_email(self):
        res = self.client.post("/show-summary", data={"email": server.clubs[0]["email"]})
        assert res.status_code == 200
        assert f"{server.clubs[0]['email']}" in res.data.decode()

    def test_invalid_email(self):
        res = self.client.post("/show-summary", data={"email": "test@gmail.com"})
        assert res.status_code == 401
        assert "No account related to this email." in res.data.decode()

    def test_empty_email(self):
        res = self.client.post("/show-summary", data={"email": ""})
        assert res.status_code == 401
        assert "Please enter your email." in res.data.decode()

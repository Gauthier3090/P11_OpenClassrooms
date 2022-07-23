from server import app


class TestLoginLogout:
    client = app.test_client()

    def test_login(self):
        res = self.client.get("/")
        assert res.status_code == 200

    def test_logout(self):
        res = self.client.get("/logout")
        assert res.status_code == 302

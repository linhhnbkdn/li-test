from django.contrib.auth.models import User
from django.test import TestCase


class LoginAPITest(TestCase):
    def setUp(self) -> None:
        User.objects.create_user(
            username="admin",
            email="admin@gmail.com",
            password="admin@Admin124",
        )
        return super().setUp()

    def test_login_with_username(self):
        response = self.client.post(
            "/oauth/login/",
            {
                "user_id": "admin",
                "password": "admin@Admin124",
                "remmber_me": False,
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["username"], "admin")
        self.assertEqual(response.json()["email"], "admin@gmail.com")

    def test_login_with_email(self):
        response = self.client.post(
            "/oauth/login/",
            {
                "user_id": "admin@gmail.com",
                "password": "admin@Admin124",
                "remmber_me": False,
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["username"], "admin")
        self.assertEqual(response.json()["email"], "admin@gmail.com")

    def test_login_with_invalid_user_id(self):
        response = self.client.post(
            "/oauth/login/",
            {
                "user_id": "admin1",
                "password": "admin@Admin124",
                "remmber_me": False,
            },
        )
        self.assertEqual(response.status_code, 401)
        self.assertEqual(
            response.json(),
            {"error": "Invalid username or password"},
        )

    def test_login_with_invalid_password(self):
        response = self.client.post(
            "/oauth/login/",
            {
                "user_id": "admin",
                "password": "admin@Admin1245",
                "remmber_me": False,
            },
        )
        self.assertEqual(response.status_code, 401)
        self.assertEqual(
            response.json(),
            {"error": "Invalid username or password"},
        )

    def test_login_with_empty_user_id(self):
        response = self.client.post(
            "/oauth/login/",
            {
                "user_id": "",
                "password": "admin@Admin124",
                "remmber_me": False,
            },
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(),
            {"user_id": ["This field may not be blank."]},
        )

    def test_login_with_empty_password(self):
        response = self.client.post(
            "/oauth/login/",
            {
                "user_id": "admin",
                "password": "",
                "remmber_me": False,
            },
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(),
            {"password": ["This field may not be blank."]},
        )

    def test_login_without_remmber_me_flag(self):
        response = self.client.post(
            "/oauth/login/",
            {
                "user_id": "admin",
                "password": "admin@Admin124",
                "remmber_me": False,
            },
        )
        self.assertEqual(response.status_code, 200)
        session = self.client.session
        session_expiry = session.get_expiry_age()
        self.assertEqual(session_expiry, 0)

    def test_login_with_remmber_me_flag(self):
        response = self.client.post(
            "/oauth/login/",
            {
                "user_id": "admin",
                "password": "admin@Admin124",
                "remmber_me": True,
            },
        )
        self.assertEqual(response.status_code, 200)
        session = self.client.session
        session_expiry = session.get_expiry_age()
        self.assertEqual(session_expiry, 60 * 60 * 24 * 30)

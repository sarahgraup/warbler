"""User views tests."""

from app import app, CURR_USER_KEY
import os
from unittest import TestCase
from flask_bcrypt import Bcrypt
from flask import session
from datetime import datetime

from models import db, User, Message, Follows

bcrypt = Bcrypt()

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql:///warbler_test"

# Now we can import app


# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

db.drop_all()
db.create_all()

"""
When you’re logged in, can you see the follower / following pages for any user?
When you’re logged out, are you disallowed from visiting a user’s follower / following pages?
When you’re logged in, can you add a message as yourself?
When you’re logged in, can you delete a message as yourself?
When you’re logged out, are you prohibited from adding messages?
When you’re logged out, are you prohibited from deleting messages?
When you’re logged in, are you prohibited from deleting another user’s message?
"""
class UserViewTestCase(TestCase):
    def setUp(self):
        User.query.delete()

        u1 = User.signup("u1", "u1@email.com", "password", None)
        u2 = User.signup("u2", "u2@email.com", "password", None)
        
        db.session.add(u1)
        db.session.add(u2)

        db.session.commit()
        self.u1_id = u1.id
        self.u2_id = u2.id

        m1 = Message(
            text = "text",
            timestamp = datetime.utcnow,
            user_id = u1.id
        )
        db.session.commit()

        self.client = app.test_client()

    def tearDown(self):
        db.session.rollback()

    def delete_message_fail(self):
        with self.client as c:
            resp = c.post(
                "/messages/"

            )


    # # def test_homepage_redirect(self):
    # #     with app.test_client() as client:
    # #         resp = client.get("/")
    # #         self.assertEqual(resp.status_code, 302)
    # #         self.assertEqual(resp.location, "/")

    # def test_signup_form(self):
    #     with app.test_client() as client:
    #         resp = client.get("/signup")
    #         html = resp.get_data(as_text=True)
    #         self.assertIn("Join Warbler today", html)

    # def test_signup_ok(self):
    #     with app.test_client() as client:
    #         resp = client.post(
    #             "/signup",
    #             data={
    #                 "username": "test",
    #                 "password": "password",
    #                 "email": "e@e.com",
    #                 "image_url": "None"
    #             }
    #         )
    #         self.assertEqual(resp.status_code, 200)
    #         self.assertEqual(resp.location, "/")


    # def test_signup_bad_form(self):
    #     with app.test_client() as client:
    #         resp = client.post(
    #             "/register",
    #             data={
    #                 "username": "test",
    #                 "password": "password",
    #                 "email": "egg",
    #                 "image_url": "None"
    #             }
    #         )
    #         html = resp.get_data(as_text=True)
    #         self.assertEqual(resp.status_code, 200)
    #         self.assertIn("Invalid email address", html)

    # def test_login_form(self):
    #     with app.test_client() as client:
    #         resp = client.get("/login")
    #         html = resp.get_data(as_text=True)
    #         self.assertIn("Welcome", html)

    # def test_login_ok(self):
    #     with app.test_client() as client:
    #         resp = client.post(
    #             "/login",
    #             data={
    #                 "username": "user-1",
    #                 "password": "password",
    #             }
    #         )
    #         self.assertEqual(resp.status_code, 200)
    #         self.assertEqual(resp.location, "/")
    #         self.assertEqual(session.get("username"), "user-1")

    # def test_login_bad(self):
    #     with app.test_client() as client:
    #         resp = client.post(
    #             "/login",
    #             data={
    #                 "username": "u1",
    #                 "password": "wrong-wrong",
    #             }
    #         )
    #         html = resp.get_data(as_text=True)
    #         self.assertEqual(resp.status_code, 404)
    #         self.assertIn("Invalid credentials.", html)
    #         self.assertEqual(session.get(CURR_USER_KEY), None)

    # def test_logout(self):
    #     with app.test_client() as client:
    #         with client.session_transaction() as sess:
    #             sess[CURR_USER_KEY] = self.u1_id
    #         resp = client.post(
    #             "/logout",
    #         )
    #         self.assertEqual(resp.status_code, 200)
    #         self.assertEqual(resp.location, "/login")
    #         self.assertEqual(session.get(CURR_USER_KEY), None)

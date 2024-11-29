from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from CodeFlow.accounts.models import Profile


class ProfileModelTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="password123"
        )

    def test_first_name_length_validation(self):
        profile = Profile(user=self.user, first_name="A")
        with self.assertRaises(ValidationError):
            profile.full_clean()

        profile.first_name = "A" * (Profile.MAX_LEN_NAME + 1)
        with self.assertRaises(ValidationError):
            profile.full_clean()

    def test_last_name_length_validation(self):
        profile = Profile(user=self.user, last_name="A")
        with self.assertRaises(ValidationError):
            profile.full_clean()

        profile.last_name = "A" * (Profile.MAX_LEN_NAME + 1)
        with self.assertRaises(ValidationError):
            profile.full_clean()


    def test_get_full_name(self):
        profile = Profile(user=self.user, first_name="John", last_name="Doe")
        self.assertEqual(profile.get_full_name(), "John Doe")

        profile.last_name = None
        self.assertEqual(profile.get_full_name(), "John")

        profile.first_name = None
        self.assertEqual(profile.get_full_name(), "No name given.")

    def test_profile_picture_validation(self):
        profile = Profile(user=self.user, profile_picture="invalid_image_path")
        with self.assertRaises(ValidationError):
            profile.full_clean()

    def test_save_method_cleans_up_empty_fields(self):
        profile = Profile(user=self.user, first_name="", last_name="None")
        profile.save()

        self.assertIsNone(profile.first_name)
        self.assertIsNone(profile.last_name)
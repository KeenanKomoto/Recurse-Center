from django.test import TestCase
from django.urls import resolve
from user_accounts.views import signup 

# Create your tests here.
class SmokeTest(TestCase):

    def test_resolving_url(self):
        found = resolve('/user_accounts/signup/')
        self.assertEqual(found.func, signup)



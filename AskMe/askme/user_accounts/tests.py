from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from user_accounts.views import signup, fake

# Create your tests here.
class SmokeTest(TestCase):

    def test_resolving_url(self):
        found = resolve('/user_accounts/signup/')
        self.assertEqual(found.func, signup)

    def test_fake(self):
        request = HttpRequest()
        response = fake(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<h1>WTF?</h1>', html)
        self.assertTrue(html.endswith('</html>'))

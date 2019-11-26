from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from core.utils import setup_view
from .views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_topscorers_view(self):
        found = resolve('/')
        self.assertEquals(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Login</title>', html)
        self.assertTrue(html.endswith('</html>'))
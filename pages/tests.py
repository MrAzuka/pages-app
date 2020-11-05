from django.test import TestCase, SimpleTestCase

# Create your tests here.
class SimpleTests(SimpleTestCase):
    def test_hompage(self):
        res = self.client.get('/')
        self.assertTrue(res.status_code, 200)


    def test_about(self):
        res = self.client.get('/about/')
        self.assertTrue(res.status_code, 200)

from django.test import TestCase

from django.test import TestCase, Client
from django.urls import reverse

class SayHelloViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_say_hello_response(self):
        response = self.client.get('/sayHi/')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content.decode(), {"message": "how are you"})



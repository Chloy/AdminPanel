from django.test import TestCase

class TestTest(TestCase):
    
    def test(self):
        self.assertIs(False, True, 'Nice')

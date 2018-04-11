from django.test import TestCase, Client
from django.contrib.auth.models import User

# Create your tests here.
class Test_User_Functionality(TestCase):
    def test_user_login(self):
        client = Client()
        client.login(username='john', password='smith')
    
    def test_user_logout(self):
        client = Client()
        client.logout()
    
    def test_user_registration(self):
        self.adminuser = User.objects.create_user('john', 'tenth@doctor.com', 'smith')
from django.test import TestCase
from .views import *

class MessageViewTests(TestCase):
    def test_inbox_template(self):
        response = self.client.get('/messenger/inbox/')
        self.assertTemplateUsed(response, "messenger/inbox.html")
        
    def test_post_message(self):
        sender = User.objects.create_user('sender', 'sender@example.com', 'sender')
        recipient = User.objects.create_user('recipient', 'recipient@example.com', 'recipient')
        self.client.login(username="sender", password="sender")
        
        message = {
            "subject": "Test Subject",
            "body": "Test Body",
            "recipient": recipient.id
        }

        response = self.client.post('/messenger/inbox/compose_message/', message)
        self.assertEqual(response.status_code, 302)
    
    def test_delete_message_that_exists(self):
        sender = User(username="sender")
        sender.save()
    
        recipient = User(username="receiver")
        recipient.save()
    
        message = Message(
            subject = "Test Subject",
            body = "Test Body",
            sender = sender,
            recipient = recipient)
        message.save()
    
        response = self.client.get('/messenger/delete_message/1')
        self.assertEqual(response.status_code, 302)
    
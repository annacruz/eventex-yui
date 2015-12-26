from django.core import mail
from django.test import TestCase

class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name="John Doe", cpf="11111111111", email="john@doe.com", phone="21-12345-1234")
        self.resp = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de Inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'john@doe.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = ['John Doe',
                    '11111111111',
                    'john@doe.com',
                    '21-12345-1234'
                    ]

        for content in contents:
            self.assertIn(content, self.email.body)

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.test import Client


class AccountsTest(TestCase):
    username = 'test_user'
    email = 'test_user@smthng.com'

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            self.username,
            self.email,
        )

    def test_login_page_by_url(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200, msg='login page by url is not working')

    def test_login_page_url_by_name(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200, msg='login page url by name is not working')

    def test_login_template(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, template_name='registration/login.html')

    def test_login_user(self):
        response = Client().post(reverse('login'), {'username': self.username})
        self.assertEqual(response.status_code, 200, msg='login user is not working')

    def test_signup_page_by_url(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200, msg='signup page by url is not working')

    def test_signup_page_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200, msg='signup page url by name is not working')

    def test_signup_template(self):
        response = self.client.get(reverse('signup'))
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_signup_user(self):
        self.assertEqual(get_user_model().objects.all().count(), 1, msg='signup a user is not working')
        self.assertEqual(get_user_model().objects.all()[0].username, self.username, msg='signup usernames not working')
        self.assertEqual(get_user_model().objects.all()[0].email, self.email, msg='signup user email is not working')

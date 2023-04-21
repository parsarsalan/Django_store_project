from django.test import TestCase
from django.urls import reverse


class PagesTests(TestCase):

    def test_home_by_url(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200, msg='Home by url is not worked')

    def test_home_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200, msg='Home url by name is not worked')

    def test_home_template_name(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, template_name='home.html')

    def test_home_page_title(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'home page')

    def test_about_us_by_url(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200, msg='about us by url is not worked')

    def test_about_us_url_by_name(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200, msg='about us url by name is not worked')

    def test_about_us_template_name(self):
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, template_name='pages/about_us.html')

    def test_about_us_title(self):
        response = self.client.get(reverse('about'))
        self.assertContains(response, 'this is about us page without any design')

    def test_contact_us_by_url(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200, msg='contact us by url is not worked')

    def test_contact_us_url_by_name(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200, msg='contact us url by name is not worked')

    def test_contact_us_template(self):
        response = self.client.get(reverse('contact'))
        self.assertTemplateUsed(response, template_name='pages/contact_us.html')

    def test_contact_us_title(self):
        response = self.client.get(reverse('contact'))
        self.assertContains(response, 'this is Contact us page without any design')

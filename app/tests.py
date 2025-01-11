from http.client import responses

from rest_framework.reverse import reverse_lazy
from rest_framework.test import APITestCase

from app.models import Category, Post


# Create your tests here.

class AppAPITestCase(APITestCase):

    def format_datetime(self, value):

        return value.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

class TestCategory(AppAPITestCase):

    url = reverse_lazy('category-list')

    def test_list(self):

        category1 = Category.objects.create(name='Category 1', active=True)
        Category.objects.create(name='Category 2', active=False)

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        expected = [
            {
                'id': category1.pk,
                'name': category1.name,
                'active': True
            }
        ]
        self.assertEqual(expected, response.json())

    def test_create(self):

        self.assertFalse(Category.objects.exists())
        response = self.client.post(self.url, data={'name': 'Nouvelle categorie'})

        self.assertEqual(response.status_code, 405)

        self.assertFalse(Category.objects.exists())

class TestPost(AppAPITestCase):

    url = reverse_lazy('post-list')

    def test_list(self):

        post1 = Post.objects.create(title='Post 1', content='Contenu 1', active=True)
        Post.objects.create(title='Post 2', content='Contenu 2', active=False)

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        expected = [
            {
                'id': post1.pk,
                'title': post1.title,
                'content': post1.content,
                'category': None,
                'active': True,
                'date_posted': self.format_datetime(post1.date_posted),
                'date_updated': self.format_datetime(post1.date_updated)
            }
        ]

        self.assertEqual(expected, response.json())

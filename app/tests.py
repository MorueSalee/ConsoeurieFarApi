from http.client import responses

from rest_framework.reverse import reverse_lazy, reverse
from rest_framework.test import APITestCase

from app.models import Category, Post, Comment


# Create your tests here.

class AppAPITestCase(APITestCase):

    def format_datetime(self, value):

        return value.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    @classmethod
    def setUpTestData(cls):
        cls.category_1 = Category.objects.create(name='Categorie 1', active=True)
        Category.objects.create(name='Categorie 2', active=False)

        cls.post_1 = cls.category_1.posts.create(title='Post 1', active=True, content='Contenu 1', author='Auteur 1', likes=1)
        cls.category_1.posts.create(title='Post 2', active=False, content='Contenu 2', author='Auteur 2', likes=2)

        cls.category_3 = Category.objects.create(name='Categorie 3', active=True)
        cls.post_3 = cls.category_3.posts.create(title='Post 3', active=True, content='Contenu 3', author='Auteur 3', likes=3)

        cls.comment_1 = cls.post_1.comments.create(author='Auteur 1', content='Contenu 1', active=True, likes=1)
        cls.post_1.comments.create(author='Auteur 2', content='Contenu 2', active=False, likes=2)

    def get_comment_list_data(self, comments):
        return [
            {
                'id': comment.pk,
                'post': comment.post_id,
                'author': comment.author,
                'likes': comment.likes,
                'active': comment.active,
                'content': comment.content,
                'date_posted': self.format_datetime(comment.date_posted),
                'date_updated': self.format_datetime(comment.date_updated),
            } for comment in comments
        ]

    def get_post_list_data(self, posts):
        return [
            {
                'id': post.pk,
                'category': post.category_id,
                'author': post.author,
                'likes': post.likes,
                'active': post.active,
                'title': post.title,
                'content': post.content,
                'date_posted': self.format_datetime(post.date_posted),
                'date_updated': self.format_datetime(post.date_updated),
            } for post in posts
        ]

    def get_category_list_data(self, categories):
        return [
            {
                'id': category.id,
                'name': category.name,
                'active': category.active,
                # 'posts': self.get_post_list_data(category.posts.filter(active=True))
            } for category in categories
        ]

class TestCategory(AppAPITestCase):

    url = reverse_lazy('category-list')

    def test_list(self):

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.get_category_list_data([self.category_1, self.category_3]), response.json()['results'])

    def test_create(self):

        category_count = Category.objects.count()

        response = self.client.post(self.url, data={'name': 'Nouvelle catégorie'})

        self.assertEqual(response.status_code, 405)
        self.assertEqual(Category.objects.count(), category_count)

class TestPost(AppAPITestCase):

    url = reverse_lazy('post-list')

    def test_list(self):

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.get_post_list_data([self.post_1, self.post_3]), response.json()['results'])

    def test_list_filter(self):

        response = self.client.get(self.url + '?category_id=%i' % self.category_1.pk)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.get_post_list_data([self.post_1]), response.json()['results'])

    def test_create(self):

        product_count = Post.objects.count()

        response = self.client.post(self.url, data={'name': 'Nouvel article'})

        self.assertEqual(response.status_code, 405)
        self.assertEqual(Post.objects.count(), product_count)

    def test_delete(self):

        response = self.client.delete(reverse('post-detail', kwargs={'pk': self.post_1.pk}))

        self.assertEqual(response.status_code, 405)
        self.post_1.refresh_from_db()

class TestComment(AppAPITestCase):

    url = reverse_lazy('comment-list')

    def test_list(self):

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.get_comment_list_data([self.comment_1]), response.json()['results'])

    def test_list_filter(self):

        response = self.client.get(self.url + '?post_id=%i' % self.post_1.pk)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.get_comment_list_data([self.comment_1]), response.json()['results'])

    def test_create(self):

        comment_count = Comment.objects.count()

        response = self.client.post(self.url, data={'name': 'Nouveau commentaire'})

        self.assertEqual(response.status_code, 405)
        self.assertEqual(Comment.objects.count(), comment_count)

    def test_delete(self):

        response = self.client.delete(reverse('comment-detail', kwargs={'pk': self.comment_1.pk}))

        self.assertEqual(response.status_code, 405)
        self.comment_1.refresh_from_db()
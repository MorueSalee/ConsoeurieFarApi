from django.db import models, transaction

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    active = models.BooleanField(default=True)
    likes = models.IntegerField(default=0)

    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, related_name='posts')

    def __str__(self):
        return self.title

    @transaction.atomic
    def like(self):
        self.likes = self.likes + 1
        self.save()

    @transaction.atomic
    def dislike(self):
        self.likes = self.likes - 1
        self.save()

class Comment(models.Model):
    author = models.CharField(max_length=100, default='Inconnu')
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    active = models.BooleanField(default=True)
    likes = models.IntegerField(default=0)

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.content

    @transaction.atomic
    def like(self):
        self.likes = self.likes + 1
        self.save()

    @transaction.atomic
    def dislike(self):
        self.likes = self.likes - 1
        self.save()
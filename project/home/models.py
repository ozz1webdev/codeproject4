from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.
class Post(models.Model):
    """
    This is a model to create a post
    """
    user = models.ForeignKey(User, related_name='post_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=300, unique=True, null=False, blank=False)
    content = models.TextField()
    image = CloudinaryField('image', default='placeholder', null=True, blank=True)
    youtube_link = models.CharField(max_length=300, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes_count = models.ManyToManyField(User, related_name='post_likes', blank=True)
    comments_count = models.ManyToManyField('Comment', related_name='post_comments', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_on']

    def nummber_of_likes(self):
        return self.likes_count.count()

    def number_of_comments(self):
        return self.comments_count.count()


class Comment(models.Model):
    """
    This is a model to create a comment
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
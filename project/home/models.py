from django.db import models
from django.contrib.auth.models import User
# from cloudinary.models import CloudinaryField
from embed_video.fields import EmbedVideoField
from django_resized import ResizedImageField


# Create your models here.
class Post(models.Model):
    """
    This is a model to create a post
    """
    user = models.ForeignKey(User, related_name='post_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=300, unique=True, null=False, blank=False)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    image = ResizedImageField(
        default='default.jpg',
        upload_to='postImages/',
        null=True,
        quality=75,
        size=[400, None],
        blank=True)
    image_alt = models.CharField(max_length=200, null=True, blank=True)
    video = EmbedVideoField(max_length=500, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_on']

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """
    This is a model to create a comment
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

    def number_of_comments(self):
        return self.comments.count()


class Friends(models.Model):
    """
    Friends list
    """

    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    friend = models.ForeignKey(User, related_name='friend', on_delete=models.CASCADE)

    def __str__(self):
        return self.user

    class Meta:
        unique_together = ('user', 'friend')

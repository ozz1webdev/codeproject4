from django.db import models
from home.models import Post
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Comments(models.Model):
    """
    This is a model to create a comment
    """
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

    def number_of_comments(self):
        return self.comments.count()


@receiver(post_save, sender=User)
def create_comment(instance, created, **kwargs):
    """Create or update comment"""
    if created:
        Comments.objects.create(user=instance)

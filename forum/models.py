import os

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(default='pf_pics/default.png', upload_to='pf_pics', null=False, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    bio = models.TextField(max_length=150, null=True, blank=True)
    def __str__(self):
        return str(self.user.__str__())

    def get_absolute_url(self):
        return reverse('forum:browse_profile', args=[str(self.id)])


class Post(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    like_count = models.PositiveIntegerField(default=0)
    content = models.TextField()
    category = models.CharField(max_length=50, default='other', null=False, blank=True)
    icon = models.ImageField(upload_to='post_pics', null=True, blank=True)

    def delete(self, *args, **kwargs):
        for post_image in self.images.all():
            post_image.delete()

        if self.icon:
            if os.path.isfile(self.icon.path):
                os.remove(self.icon.path)

        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('forum:post_detail', args=[str(self.id)])


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    like_count = models.PositiveIntegerField(default=0)
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Komentár používateľa {self.user if self.user else 'Anonymous'} v {self.post.title}"


class PostLikedbyUser(models.Model):
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class PostImages(models.Model):
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_pics', blank=True, null=True)

    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)


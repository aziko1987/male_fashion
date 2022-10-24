from django.db import models
from ckeditor.fields import RichTextField
from users.models import UserModel


class BlogTagsModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'


class BlogModel(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField()
    main_image = models.ImageField(upload_to='blogs/')
    banner_image = models.ImageField(upload_to='blogs/')
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='blogs')
    tags = models.ManyToManyField(BlogTagsModel, related_name='blogs')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'
        ordering = ('-id',)


class CommentModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    comment = models.TextField()
    blog = models.ForeignKey(BlogModel, on_delete=models.RESTRICT, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.email}"

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

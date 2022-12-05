from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    comment = models.CharField(max_length=400)

    def __str__(self):
        return self.name


class Sharing(models.Model):
    title = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='media/')
    videofile = models.FileField(
        upload_to='videos/', null=True, verbose_name="")

    def __str__(self):
        return self.title

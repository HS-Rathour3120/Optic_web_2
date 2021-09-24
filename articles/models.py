from django.db import models


from django.conf import settings

from django.contrib.auth import get_user_model

from django.urls import reverse

from ckeditor.fields import RichTextField


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length= 500)
    # body = models.TextField()
    body = RichTextField(blank = True , null = True)
    date = models.DateTimeField(auto_now_add=True)


    img_field_name = models.ImageField(upload_to="images/", height_field=None, width_field=None, max_length=100, null = True , blank= True )

    file_field_name = models.FileField(upload_to="pdfs/", max_length=254, null= True, blank=True)

    author = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE,
    )


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail' , args = [str(self.id)])

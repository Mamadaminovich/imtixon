from django.db import models

class data(models.Model):
    title = models.CharField(db_column='title', max_length=100, blank=False)   
    author = models.CharField(db_column='author', max_length=100, blank=False)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(db_column='description', max_length=1000, blank=False)
    body = models.TextField(db_column='body', max_length=1000, blank=False)

    def __str__(self):
        return self.title  
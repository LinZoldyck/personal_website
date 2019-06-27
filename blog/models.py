from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField( max_length=250)
    age = models.DateField()
    def __str__(self):
        return '%s' % (self.name)

class Article(models.Model):
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    title = models.CharField(max_length = 255)
    pub_dat = models.DateField(auto_now = True)
    slug = models.SlugField(max_length = 50)
    content = models.TextField()
    summary = models.CharField( max_length = 300)
    published = models.BooleanField(default = True)






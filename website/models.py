from django.db import models
from django.core.files.storage import FileSystemStorage

fs=FileSystemStorage(location='/media')
# Create your models here.
class Formation(models.Model):
    name = models.CharField(max_length= 500)
    start_date = models.DecimalField(max_digits = 6, decimal_places=0)
    status = models.CharField(max_length= 8)
    school = models.CharField(max_length=500)
    photo = models.ImageField(upload_to="images/")

    def __str__(self):
        return '%s %s' % (self.name, self.school)



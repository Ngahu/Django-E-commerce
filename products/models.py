from django.db import models

# Create your models here.



class Product(models.Model):
    """
    """
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2,max_digits=20)
    image = models.FileField(upload_to='products/',blank=True, null=True)


    def __str__(self):
        return self.title
        
from django.db import models
# Create your models here.


class Product(models.Model):
    # category = models.ForeignKey(Category, related_name='product')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    charity = models.CharField(max_length=200, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    overview = models.TextField(blank=True)
    picture = models.ImageField(upload_to='product_image', blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    stock = models.DecimalField(max_digits=10, decimal_places=0)

    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

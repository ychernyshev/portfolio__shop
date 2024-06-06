from django.db import models


# Create your models here.
class ProductItemModel(models.Model):
    product_item_name = models.CharField(max_length=35, verbose_name='Name')
    product_item_slug = models.SlugField(max_length=35)
    product_item_cost = models.FloatField()
    product_item_description = models.TextField()
    product_item_image = models.ImageField(upload_to='products/product_item_images/',
                                           default='shop/images/default.jpg',
                                           blank=True, null=True)

    def __str__(self):
        return f'{self.product_item_name} - ${self.product_item_cost}'

    class Meta:
        ordering = ['-pk']
        verbose_name = 'name'
        verbose_name_plural = 'Names'

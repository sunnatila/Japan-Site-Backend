from django.db import models
from django.utils.translation import gettext_lazy as _

class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_('Description'))
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name=_('Price'))
    image = models.ImageField(upload_to='product_images/', null=True, blank=True, verbose_name=_('Image'))

    objects = models.Manager()


    def __str__(self):
        return f"{self.pk} - {self.title}"

    class Meta:
        verbose_name = _('Product ')
        verbose_name_plural = _('Products')
        db_table = 'products'



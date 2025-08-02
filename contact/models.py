from django.db import models
from django.utils.translation import gettext_lazy as _


class Contact(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    phone_number = models.CharField(verbose_name=_('Phone number'), max_length=20)
    message = models.TextField(verbose_name=_('Message'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    objects = models.Manager()

    def __str__(self):
        return f"{self.name} - {self.phone_number}"

    class Meta:
        verbose_name = _('Contact ')
        verbose_name_plural = _('Contacts')
        db_table = 'contacts'
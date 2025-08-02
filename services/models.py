from django.db import models
from django.utils.translation import gettext_lazy as _



class Service(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_('Description'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    objects = models.Manager()

    def __str__(self):
        return f"{self.pk} - {self.title}"

    class Meta:
        verbose_name = _('Service ')
        verbose_name_plural = _('Services')

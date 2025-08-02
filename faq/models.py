from django.db import models
from django.utils.translation import gettext_lazy as _


class FAQ(models.Model):
    question = models.CharField(max_length=255, verbose_name=_('Question'))
    answer = models.TextField(verbose_name=_('Answer'))

    objects = models.Manager()

    def __str__(self):
        return f"{self.question} - {self.answer[:30]}"

    class Meta:
        verbose_name = _('FAQ ')
        verbose_name_plural = _('FAQs')
        db_table = 'faqs'
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


class Video(models.Model):
    video_url = models.URLField(unique=True, null=True, blank=True, verbose_name=_('Video URL'))
    title = models.CharField(max_length=500, verbose_name=_('Title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    objects = models.Manager()

    class Meta:
        verbose_name = _('Video ')
        verbose_name_plural = _('Videos')
        db_table = 'videos'


    def clean(self):
        if not self.video_url:
            raise ValidationError(_('Please provide either a video URL.'))

        qs = Video.objects.all()
        if self.pk:
            qs = qs.exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError(_('Only one video instance is allowed.'))

    def save(self, *args, **kwargs):
        self.full_clean()
        if not self.pk:
            last = Video.objects.all().order_by('-pk').first()
            self.pk = 1 if not last else last.pk + 1
        super().save(*args, **kwargs)

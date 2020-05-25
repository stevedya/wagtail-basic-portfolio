from django.db import models

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting


@register_setting
class SocialMediaSettings(BaseSetting):

    social_media_header = models.CharField(max_length=255, default='Other ways to stalk me')
    github = models.URLField(
        blank=True,
        help_text='Enter your GitHub URL'
    )
    snapchat = models.URLField(
        blank=True,
        help_text='Enter your Snapchat URL'
    )
    instagram = models.URLField(
        blank=True,
        help_text='Enter a Instagram URL'
    )
    linkedin = models.URLField(
        blank=True,
        help_text='Enter a LinkedIn URL'
    )
    facebook = models.URLField(
        blank=True,
        help_text='Enter a Facebook URL'
    )

    panels = [
        FieldPanel("social_media_header"),
        FieldPanel("github"),
        FieldPanel("snapchat"),
        FieldPanel("instagram"),
        FieldPanel("linkedin"),
        FieldPanel("facebook"),
    ]

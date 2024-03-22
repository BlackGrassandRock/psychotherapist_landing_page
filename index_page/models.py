from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from datetime import timedelta


# date = now + 7 days at 18.00
def next_week_at_six_pm():
    return (timezone.now() + timedelta(weeks=1)).replace(hour=18, minute=0, second=0, microsecond=0)


class TimeStampedMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Title_and_Description(TimeStampedMixin):

    class TypeOfStatus(models.TextChoices):
        PUBLISH = "PB", _("Published")
        HIDE = "HD", _("Is hidden")

    title = models.CharField(_('title'), max_length=256)
    description = models.TextField(_('description'), blank=True)
    status = models.CharField(_('status'), choices=TypeOfStatus.choices, default=TypeOfStatus.PUBLISH)

    class Meta:
        abstract = True


class LinksandImages(models.Model):
    image = models.ImageField(_('image'), upload_to='', null=True)
    link = models.CharField(_('link'), max_length=2048)

    class Meta:
        abstract = True


class IndexContent(TimeStampedMixin):

    class TypeOfSectionName(models.TextChoices):
        COVER = "CV", _("Block Cover")
        PERFORMANCE = "PR", _("Block Performance")
        STATISTICS = "ST", _("Block Statistics")
        WORKING_APPROACH = "WA", _("Block Working Approach")
        LIST_SERVICES = "LS", _("Block List Of Services")
        DESCRIPTION = "DC", _("Block Description of the Client")
        QUESTIONS = "QS", _("Block Questions")
        CONTACTS = "CN", _("Block Contacts")
        NONE = "NN", _("------")

    title = models.CharField(_('title'), max_length=256, blank=True, null=True)
    section_title = models.CharField(_('Section title'), choices=TypeOfSectionName.choices, default=TypeOfSectionName.NONE)
    image = models.ImageField(upload_to='', blank=True, null=True)

    class Meta:
        db_table = "content\".\"index_content"
        verbose_name = _('Content')
        verbose_name_plural = _('Content')


class DopFieldsIndex(models.Model):
    subtitle = models.CharField(_('subtitle'), max_length=256, blank=True, null=True)
    description = models.TextField(_('description'), blank=True)
    index_content = models.ForeignKey(IndexContent, on_delete=models.CASCADE)
    class Meta:
        db_table = "content\".\"dop_fields_index"
        verbose_name_plural = _('Additional fields')


class Comments(Title_and_Description):
    image = models.ImageField(_('image'), upload_to='')
    class Meta:
        db_table = "content\".\"comments"
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')


class Events(Title_and_Description, LinksandImages):
    date_of_event = models.DateTimeField(default=next_week_at_six_pm)
    class Meta:
        db_table = "content\".\"events"
        verbose_name = _('Event')
        verbose_name_plural = _('Events')


class Services(Title_and_Description, LinksandImages):
    class Meta:
        db_table = "content\".\"services"
        verbose_name = _('Service')
        verbose_name_plural = _('Services')


class Posts(Title_and_Description):
    image = models.ImageField(_('image'), upload_to='', blank=True, null=True)
    class Meta:
        db_table = "content\".\"posts"
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')


class Subscribers(models.Model):
    mail = models.CharField(_('mail'), max_length=256, unique=True)
    class Meta:
        db_table = "content\".\"subscribers"
        verbose_name = _('Subscriber')
        verbose_name_plural = _('Subscribers')




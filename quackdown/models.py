from django.db import models
from django_countries import CountryField
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext
from quackdown import settings
from filebrowser.fields import FileBrowseField

from tagging.fields import TagField
from pubman.models import FurtherReading

class LookupModel(models.Model):

    title = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        abstract = True
        ordering = ['title',]

class ClaimantType(LookupModel):
    class Meta(LookupModel.Meta):
        verbose_name = _('claimant type')
        verbose_name_plural = _('claimant types')

class Brand(LookupModel):
    class Meta(LookupModel.Meta):
        verbose_name = _('brand')
        verbose_name_plural = _('brands')

class Forum(LookupModel):
    class Meta(LookupModel.Meta):
        verbose_name = _('forum')
        verbose_name_plural = _('forums')

class Methodology(LookupModel):
    class Meta(LookupModel.Meta):
        verbose_name = _('methodology')
        verbose_name_plural = _('methodologies')


class Frequency(LookupModel):
    class Meta(LookupModel.Meta):
        verbose_name = _('frequency')
        verbose_name_plural = _('frequencies')


class ClaimType(LookupModel):
    class Meta(LookupModel.Meta):
        verbose_name = _('claim type')
        verbose_name_plural = _('claim types')

class Condition(LookupModel):
    class Meta(LookupModel.Meta):
        verbose_name = _('condition')
        verbose_name_plural = _('conditions')

class Plausibility(LookupModel):
    class Meta(LookupModel.Meta):
        verbose_name = _('plausibility')
        verbose_name_plural = _('plausibility')


class ResponseType(LookupModel):
    class Meta(LookupModel.Meta):
        verbose_name = _('response type')
        verbose_name_plural = _('response types')




class Document(models.Model):
    name = models.CharField(max_length=200)
    #file = models.FileField(upload_to='quackfiles')
    file = FileBrowseField(max_length=300, directory="quackfiles/")


    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name',]

class Entity(models.Model):
    name = models.CharField(max_length=200, unique=True)
    date_added = models.DateTimeField(editable=False, auto_now_add=True)
    date_last_edited = models.DateTimeField(editable=False, auto_now=True)
    type = models.ForeignKey(ClaimantType)

    # Physical address
    physical_address = models.CharField(max_length=200, blank=True)
    physical_city = models.CharField(max_length=200, blank=True)
    physical_country = CountryField(blank=True)
    physical_code = models.CharField(max_length=12, blank=True)

    # Postal address
    postal_address = models.CharField(max_length=200, blank=True)
    postal_city = models.CharField(max_length=200, blank=True)
    postal_country = CountryField(blank=True)
    postal_code = models.CharField(max_length=12, blank=True)

    website = models.URLField(blank=True, verify_exists=False)

    slug = models.SlugField(unique=True)
    further_reading = models.ManyToManyField(FurtherReading, blank=True, null=True,
                                verbose_name=_('further reading'))
    notes = models.TextField(blank=True)

    tags = TagField(help_text=_('Comma separated list of tags. '
                                'E.g. "huge quack", international etc.'
                                'Each tag must start with a letter and can contain '
                                'letters, digits, spaces and underscores.'))


    def describe(self):
        if self.notes:
            return self.notes
        else:
            return ""


    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ['name',]

class Claimant(Entity):

    @models.permalink
    def get_absolute_url(self):
        return ('claimant_object_by_slug', (), {
            'slug': self.slug
        })


    class Meta(Entity.Meta):
        verbose_name = _('claimant')
        verbose_name_plural = _('claimants')


class Respondent(Entity):
    class Meta(Entity.Meta):
        verbose_name = _('respondent')
        verbose_name_plural = _('respondents')


class Response(models.Model):
    date_added = models.DateTimeField(editable=False, auto_now_add=True)
    date_last_edited = models.DateTimeField(editable=False, auto_now=True)
    responder = models.ForeignKey(Respondent)
    response_date = models.DateField()
    response_type = models.ForeignKey(ResponseType,
            help_text=_('E.g. "Complaint to ASASA"'))
    documents = models.ManyToManyField(Document, blank=True, null=True)
    short_description = models.CharField(blank=True, max_length=200,
                                         verbose_name=_('summary'))
    further_reading = models.ManyToManyField(FurtherReading, blank=True, null=True)
    notes = models.TextField(blank=True, verbose_name=_('description'))
    tags = TagField(help_text=_('Comma separated list of tags. '
                                'E.g. health, dangerous etc.'
                                'Each tag must start with a letter and can contain '
                                'letters, digits, spaces and underscores.'))

    def describe(self):
        if self.short_description:
            return self.short_description
        elif self.notes:
            return self.notes
        else:
            return ""


    def __unicode__(self):

        return ' '.join([ugettext(u'Response no '),
                         (unicode(self.id) + u':'),
                         unicode(self.responder),
                         unicode(self.response_type),
                         ugettext(u'on'),
                         unicode(self.response_date)])

    @models.permalink
    def get_absolute_url(self):
        return ('response_object', (), {
            'object_id': self.id
        })


    class Meta:
        ordering = ['-response_date',]
        verbose_name = _('response')
        verbose_name_plural = _('responses')


class Claim(models.Model):
    claimant = models.ForeignKey(Claimant)
    date_added = models.DateTimeField(editable=False, auto_now_add=True)
    date_last_edited = models.DateTimeField(editable=False, auto_now=True)
    forum = models.ForeignKey(Forum,
            help_text=_('Forum in which claim was made'))
    brand_name = models.ForeignKey(Brand, blank=True, null=True,
            help_text=_('Brand name of the product if it has one.'))
    methodology = models.ForeignKey(Methodology,
            help_text=_('E.g. electromagnetism, faith-healing, vitamins etc.'))
    claim_frequency = models.ForeignKey(Frequency,
            help_text=_('Frequency with which this claimant makes this claim'))
    claim_date = models.DateField()
    claim_type = models.ForeignKey(ClaimType,
            help_text=_('E.g. treat, cure, alleviate etc.'))
    condition = models.ForeignKey(Condition,
            help_text=_('E.g. AIDS, TB, diabetes etc.'))
    plausibility = models.ForeignKey(Plausibility,
            help_text=_('Indicate how plausible this claim is'))
    short_description = models.CharField(blank=True, max_length=200,
                                         verbose_name=_('summary'))
    responses = models.ManyToManyField(Response, blank=True, null=True,
                related_name='claims')
    documents = models.ManyToManyField(Document, blank=True, null=True)
    further_reading = models.ManyToManyField(FurtherReading, blank=True, null=True)
    notes = models.TextField(blank=True, verbose_name=_('description'))
    tags = TagField(help_text=_('Comma separated list of tags. '
                                'E.g. health, dangerous etc.'
                                'Each tag must start with a letter and can contain '
                                'letters, digits, spaces and underscores.'))

    def describe(self):
        if self.short_description:
            return self.short_description
        elif self.notes:
            return self.notes
        else:
            return ""

    def __unicode__(self):
        return ' '.join([ugettext(u'Claim no '),
                         (unicode(self.id) + u':'),
                         unicode(self.claimant),
                         unicode(self.claim_type),
                         unicode(self.condition),
                         ugettext(u'made on'),
                         unicode(self.claim_date),
                         u'-',
                         unicode(self.plausibility)])

    @models.permalink
    def get_absolute_url(self):
        return ('claim_object', (), {
            'object_id': self.id
        })

    class Meta:
        ordering = ['claimant',]
        verbose_name = _('claim')
        verbose_name_plural = _('claims')

class ClaimToInvestigate(models.Model):
    name = models.CharField(max_length=200,
        verbose_name=_('Your name'))
    email_address = models.EmailField(
        verbose_name=_('Your email address'),
        blank=True)
    telephone_number = models.CharField(max_length=12,
        blank=True,
        verbose_name=_('Phone number at which we can contact you'))

    date_added = models.DateTimeField(editable=False, auto_now_add=True)
    date_last_edited = models.DateTimeField(editable=False, auto_now=True)

    claimant = models.CharField(max_length=200,
        verbose_name =_('Name of person or organisation who made the '
                    'health care claim'))
    claim_date = models.DateField()
    forum = models.ForeignKey(Forum,
            blank=True,
            null=True,
            verbose_name =_('Forum in which the claim was made'))
    methodology = models.ForeignKey(Methodology,
            blank=True,
            null=True,
            help_text=_('E.g. electromagnetism, faith-healing, vitamins.'))
    claim_type = models.ForeignKey(ClaimType,
            blank=True,
            null=True,
            help_text=_('E.g. treat, cure, alleviate etc.'))
    condition = models.ForeignKey(Condition,
            blank=True,
            null=True,
            help_text=_('E.g. AIDS, TB, diabetes etc.'))
    plausibility = models.ForeignKey(Plausibility,
            blank=True,
            null=True,
            verbose_name=_('How plausible the claim is'))
    description = models.TextField(
            verbose_name='Short description of the claim')
    relevant_documents = models.FileField(null=True,
                                          blank=True,
            verbose_name=_('You may attach a relevant file, such as a scan of an advert'),
            help_text=_('If there is more than one file, use a zip file.'),
                      upload_to=settings.USER_CLAIM_FILES_FOLDER)

    def __unicode__(self):
        return ' '.join([(_(u'by') + u' ' + self.name),
                         (_(u'on') + u' ' + unicode(self.claim_date)),
                         (_(u'about') + u' ' + unicode(self.claimant))])

    class Meta:
        ordering = ['date_added']
        verbose_name = _('claim to investigate')
        verbose_name_plural = _('claims to investigate')


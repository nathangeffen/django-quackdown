from django.contrib import admin
from django.utils.translation import ugettext as _
from django import forms
 
from models import ClaimantType, Forum, Methodology, Frequency, ClaimType,\
    Condition, Plausibility, Respondent, ResponseType, Claimant,\
    Claim, Response, Document, ClaimToInvestigate, Brand 

claim_fieldsets = (
        (_('Claim details'), 
            {'classes' : ['collapse open',],
             'fields': ('claimant', 'brand_name', 
                        'forum', 'methodology', 
                        'claim_frequency', 'claim_date',
                        'claim_type' ,'condition',
                        'plausibility',),
            }        
        ),
        (_('Detailed Description'),
         {'classes' : ['collapse open',],
          'fields': ('short_description', 'notes','tags',),}
        ),
    )
    
response_fieldsets = (
        (None, 
            {'fields': ('responder', ('response_date', 
                                                'response_type'), 
                        ),}
        ),
        (_('Additional'),
         {'classes' : ['collapse',],
          'fields': ('short_description', 'further_reading', 'notes','documents', 'tags',),}
        ),
    )

class ResponseInline(admin.StackedInline):
    model = Response
    extra = 0
    fieldsets = response_fieldsets
    filter_horizontal = ['documents',]

class ClaimDocumentInline(admin.TabularInline):
    model = Claim.documents.through
    verbose_name = _('document')
    verbose_name_plural = _('documents')
    extra = 0
    raw_id_fields = ['document',]
    related_lookup_fields = {
        'fk': ['document',],
    }
    
    
class ClaimFurtherReadingInline(admin.TabularInline):
    model = Claim.further_reading.through
    verbose_name = _('further reading')
    verbose_name_plural = _('further readings')
    extra = 0
    raw_id_fields = ['furtherreading',]
    related_lookup_fields = {
        'fk': ['furtherreading',],
    }
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "furtherreading":
            kwargs["label"] = _("further reading")
        return super(ClaimFurtherReadingInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class ClaimResponseInline(admin.TabularInline):
    model = Claim.responses.through
    verbose_name = _('response')
    verbose_name_plural = _('responses')
    extra = 0
    raw_id_fields = ['response',]
    related_lookup_fields = {
        'fk': ['response',],
    }


class ClaimInline(admin.StackedInline):
    model = Claim
    extra = 0 
    fieldsets = claim_fieldsets
    filter_horizontal = ['responses', 'documents',]
 
class ClaimantAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'type', 'website', 'date_added', 'date_last_edited',]
    list_filter = ('type', 'tags',)
    search_fields = ('name',)
    save_on_top = True
    prepopulated_fields = {"slug": ("name",)}  
    inlines = [ClaimInline, ]
    filter_horizontal = ['further_reading',]

    fieldsets = (
        (None, 
            {'fields': ('name', 'type', 'website',),}
        ),
        (_('Addresses'),
            {'classes' : ['collapse',],
             'fields': (('physical_address','physical_city' ,'physical_country','physical_code'),
                     ('postal_address','postal_city','postal_country','postal_code'),),
            }
        ),
        (None,
         {'classes' : ['collapse',],
         'fields': ('further_reading', 'notes', 'slug','tags',),}
        ),
    )

class RespondentAdmin(ClaimantAdmin):
    inlines = [ResponseInline,]

class ClaimAdmin(admin.ModelAdmin):
    list_display = ['id', 'claimant', 'date_added', 'date_last_edited', 
                    'claim_date', 'claim_type', 'condition','plausibility',]
    list_editable = ['claim_type', 'condition','plausibility',]
    list_filter = ['claimant', 'claim_type','condition','plausibility' ]
    search_fields = ('claimant__name',)
    save_on_top = True
    fieldsets = claim_fieldsets
    filter_horizontal = ['responses', 'documents', 'further_reading',]    
    raw_id_fields = ['claimant', 'brand_name',]
    inlines = [ClaimResponseInline, ClaimDocumentInline, ClaimFurtherReadingInline,]
    related_lookup_fields = {
        'fk': ['claimant', 'brand_name',],
    }
    class Media:
        js = [
              'grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
              'grappelli/tinymce_setup/tinymce_setup.js',
             ]
    
    

class ResponseAdmin(admin.ModelAdmin):
    list_display = ['id', 'responder', 'response_type', 'date_added', 'date_last_edited', 'response_date'] 
    fieldsets = response_fieldsets
    filter_horizontal = ['documents', 'further_reading',]

class ClaimToInvestigateAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email_address', 'date_added', ]
    search_fields = ['name', 'email_address', 'claimant', ]
    list_filter = ['name', 'claimant']

class DocumentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'file']
    list_editable = ['name',]
    search_fields = ['name', 'file']

admin.site.register(Claimant, ClaimantAdmin)
admin.site.register(ClaimantType)
admin.site.register(Brand)
admin.site.register(Forum)
admin.site.register(Methodology)
admin.site.register(Frequency)
admin.site.register(ClaimType)
admin.site.register(Condition)
admin.site.register(Plausibility)
admin.site.register(Respondent, RespondentAdmin)
admin.site.register(ResponseType)
admin.site.register(Claim, ClaimAdmin)
admin.site.register(Response, ResponseAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(ClaimToInvestigate, ClaimToInvestigateAdmin)


from django.conf.urls.defaults import *
from django.views.generic import list_detail
from django.db.models import Count
from django.views.generic.simple import direct_to_template

from quackdown.views import list_claims, investigate_claim
from quackdown.models import Claim, Response, Claimant

claim_info = {
    "queryset" : Claim.objects.all(),
}

responses_info = {
    "queryset" : Response.objects.annotate(Count('claims')),
    "paginate_by" : 20,
}

response_info = {
    "queryset" : Response.objects.all(),
}

claimant_info = {
    "queryset" : Claimant.objects.all(),
}

urlpatterns = patterns('quackdown.views',
        (r'^claims/$', list_claims),
        url(r'^claims/(?P<object_id>[0-9]+)/$', list_detail.object_detail,claim_info, name="claim_object"),
        url(r'^claims/(?P<slug>[a-zA-Z0-9-_]+)/$',list_detail.object_detail,claim_info,name="claim_object_by_slug"),
        (r'^responses/$',list_detail.object_list, responses_info),
        url(r'^responses/(?P<object_id>[0-9]+)/$',list_detail.object_detail,response_info, name="response_object"),
        url(r'^responses/(?P<slug>[a-zA-Z0-9-_]+)/$',list_detail.object_detail,response_info, name="response_object_by_slug"),
        url(r'^claimants/(?P<object_id>[0-9]+)/$',list_detail.object_detail,claimant_info, name="claimant_object"),
        url(r'^claimants/(?P<slug>[a-zA-Z0-9-_]+)/$',list_detail.object_detail,claimant_info, name="claimant_object_by_slug"),
        (r'^investigate/$', investigate_claim),
        (r'^thanks/', direct_to_template, {'template': 'quackdown/thanks.html'}),
) 

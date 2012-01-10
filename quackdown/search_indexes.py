'''This module implements Haystack indices for searching.  

Search indices have been implemented for Article, MediaObject, Story and 
Copyright.
'''

import datetime
from haystack.indexes import *
from haystack import site
from quackdown.models import Claimant, Claim, Response

class ClaimIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    pub_date = DateTimeField(model_attr='claim_date')

    def get_queryset(self):
        """Used when the entire index for model is updated."""
        return Claim.objects.all()


site.register(Claim, ClaimIndex)

class ClaimantIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    pub_date = DateTimeField(model_attr='date_added')

    def get_queryset(self):
        """Used when the entire index for model is updated."""
        return Claimant.objects.all()


site.register(Claimant, ClaimantIndex)

class ResponseIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    pub_date = DateTimeField(model_attr='response_date')

    def get_queryset(self):
        """Used when the entire index for model is updated."""
        return Response.objects.all()


site.register(Response, ResponseIndex)



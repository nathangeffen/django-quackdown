from django.views.generic import list_detail
from django.db.models import Count
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.mail import mail_admins
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _

from quackdown.models import Claim
from quackdown.forms import ClaimToInvestigateForm

claims_info = {
    "paginate_by" : 20, 
}


def list_claims(request):
    
    ordering = request.GET.get('ord', 'claim_date')
    direction = request.GET.get('asc', 'd')
    
    if direction == 'a': # ascending order
        queryset = Claim.objects.annotate(Count('responses')).\
            order_by(ordering)
    else: # descending order
        queryset = Claim.objects.annotate(Count('responses')).\
            order_by("-" + ordering)
    
    return list_detail.object_list(
        request,
        queryset=queryset,
        paginate_by=20,
        extra_context = {"ordering" : ordering,
                         "direction" : direction}
    )


def investigate_claim(request):

    if request.method == 'POST':
        form = ClaimToInvestigateForm(request.POST, request.FILES) 
        if form.is_valid(): 
            claim_to_investigate = form.save()
            
            fields = filter(lambda x: x[0]!=None, [(form.fields[i].label, form.cleaned_data[i]) 
                      for i in form.fields])
            
            message = '\n'.join([unicode(i[0]) + u': ' + unicode(i[1]) for i in fields] +
                    ['URL: ', 'http://'+ request.META['SERVER_NAME'] + reverse('admin:quackdown_claimtoinvestigate_change',  
                                      args=[claim_to_investigate.id])]) 
                

            mail_admins(_('Claim to Investigate'), 
                message, 
                fail_silently=True)            
            return HttpResponseRedirect('/quackdown/thanks/') 
    else:
        form = ClaimToInvestigateForm() 

    return render_to_response('quackdown/claimtoinvestigate.html', {
        'form': form,
    }, context_instance=RequestContext(request))

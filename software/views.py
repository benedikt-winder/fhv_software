from models import *
from django.shortcuts import render_to_response
from django.template import RequestContext

def software_byname(request):
    print request.GET
    objects = Lector.objects.filter(username = 'bw')
    params = {
        'objects':objects
        }
        
    return render_to_response('software_byname.html', params, context_instance=RequestContext(request))
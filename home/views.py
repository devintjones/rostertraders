from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import logout as auth_logout


def index(request):
	return render_to_response('index.html', context_instance=RequestContext(request))


def logout(request):
        auth_logout(request)
        return HttpResponseRedirect('/')


def contact(request):
        return render_to_response('contact.html', context_instance=RequestContext(request))

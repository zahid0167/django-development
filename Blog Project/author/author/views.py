from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
def Index(request):
    return HttpResponseRedirect(reverse('App_author:blog_list'))
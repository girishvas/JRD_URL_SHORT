from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.template import loader
from django.views.generic import TemplateView, ListView, CreateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import urldetails
from .forms import urldetailsForm
from .documents import urldetailsDocument
import pdb
import random
import string
import json


class HomePage(TemplateView):
    template_name       = 'url/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, locals())


class UrlCreateView(LoginRequiredMixin,CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': urldetailsForm()}
        return render(request, 'url/action.html', context)

    def post(self, request, *args, **kwargs):
        username            = request.user.username
        url                 = request.POST.get("full_url")
        urlname             = request.POST.get("name")
        
        key                 = str(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6)))
        urlObj, created     = urldetails.objects.get_or_create(full_url=url, user__username=username)
        urlObj.key          = key
        urlObj.short_url    = request.META['HTTP_REFERER'].replace("create/", "") + key
        urlObj.name         = urlname
        urlObj.user         = User.objects.get(username=username)
        urlObj.save()

        data                = {}
        data["url"]         = urlObj.full_url
        data["name"]        = urlObj.name
        data["short_url"]   = urlObj.short_url

        print(data)

        return JsonResponse(data)
        return HttpResponse(json.dumps(data), content_type='application/json')


class UrlListView(LoginRequiredMixin,ListView):
    template_name               = "url/list.html"
    
    def get_queryset(self):
        search                  = urldetailsDocument.search().sort('-created_on')
        new_context             = search.filter('match', user__username=self.request.user.username)

        return new_context

    def post(self, request, *args, **kwargs):
        search                  = urldetailsDocument.search().sort('-created_on')
        object_list             = search.filter('match', user__username=self.request.user.username)
        try:
            q                   = request.POST['search']
            if not len(q) == 0:
                object_list     = object_list.query("multi_match", query=q, fields=['name', 'full_url', 'short_url'])
            else:
                pass
        except:
            pass
        
        try:
            sort                = request.POST['sort']
            if not len(sort) == 0:
                if sort == 'add_latest':
                    object_list = object_list.sort(
                        '-created_on',
                    )
                elif sort == 'add_old':
                    object_list = object_list.sort(
                        'created_on',
                    )
                elif sort == 'updated_latest':
                    object_list = object_list.sort(
                        '-updated_on',
                    )
                elif sort == 'updated_old':
                    object_list = object_list.sort(
                        'updated_on',
                    )
            else:
                pass
        except:
            pass

        return render(request, self.template_name, locals())
    

class ViewList(TemplateView):
    def get(self, request, slug, *args, **kwargs):
        try:
            urlObj              = urldetails.objects.get(key=slug)
            return redirect(urlObj.full_url)
        except:
            urlObj              = None
            return HttpResponseRedirect('/list/')
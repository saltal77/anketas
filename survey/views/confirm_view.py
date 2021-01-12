# -*- coding: utf-8 -*-

from django.views.generic import TemplateView, View
from django.shortcuts import get_object_or_404
from survey.forms import PinForm
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.views.decorators.csrf import csrf_exempt

from survey.models import Response, Answer


def my_handler404(request, exception):
    return render(request, 'survey/404.html', locals())


class ConfirmView(TemplateView):

    template_name = "survey/confirm.html"

    def get_context_data(self, **kwargs):
        context = super(ConfirmView, self).get_context_data(**kwargs)
        context["uuid"] = str(kwargs["uuid"])
        context["response"] = Response.objects.get(interview_uuid=context["uuid"])
        return context


class FoundView(TemplateView):

    template_name = "survey/get.html"

    def get_context_data(self, **kwargs):
        context = super(FoundView, self).get_context_data(**kwargs)
        context["pin"] = str(kwargs["pin"])
        resp = get_object_or_404(Response, pin=context["pin"])
        context["response"] = resp
        context["ans"] = Answer.objects.filter(response=resp)
        return context


class SearchView(View):
    form_class = PinForm
    initial = {'pin': ''}
    template_name = 'survey/find.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        res = []
        ans = []
        no_res = True
        form = self.form_class(request.POST)
        if form.is_valid():
            res = Response.objects.filter(pin=(request.POST['pin']).lower())
            if len(res):
                ans = Answer.objects.filter(response=res[0])
                res = res[0]
                no_res = None

        return render(request, self.template_name, {'form': form, 'res': res, 'ans': ans, 'no_res': no_res})
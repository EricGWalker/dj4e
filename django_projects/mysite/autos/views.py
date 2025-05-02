from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpRequest, HttpResponse

# from autos.models import Auto, Make
# from autos.forms import MakeForm

# Create your views here.

dummy_response = HttpResponse(b"This is a dummy response.")


class IndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "autos/index.html")


class Make_List(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return dummy_response


class Make_Create(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return dummy_response


class Make_Update(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return dummy_response


class Make_Delete(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return dummy_response


class Autos_List(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return dummy_response


class Autos_Create(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return dummy_response


class Autos_Update(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return dummy_response


class Autos_Delete(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return dummy_response

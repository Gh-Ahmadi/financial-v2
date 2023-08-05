from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from .models import Cut
from warehouse.models import *
from .forms import CutForm


class CutList(ListView):
    model = Cut
    queryset = Cut.objects.all().order_by('-date', '-code')
    template_name = "pages/workhouse/cut/list.html"
    context_object_name = "cuts"


# class CutDetail(DetailView):
#     model = Cut
#     queryset = Cut.objects.all()
#     template_name = "pages/workhouse/cut/detail.html"
#     context_object_name = "cut"
#     pk_url_kwarg = 'pk'


class CutCreate(CreateView):
    model = Cut
    template_name = 'pages/workhouse/cut/create.html'
    form_class = CutForm
    success_url = reverse_lazy("cut-list")


class CutUpdate(UpdateView):
    model = Cut
    form_class = CutForm
    template_name = "pages/workhouse/cut/update.html"
    success_url = reverse_lazy("cut-list")
    pk_url_kwarg = "pk"


def CutDetail(request,  slug):
    print(f"-----------------{slug}--------------")
    cut = Cut.objects.get(slug=slug)
    cloths = ClothRoll.objects.filter(cut_id=cut.pk)
    return render(request, "pages/workhouse/cut/detail.html", {'cut': cut, 'cloths': cloths})


def delete(request, id):
    obj = Cut.objects.get(id=id)
    obj.delete()
    return HttpResponseRedirect(reverse('cut-list'))

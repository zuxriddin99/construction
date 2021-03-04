from django.shortcuts import render
from .models import Yangilik

# Create your views here.
from django.views.generic import ListView, DetailView


def main_page(request):
    return render(request, 'index.html')


def test(request):
    return render(request, 'detail.html')


class YangiliklarJadvaliView(ListView):
    queryset = Yangilik.objects.all()
    context_object_name = 'yangiliklar'
    template_name = 'index.html'


class YangilikView(DetailView):
    queryset = Yangilik.objects.all()
    template_name = 'detail.html'

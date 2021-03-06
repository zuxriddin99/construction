from django.shortcuts import render
from .models import Yangilik, Xodim, BizningIshlarimiz, Korxona, Xabar
from construction.telegram_bot import send_message_via_bot
# Create your views here.
from django.views.generic import ListView, DetailView, CreateView


class BoshSaxifaView(ListView):
    queryset = Yangilik.objects.all()
    context_object_name = 'yangiliklar'
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['xodimlar'] = Xodim.objects.all()
        context['bizning_ishlar'] = BizningIshlarimiz.objects.all().order_by('-created_dt')
        context['korxona'] = Korxona.objects.all()
        return context


class YangilikView(DetailView):
    queryset = Yangilik.objects.all()
    template_name = 'detail_news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['yangiliklar'] = Yangilik.objects.all().exclude(id=self.kwargs['pk']).order_by('-created_dt')
        return context


class KorxonaView(DetailView):
    queryset = Korxona.objects.all()
    template_name = 'about_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['yangiliklar'] = Yangilik.objects.all().order_by('-created_dt')
        return context


class XabarView(CreateView):
    model = Xabar
    template_name = 'index.html'
    fields = ['name', 'phone', 'message']
    success_url = '/'

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        data = request.POST
        message = '<i>Sizga yangi mijoz xabar qoldirdi.</i>\n'
        message += 'Mijozning ismi:  <b>' + data['name'] + '</b>'
        message += '\nMijozning raqami:   <b>' + data['phone'] + '</b>'
        message += '\nXabar: \n <b>' + data['message'] + '</b>'
        send_message_via_bot(request, message)
        return super().post(request, *args, **kwargs)

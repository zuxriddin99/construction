from django.urls import path
from mainapp.views import BoshSaxifaView, YangilikView, KorxonaView, XabarView

urlpatterns = [
    path('', BoshSaxifaView.as_view(), name='yangiliklar'),
    path('yangilik/<int:pk>/', YangilikView.as_view(), name='yangilik'),
    path('korxona/<int:pk>/', KorxonaView.as_view(), name='korxona'),
    path('xabar/', XabarView.as_view(), name='xabar')
]

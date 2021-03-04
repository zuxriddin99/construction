from django.urls import path
from mainapp.views import YangiliklarJadvaliView, YangilikView, main_page, test

urlpatterns = [
    path('', YangiliklarJadvaliView.as_view(), name='yangiliklar'),
    path('yangilik/<int:pk>/', YangilikView.as_view(), name='yangilik')
]

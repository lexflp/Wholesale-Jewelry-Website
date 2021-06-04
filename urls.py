from django.urls import path

from . import views

app_name = 'jewelry'
urlpatterns = [
    path('', views.index, name='index'),
    path('inventory', views.inventory_view, name='inventory'),
    path('figaro', views.figaro_view, name='figaro'),
    path('quote', views.quote_view, name='quote'),
    path('thanks', views.thanks_view, name='thanks'),
    path('jewelry-multiple', views.jewelry_formset, name='jewelry-multiple'),
]

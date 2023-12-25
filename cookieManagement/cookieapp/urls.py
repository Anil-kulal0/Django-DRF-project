
from django.urls import path
from . import views

urlpatterns = [
    path('', views.visitcounter, name='counter'),
    path('persistent/', views.visitcounterpersistent, name='counter'),
    path('registeritem/', views.registeritem, name='counter'),
    path('showitems/', views.showitems, name='showitem'),

    path('page1/', views.page1, name='page1'),

    path('page2/', views.page2, name='page2'),
    path('page3/', views.page3, name='page3'),
    path('showdata/', views.showdata, name='showdata'),
 





]
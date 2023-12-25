
from django.urls import path
from . import views

urlpatterns = [
    path('', views.visitcounter, name='counter'),
    path('restart', views.restart, name='restart'),
    path('showsessionval', views.showsessionval, name='showsessionval'),
    

]
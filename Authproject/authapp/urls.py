from django.urls import path,include
from . import views


urlpatterns = [
    path('accounts/login/', include('django.contrib.auth.urls')),
    path('signup/', views.register, name='register'),

]

LOGIN_REDIRECT_URL = '/'
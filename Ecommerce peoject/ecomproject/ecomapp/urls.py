"""ecomproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . views import * 

app_name = 'ecomapp'
urlpatterns = [
      path('', Homeview.as_view(), name='home'),
      path('about/', Aboutview.as_view(), name='about'),
      path('contact/', contactview.as_view(), name='contact'),
      path('all_products/', All_productsview.as_view(), name='all_products'),
      path('product/<slug:slug>/',productdetailview.as_view(), name='product'),
      path('addtocart<int:pro_id>/',Addtocartview.as_view(), name='addtocart'),
      path('my_cart/',Mycartview.as_view(), name='mycart'),
      path('manage_cart/<int:cp_id>/',Managecartview.as_view(), name='managecart'),
      path('emptycart/',Emptycartview.as_view(), name='emptycart'),
      path('checkout/',Checkoutcartview.as_view(), name='checkout'),
      path('register/',customerregistrationview.as_view(), name='register'),
      path('logout/',customerlogoutview.as_view(), name='logout'),
      path('login/',customerloginview.as_view(), name='login'),
      path('profile/',customerprofileview.as_view(), name='profile'),
      path('profile/order/<int:pk>',customerorderdetailview.as_view(), name='customerorder'),
  
    
]
# from typing import Any, Dict
# from typing import Any, Dict
# from django import http
from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView,View, CreateView, FormView, DetailView
from django.contrib.auth import authenticate, login, logout
from .forms import checkoutForm, customerregistrationForm, customerloginForm
from .models import *
from django.urls import reverse_lazy
# Create your views here.

class Ecommixin(object):
      def dispatch(self, request, *args, **kwargs):
            cart_id = request.session.get('cart_id')
            if cart_id:
                  cart_obj = Cart.objects.get(id=cart_id)
                  if request.user.is_authenticated and hasattr(request.user,'customer'):
                        cart_obj.customer = request.user.customer
                        cart_obj.save()
            return super().dispatch(request, *args, **kwargs) 

class Homeview(Ecommixin, TemplateView):
      template_name = 'home.html'
      
      
      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['myname'] = 'Anil Kulal'
            context['product_list'] = Product.objects.all()
            return context
      
class All_productsview(Ecommixin, TemplateView):
      template_name = 'allproducts.html'
      
      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['allcategories'] = Category.objects.all()
            return context
      
class productdetailview(Ecommixin, TemplateView):
      template_name = 'productdetail.html'
      
      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            url_slug = self.kwargs['slug']
            product = Product.objects.get(slug=url_slug)
            product.view_count += 1
            product.save()
            context['product'] = product
            return context
      
class Addtocartview(Ecommixin, TemplateView):
      template_name = 'addtocart.html'
      
      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            # get product id from requested url
            product_id = self.kwargs['pro_id']
            # get product
            product_obj = Product.objects.get(id=product_id)
            # check if cart exists
            cart_id = self.request.session.get('cart_id', None)
            if cart_id:
                  cart_obj = Cart.objects.get(id=cart_id)
                  this_product_in_cart = cart_obj.cartproduct_set.filter(product=product_obj)
                  # print('old cart')
                  #item allready exists in cart
                  if this_product_in_cart.exists():
                        cartproduct = this_product_in_cart.last()
                        cartproduct.quantity +=1
                        cartproduct.subtotal += product_obj.selling_price
                        cartproduct.save()
                        cart_obj.total += product_obj.selling_price
                        cart_obj.save()
                  # new item added in cart
                  else:
                        cartproduct = Cartproduct.objects.create(cart=cart_obj, product=product_obj, rate=product_obj.selling_price, quantity=1, subtotal= product_obj.selling_price)
                        cart_obj.total += product_obj.selling_price
                        cart_obj.save()
                              
            else:
                  cart_obj = Cart.objects.create(total=0)
                  self.request.session['cart_id'] = cart_obj.id
                  cartproduct = Cartproduct.objects.create(cart=cart_obj, product=product_obj, rate=product_obj.selling_price, quantity=1, subtotal= product_obj.selling_price)
                  cart_obj.total += product_obj.selling_price
                  cart_obj.save()
                  # print('new cart')
                  
            # check if product already exists in cart
            return context
      
class Managecartview(Ecommixin, View):
      def get(self, request, *args, **kwargs):
            print('This is manage cart section')
            cp_id = self.kwargs['cp_id']
            action = request.GET.get('action')
            # print(cp_id, action)
            cp_obj = Cartproduct.objects.get(id=cp_id)
            cart_obj = cp_obj.cart
            
            if action =='inc':
                  cp_obj.quantity += 1
                  cp_obj.subtotal += cp_obj.rate
                  cp_obj.save()
                  cart_obj.total += cp_obj.rate
                  cart_obj.save()
                  
            elif action =='dcr':
                  cp_obj.quantity -= 1
                  cp_obj.subtotal -= cp_obj.rate
                  cp_obj.save()
                  cart_obj.total -= cp_obj.rate
                  cart_obj.save()
                  if cp_obj.quantity == 0:
                        cp_obj.delete()
            elif action =='rmv':
                  cart_obj.total -= cp_obj.subtotal
                  cart_obj.save()
                  cp_obj.delete()
            else:
                  pass
                  
            return redirect('ecomapp:mycart')
      
class Emptycartview(Ecommixin, View):
      def get(self, request, *args, **kwargs):
            cart_id = request.session.get('cart_id', None)
            if cart_id:
                  cart = Cart.objects.get(id=cart_id)
                  cart.cartproduct_set.all().delete()
                  cart.total = 0
                  cart.save()
            return redirect('ecomapp:mycart')
      
            
      
      
class Mycartview(Ecommixin, TemplateView):
      template_name = 'mycart.html'
      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            cart_id = self.request.session.get('cart_id', None)
            if cart_id:
                  cart = Cart.objects.get(id=cart_id)
            else:
                  cart = None
            context['cart'] = cart
            return context
      
class Checkoutcartview(Ecommixin, CreateView):
      template_name = 'checkout.html'
      form_class = checkoutForm
      success_url = reverse_lazy('ecomapp:home')
      
      # def dispatch(self, request, *args, **kwargs):
      #       if request.user.is_authenticated and request.user.customer:
                  
      #             pass
      #       else:
      #             return redirect ('/login/')
      #       return super().dispatch(request,  *args, **kwargs )
      def dispatch(self, request, *args, **kwargs):
            if request.user.is_authenticated and hasattr(request.user, 'customer'):
                  pass
            else:
                  return redirect('/login/?next=/checkout/')
            return super().dispatch(request, *args, **kwargs)
      
      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            cart_id = self.request.session.get('cart_id', None)
            if cart_id:
                  cart_obj = Cart.objects.get(id=cart_id)
            else:
                  cart_obj = None
            context['cart'] = cart_obj
            return context
      
      def form_valid(self, form):
            cart_id = self.request.session.get('cart_id')
            if cart_id:
                  cart_obj = Cart.objects.get(id=cart_id)
                  form.instance.cart = cart_obj
                  form.instance.subtotal = cart_obj.total
                  form.instance.discount = 0
                  form.instance.total = cart_obj.total
                  form.instance.order_status = cart_obj = 'Order Received'
                  del self.request.session['cart_id']
            else:
                  return redirect('ecomapp:home')
            return super().form_valid(form)
      
class customerregistrationview(CreateView):
      template_name = 'customerregistration.html'
      form_class = customerregistrationForm
      success_url = reverse_lazy('ecomapp:home')
      
      def form_valid(self, form):
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            user = User.objects.create_user(username, email, password)
            form.instance.user = user
            login(self.request, user)
            return super().form_valid(form)
      
      def get_success_url(self):
            if 'next' in self.request.GET:
                  next_url = self.request.GET.get('next')
                  # print(next_url)
                  return next_url
            else:
                  return self.success_url
            

class customerlogoutview(View):
      def get(self, request):
            logout(request)
            return redirect('ecomapp:home') 

class customerloginview(FormView):
      template_name = 'customerlogin.html'
      form_class = customerloginForm
      success_url = reverse_lazy('ecomapp:home')
      
      def form_valid(self, form):
            uname = form.cleaned_data.get('username')
            pword = form.cleaned_data['password']
            usr = authenticate(username=uname, password=pword)
            if usr is not None and usr.customer:
                  login(self.request,usr)
            else:
                  return render(self.request, self.template_name, {'form':self.form_class, 'error':'Invalid credentials'})
            return super().form_valid(form)
            
      def get_success_url(self):
            if 'next' in self.request.GET:
                  next_url = self.request.GET.get('next')
                  # print(next_url)
                  return next_url
            else:
                  return self.success_url
            
            
                  
            
               
class Aboutview(Ecommixin, TemplateView):
      template_name = 'about.html'
      
class contactview(Ecommixin, TemplateView):
      template_name = 'contact.html'
      
      
class customerprofileview(TemplateView):
      template_name = 'customer.html'
      
      def dispatch(self, request, *args, **kwargs):
            if request.user.is_authenticated and hasattr(request.user,'customer'):
                  pass
            else:
                  return redirect('/login/?next=/profile/')
            return super().dispatch(request, *args, **kwargs)
      
      
      def get_context_data(self, **kwargs):
            context=super().get_context_data(**kwargs)
            customer=self.request.user.customer
            context['customer']=customer
            orders=Order.objects.filter(cart__customer=customer)
            context['orders']=orders

            return context
                 
class customerorderdetailview(DetailView):
      template_name = 'customerorder.html'
      model = Order
      context_object_name = 'ord_obj'
      
      def dispatch(self, request, *args, **kwargs):
            if request.user.is_authenticated and hasattr(request.user, 'customer'):
                  pass
            else:
                  return redirect('/login/?next=/profile/')
            return super().dispatch(request, *args, **kwargs)
      

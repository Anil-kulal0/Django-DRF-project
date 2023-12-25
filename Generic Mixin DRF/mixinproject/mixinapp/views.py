from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics
from . models import Course, CourseSerializer
# Create your views here.

#MIXINS GENERICS 
# class courseListView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#       queryset = Course.objects.all()
#       serializer_class = CourseSerializer
      
#       def get(self, request):
#             return self.list(request)
      
#       def post(self, request):
#             return self.create(request)
      
# class courseDetailView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
#       queryset =  Course.objects.all()
#       serializer_class = CourseSerializer
      
#       def get(self, request, pk):
#             return self.retrieve(request, pk)
      
#       def put(self, request, pk):
#             return self.update(request, pk) 
      
#       def delete(self, request, pk):
#             return self.destroy(request, pk)

# SINGE GENERICS LISTVIEW 
# class courseListView(generics.ListAPIView, generics.CreateAPIView):
#       queryset = Course.objects.all()
#       serializer_class = CourseSerializer

# class courseDetailView(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
#       queryset = Course.objects.all()
#       serializer_class = CourseSerializer

# MIX GENERICS APIVIEW

class courseListView(generics.ListCreateAPIView):
      queryset = Course.objects.all()
      serializer_class = CourseSerializer

# class courseDetailView(generics.RetrieveUpdateAPIView):
#       queryset = Course.objects.all()
#       serializer_class = CourseSerializer

# class courseDetailView(generics.RetrieveDestroyAPIView):
#       queryset = Course.objects.all()
#       serializer_class = CourseSerializer

class courseDetailView(generics.RetrieveUpdateDestroyAPIView):
      queryset = Course.objects.all()
      serializer_class = CourseSerializer
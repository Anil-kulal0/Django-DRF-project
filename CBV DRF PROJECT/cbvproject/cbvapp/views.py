from django.shortcuts import render
from rest_framework.views import APIView
from .models import Course,CourseSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.
class CourseListView(APIView):
      def get(self, request):
            courses = Course.objects.all()
            courseSerializer = CourseSerializer(courses, many=True)
            return Response(courseSerializer.data)
      
      def post(self, request):
            courseSerializer = courseSerializer(data = request.data)
            if courseSerializer.is_valid():
                  courseSerializer.save()
                  return Response (courseSerializer.data)
            return Response(courseSerializer.errors)
            

class CourseDetailView(APIView):
      
      def get_course(self, pk):
            try:
                  return Course.objects.get(pk= pk)
            except Course.DoesNotExist:
                  raise Http404
            
      def get(self, request, pk):
            course = self.get_course(pk)
            serializer = CourseSerializer(course)
            return Response(serializer.data)
            
      
      def delete(self, request, pk):
            self.get_course(pk).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
            
            
      def put(self, request, pk):
            course = self.get_course(pk)
            courseSerializer = CourseSerializer(course, data=request.data)
            if courseSerializer.is_valid():
                  courseSerializer.save()
                  return Response(courseSerializer.data)
            return Response(courseSerializer.errors)
                  
from django.shortcuts import render
from rest_framework import viewsets
from .models import Company, Employee
from .serializers import CompanySerialzer, EmployeeSerializer


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

# Create your views here.

'''
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerialzer
    
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
'''
@api_view(['GET', 'POST'])
def company_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Company.objects.all()
        serializer = CompanySerialzer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CompanySerialzer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def employee_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Employee.objects.all()
        serializer = EmployeeSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def employee_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmployeeSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EmployeeSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        # status_msg = {"message":"Record Deleted Successfully."}
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
@api_view(['GET', 'PUT', 'DELETE'])
def company_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Company.objects.get(pk=pk)
    except Company.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer =CompanySerialzer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CompanySerialzer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        status_msg = {"message":"Record Deleted Successfully."}
        # return Response(status=status.HTTP_204_NO_CONTENT)    
        return Response(status_msg)    
    

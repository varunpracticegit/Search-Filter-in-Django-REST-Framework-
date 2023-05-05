from django.shortcuts import render
from .serializers import StudentSeriazer
from rest_framework.generics import ListAPIView
from .models import Student
from rest_framework.filters import SearchFilter

# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()        
    serializer_class = StudentSeriazer
    filter_backends = [SearchFilter]
    # search_fields = ['city']
    search_fields = ['^name']
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import mixins
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.views import APIView

from .models import Faculty
from .serializer import FacultySerializer

class FacultyListCreate(GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    queryset=Faculty.objects.all()
    serializer_class=FacultySerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class FacultyUpdate(RetrieveUpdateDestroyAPIView):
    queryset=Faculty.objects.all()
    serializer_class=FacultySerializer


def faculty(request):
    return HttpResponse(request.method)
# Create your views here.

#class StudentViewSet(ModelViewSet):

 #   queryset = Student.objects.all()

  #  serializer_class = StudentSerializer
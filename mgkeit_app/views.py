# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *
# Create your views here.

class PersonView(APIView):
    def get(self, request):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response({"users": serializer.data})

class TimetableView(APIView):
    def get(self, request):
        persons = Timetabels.objects.all()
        serializer = TimetableSerializer(persons, many=True)
        return Response({"timetable": serializer.data})
# from django.shortcuts import render
from django.db.models.expressions import F
from django.http.response import HttpResponse, HttpResponseNotFound, JsonResponse
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from .serializers import *
from .models import *
import json
from django.core import serializers
# Create your views here.


class PersonView(APIView):
    # permission_classes = (IsAuthenticated,)
    def get(self, request, pk=None):
        if pk is None:
            persons = Person.objects.all()
            serializer = PersonSerializer(persons, many=True)
            return Response({"users": serializer.data})
        else:
            serializer = PersonSerializer(Person.objects.get(user_id=pk))
            return Response({'user': serializer.data })

    def post(self, request):
        serializer = PersonSerializer(data=request.data.get('user'))
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
            return Response({"success": "Person '{}' created successfully".format(article_saved.user_id)})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        saved_article = Person.objects.get(user_id=pk)
        serializer = PersonSerializer(instance=saved_article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({
            "success": "Person '{}' updated successfully".format(article_saved.user_id)
        })

    def delete(self, request, pk):
        # Get object with this pk
        article = Person.objects.get(user_id=pk)
        article.delete()
        return Response({
            "message": "Person '{}' has been deleted.".format(pk)
        })
        
class TimetableView(APIView):
    def get(self, request, pk=None):
        if pk is None:
            # serializer = TimetableSerializer(Timetabels.objects.all(), many=True)
            data = serializers.serialize('json', Timetabels.objects.all())
            struct = json.loads(data)
            for obj in struct:
                timetable = obj['fields']['timetable'].split("\r\n")
                obj['fields']['timetable'] = timetable
            return JsonResponse({"res": struct})
        # else:
        #     r = pk.split("&")
        #     data = serializers.serialize('json', Timetabels.objects.all())
        #     struct = json.loads(data)
        #     for obj in struct:
        #         print(obj)
        #         day = obj['fields']['day_week']
        #         course = obj['fields']['course_id']
        #         odd = obj['fields']['is_odd']
        #         if day == int(r[0]) and course == int(r[1]) and odd == bool(r[2]):
        #             return JsonResponse({"res": obj})
        #         else:
        #             return HttpResponseNotFound()
# from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *
# Create your views here.


class PersonView(APIView):
    permission_classes = (IsAuthenticated,)
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
            serializer = TimetableSerializer(Timetabels.objects.all(), many=True)
            return Response({"timetables": serializer.data})
        # else:
        #     def destruct():
        #         args = pk.split('&')
        #         for el in args:
        #             i = el.split('=')
        #             if i == 'course':
        #                 pass
                # return ', '.join(args)

            # print(destruct())
            # serializer = TimetableSerializer()
            # return Response({'timetable': serializer.data })
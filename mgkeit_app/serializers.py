from rest_framework import serializers
from .models import *

class PersonSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    course_id = serializers.IntegerField()
    notify = serializers.BooleanField()

    def create(self, validated_data):
        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.course_id = validated_data.get('course_id', instance.course_id)
        instance.notify = validated_data.get('notify', instance.notify)
        instance.save()
        return instance

class TimetableSerializer(serializers.Serializer):
    course_id = serializers.IntegerField()
    day_week = serializers.IntegerField()
    timetable = serializers.CharField()
    is_odd = serializers.BooleanField()

    def create(self, validated_data):
        return Timetabels.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.course_id = validated_data.get('course_id', instance.course_id)
        instance.day_week = validated_data.get('day_week', instance.day_week)
        instance.timetable = validated_data.get('timetable', instance.timetable)
        instance.is_odd = validated_data.get('is_odd', instance.is_odd)
        instance.save()
        return instance
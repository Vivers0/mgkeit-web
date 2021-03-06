from rest_framework import serializers

class PersonSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    course_id = serializers.IntegerField()
    # build_id = serializers.ForeignKey('Build', on_delete=serializers.DO_NOTHING, verbose_name='Корпус')
    notify = serializers.BooleanField()

class TimetableSerializer(serializers.Serializer):
    course_id = serializers.IntegerField()
    day_week = serializers.IntegerField()
    timetable = serializers.CharField()
    is_odd = serializers.BooleanField()
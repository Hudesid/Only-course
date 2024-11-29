from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers, models

class InstructorAPIView(APIView):
    def get(self, request):
        instructors = models.Instructor.objects.all()
        serializer = serializers.InstructorSerializer(instructors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.InstructorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseAPIView(APIView):
    def get(self, request):
        courses = models.Course.objects.all()
        serializer = serializers.CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.CourseSerializer(data=request.data)
        if serializer.is_valid():
            teacher = request.data.get('teacher')
            teacher_instance = get_object_or_404(models.Instructor, name=teacher)
            serializer.save(teacher=teacher_instance)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LessonAPIView(APIView):
    def get(self, request):
        lessons = models.Lesson.objects.all()
        serializer = serializers.LessonSerializer(lessons, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.LessonSerializer(data=request.data)
        if serializer.is_valid():
            course = request.data.get('course')
            course_instance = get_object_or_404(models.Course, id=course)
            serializer.save(course=course_instance)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
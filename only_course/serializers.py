from rest_framework import serializers
from . import models

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Instructor
        fields = ('id', 'name', 'email', 'specialty')

    def validate_email(self, value):
        if models.Instructor.objects.filter(email=value).exists():
            raise serializers.ValidationError({"email" :'Bu email manzil allaqachon mavjud.'})
        return value

class CourseSerializer(serializers.ModelSerializer):
    teacher = InstructorSerializer(read_only=True)

    class Meta:
        model = models.Course
        fields = ('id', 'title', 'description', 'start_at', 'end_at', 'teacher')

    def validate(self, data):
        start_at = data.get('start_at')
        end_at = data.get('end_at')

        if start_at and end_at and start_at > end_at:
            raise serializers.ValidationError({
                'non_field_errors': "Kursning boshlanish sanasi tugash sanasidan oldin bo'lishi kerak.",
            })

        return data

class LessonSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)

    class Meta:
        model = models.Lesson
        fields = ('id', 'title', 'description', 'course', 'order')

    def validate_order(self, value):
        if value < 0 :
            raise serializers.ValidationError({"order" : "Tartib raqami musbat butun son bo'lishi kerak."})
        return value
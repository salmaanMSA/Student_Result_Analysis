
"""
    Imports..
"""
from .models import StudentsDetail, StudentsMark
from rest_framework import serializers

class StudentsDetail_Serializer(serializers.ModelSerializer):
    """
        Creating Student Detail Serializer
        Ref-Model : StudentsDetails
    """
    class Meta:
        model= StudentsDetail
        fields = '__all__'


class StudentsMark_Serializer(serializers.ModelSerializer):
    """
        Creating Student Mark Serializer
        Ref-Model : StudentsMark
    """
    class Meta:
        model = StudentsMark
        fields = '__all__'

    def to_representation(self, instance):
        """
            To get ForeignKey Field Name Instead of id
        """
        rep = super(StudentsMark_Serializer, self).to_representation(instance)
        rep['student'] = instance.student.name
        return rep




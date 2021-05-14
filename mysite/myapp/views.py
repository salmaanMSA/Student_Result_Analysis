"""
    Imports
"""
from .models import StudentsMark, StudentsDetail
from .serializer import StudentsDetail_Serializer, StudentsMark_Serializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.
# Task-1:-
class StudentDetails_ListCreateView(generics.ListCreateAPIView):
    """
        url : /api/student,
        Method : GET, POST
    """
    queryset = StudentsDetail.objects.all()
    serializer_class = StudentsDetail_Serializer

# Task-2:-
class StudentMark_ListCreateView(generics.ListCreateAPIView):
    """
        url : /api/student/add-mark,
        Method : GET, POST
    """
    queryset = StudentsMark.objects.all()
    serializer_class = StudentsMark_Serializer

# Task-3:-
class ResultsOnCategory(APIView):
    def get(self, request):
        """
            url : /api/students/results
            Method : GET
        """
        records = StudentsDetail.objects.all()
        total_no_of_students = len(records)

        grade_A = StudentsMark.objects.filter(mark__range=[91, 100])
        students_with_Grade_A = len(grade_A)
        grade_B = StudentsMark.objects.filter(mark__range=[81, 90])
        students_with_Grade_B = len(grade_B)
        grade_C = StudentsMark.objects.filter(mark__range=[71, 80])
        students_with_Grade_C = len(grade_C)
        grade_D = StudentsMark.objects.filter(mark__range=[61, 70])
        students_with_Grade_D = len(grade_D)
        grade_E = StudentsMark.objects.filter(mark__range=[55, 61])
        students_with_Grade_E = len(grade_E)
        grade_F = StudentsMark.objects.filter(mark__range=[0, 54])
        students_with_Grade_F = len(grade_F)

        distinction = round((students_with_Grade_A / total_no_of_students),3)

        firstClass = round(((students_with_Grade_B + students_with_Grade_C) / total_no_of_students),3)

        passClass = (total_no_of_students - students_with_Grade_F) / total_no_of_students

        response = {
            "Total_No_Of_Student": total_no_of_students,
            "Total_students_with_Grade-A": students_with_Grade_A,
            "Total_students_with_Grade-B": students_with_Grade_B,
            "Total_students_with_Grade-C": students_with_Grade_C,
            "Total_students_with_Grade-D": students_with_Grade_D,
            "Total_students_with_Grade-E": students_with_Grade_E,
            "Total_students_with_Grade-F": students_with_Grade_F,
            "Distinction % ": distinction,
            "First Class %": firstClass,
            "Pass Class %": passClass

        }

        return Response(response, status=status.HTTP_200_OK)








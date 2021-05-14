from django.db import models

# Create your models here.

class StudentsDetail(models.Model):
    """
        Student Detail Register Model
    """
    name = models.CharField(verbose_name="Name",max_length=55, null=False)
    roll_number = models.CharField(verbose_name="Roll-No",max_length=55, unique=True, null=False)
    dob = models.DateField(verbose_name="D.O.B",null=False)

    def __str__(self):
        return self.name

class StudentsMark(models.Model):
    """
        Student Mark Adding Model
    """
    student = models.ForeignKey(to=StudentsDetail, on_delete=models.CASCADE)
    mark = models.IntegerField(verbose_name="Mark",null=False)

    def __str__(self):
        return str(self.student)

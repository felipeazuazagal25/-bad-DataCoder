from django.db import models
from authentication.models import User


class Course(models.Model):
    shortname=models.CharField(max_length=8, unique=True)
    fullname=models.CharField(max_length=64, unique=True)
    semester=models.CharField(max_length=16)

    class Meta:
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.fullname
    
    

class Student(models.Model):
    userModel = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    course = models.ForeignKey(Course,verbose_name='Course', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Students'

    def __str__(self):
        return self.userModel.email

# arreglar esto para subir la rúbrica
class Test(models.Model):
    testName=models.SlugField(max_length=32, unique=True)
    rubric=models.FileField(default = None) # Zip File with all versions
    def __str__(self):
        return self.testName
    

class Question(models.Model):
    test = models.ForeignKey(Test, verbose_name='Test', on_delete = models.CASCADE)
    questionNumber=models.CharField(max_length=3)
    questionVersion=models.CharField(max_length=3)
    questionText=models.TextField()
    questionScore=models.DecimalField(max_digits=3,decimal_places=1)

    def __str__(self):
        return self.questionNumber + '-' + self.questionVersion

class QuestionRubric(models.Model):
    question = models.ForeignKey(Question, verbose_name = 'Question', on_delete = models.CASCADE)
    cellRow = models.CharField(max_length = 10)
    cellColumn = models.CharField(max_length = 10)
    cellFormula = models.CharField(max_length = 256)
    cellValue = models.CharField(max_length = 256)

    def __str__(self):
        return self.question.questionNumber + '-' + self.question.questionVersion + ' [' + str(self.cellRow) + ',' + str(self.cellColumn) + ']: ' + str(self.cellFormula) + ' --- ' + str(self.cellValue)


class TestDate(models.Model):
    test = models.ForeignKey(Test,verbose_name='Test',on_delete=models.CASCADE)
    course = models.ForeignKey(Course,verbose_name='Course',on_delete=models.CASCADE)
    testdate = models.DateTimeField()
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["test", "course"], name="all_keys_unique_together")
        ]


class StudentTest(models.Model):
    choices = (
      (1, 'No rendido'),
      (2, 'En curso'),
      (3, 'Por revisar'),
      (4, 'Revisado'),
    )
    student=models.ForeignKey(Student,verbose_name='Student',on_delete=models.CASCADE)
    test= models.ForeignKey(Test,verbose_name='Test',on_delete=models.CASCADE)
    code=models.SlugField(max_length=16)
    takeDateStart = models.DateTimeField(default = None, blank = True, null = True)
    takeDateEnd = models.DateTimeField(default = None, blank = True, null = True)
    status = models.PositiveSmallIntegerField(choices = choices,default = 1)
    grade = models.FloatField(null = True)
    excelFile = models.FileField(null = True)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["student", "test"], name="one_test_per_student")
        ]

class StudentTestQuestion(models.Model):
    studentTest = models.ForeignKey(StudentTest, verbose_name='Student Test',on_delete=models.CASCADE)
    questionTest = models.ForeignKey(Question,  verbose_name='Question Test',on_delete=models.CASCADE)
    scoreStudent = models.FloatField(null = True)
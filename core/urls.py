from django.urls import path, re_path
from . import views

app_name = 'core'

urlpatterns = [
    path('course_creation', views.course_creation_view, name='course_creation'),
    path('courses', views.courses_view, name='courses_view'),
    path('test_question_creation', views.test_creation_view,name='test_creation'),
    path('test_question_massive_creation', views.massive_test_question_creation_view, name = 'massive_test_question_creation'),
    path('tests', views.test_view, name='tests_view'),
    path('tests/<str:slug>',views.questions_view, name = 'questions_view'),
    path('delete_test/<str:testName>',views.delete_test, name = 'delete_test'),
    path('test_date_creation/',views.test_date_creation_view,name='test_date_creation'),
    path('student_creation', views.student_creation_view, name='student_creation'),
    path('send_email/<str:slug>', views.send_email, name='send_email'),

    # Views for the student
    path('tests_student/', views.tests_student_view, name='tests_student'),
    path('generate_test/<str:slug>',views.generate_test_view,name='generate_test'),
    path('generate_practice/<str>slug>',views.generate_practice,name='generate_practice'),
    path('request_code/<str:slug>',views.request_code, name = 'request_code'),

    # Views for the DEMO
    path('demo_contenidos/', views.demo_contenidos_view, name='demo_contenidos'),
]


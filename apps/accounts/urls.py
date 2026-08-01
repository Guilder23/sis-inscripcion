from django.urls import path
from .views import login_view, logout_view, dashboard, student_dashboard

urlpatterns = [
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('student-dashboard/', student_dashboard, name='student_dashboard'),
]

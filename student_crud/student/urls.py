from django.urls import path
from . import views

urlpatterns = [
    path('', views.student, name='student'),
    path('list/', views.all_student, name='list'),
    path('<int:sid>/', views.student, name='update'),
    path('delete/<int:sid>',views.delete,name='delete')



]

"""
URL configuration for check_task project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from django.conf.urls.static import static

from check_task import settings
from student.views import *
from task.views import *
from django.urls import include, path
from teacher.views import *


urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('login/',login_user.as_view(),name='login_user'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('add/',add),
    path('fill_storage/',fill_storage,name='fill_storage'),
    path('sent_neuro/', sent_neuro, name='sent_neuro'),

    path('new_topic/',new_topic, name= 'new_topic/'),


    path('get_subsection_for_topic/<int:topic_id>/', get_subsection_for_topic, name='get_subsection_for_topic'),

    path('add_request/',add_request, name= 'add_request/'),
    path('start_fon_task/',start_fon_task, name= 'start_fon_task/'),

    # для student
    path('home_student/',home_student,name='home_student'),
    path('home_student/task_view/<int:number>/', task_view, name='task_view'),

    # для teacher
    path('pivot_table_teacher/',pivot_table_teacher,name='pivot_table_teacher'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
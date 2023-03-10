"""Notepad URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from core.urlsApi import router
from core.apiViews import NoteListPriorityViewSet, NoteListScheduleViewSet, NoteListDelegateViewSet, NoteListEliminateViewSet, \
    AssignmentListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('fazer', NoteListPriorityViewSet.as_view()),
    path('agendar', NoteListScheduleViewSet.as_view()),
    path('delegar', NoteListDelegateViewSet.as_view()),
    path('eliminar', NoteListEliminateViewSet.as_view()),
    path('users/<int:user_id>/notas-atribuidas/', AssignmentListView.as_view()),

]

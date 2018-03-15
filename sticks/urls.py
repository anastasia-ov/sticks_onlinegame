"""sticks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from sticks_online.views import main_view, start_view, take_view, win_view, lose_view, bad_sticks_view, more_sticks_view, please_start

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view, name='main'),
    path('start/', start_view, name='start_game'),
    path('take/<int:sticks_taken>/', take_view, name='taken'),
    path('win/', win_view, name='win'),
    path('lose/', lose_view, name='lose'),
    path('bad_sticks/', bad_sticks_view, name='bad_sticks'),
    path('more_sticks/', more_sticks_view, name='more_sticks'),
    path('please_start/', please_start, name='please'),
]

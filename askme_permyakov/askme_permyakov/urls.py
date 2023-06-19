"""askme_permyakov URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from askme import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user-page/', views.user_page, name='user_page'),
    path('new-post/', views.create_post, name='create_post'),
    path('delete-post/', views.delete_post, name='delete_post'),
    path('delete-respond/', views.delete_respond, name='delete_respond'),
    path('login/', views.login_user, name='login'),
    path('signup/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('question/<str:current_id>/', views.question, name='question'),
    path('tag/<str:tag_id>/', views.post_with_tag, name='post_with_tag'),
    path('admin/', admin.site.urls),
]

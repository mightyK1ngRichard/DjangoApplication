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
from django.urls import path, include
from askme import views

urlpatterns = [
    path('', views.main, name='main'),
    path('index', views.index, name='index'),
    path('users/', views.users, name='users'),
    path('user-page/', views.user_page, name='user_page'),
    path('user/<int:user_id>', views.user_page_by_id, name='user_page_by_id'),
    path('new-post/', views.create_post, name='create_post'),
    path('delete-post/', views.delete_post, name='delete_post'),
    path('delete-respond/', views.delete_respond, name='delete_respond'),
    path('delete-answer/', views.delete_answer, name='delete_answer'),
    path('login/', views.login_user, name='login'),
    path('signup/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('question/<str:current_id>/', views.question, name='question'),
    path('tag/<str:tag_id>/', views.post_with_tag, name='post_with_tag'),
    path('admin/', admin.site.urls),
    path('likes/add', views.AddLikeView.as_view(), name='likes-add'),
    path('likes/remove', views.RemoveLikeView.as_view(), name='likes-remove'),
    path('likes/addAnswer', views.AddLikeAnswerView.as_view(), name='likes-add-answer'),
    path('likes/removeAnswer', views.RemoveLikeAnswerView.as_view(), name='likes-remove-answer'),
    path('likes/addAnswerToResponse', views.AddLikeAnswerToResponseView.as_view(), name='likes-add-answer_to_response'),
    path('likes/removeAnswerToResponse', views.RemoveLikeAnswerToResponseView.as_view(), name='likes-remove-answer_to_response'),
    path('update-post/<str:current_id>/', views.update_post, name='update_post'),
    path('delete-account/', views.delete_account, name='delete_account'),
    path('change_password/', views.change_password, name='change_password'),
]

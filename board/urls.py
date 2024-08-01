from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('login/', views.login, name='login'),
    path('signup/page', views.signup_page, name='signup_page'),
    path('signup/', views.signup, name='signup'),
    path('list/', views.index, name='index'),
    path('<int:board_id>/', views.detail, name='detail'),
    path('create/', views.create_board, name='create_board'),
    path('create/comment/<int:board_id>', views.create_comment, name='create_comment')
]

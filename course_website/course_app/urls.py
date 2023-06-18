from django.urls import path
from .import views
urlpatterns = [
    path('',views.user_signup,name='signup'),
    path('login',views.user_login,name='login'),
    path('index/',views.index,name='index'),
    path('course/create',views.course_create,name='short_course_add'),
    path('course/update/<int:pk>/', views.course_update, name='short_course_update'),
    path('course/delete/<int:pk>/', views.course_delete, name='short_course_delete'),
    path('course/list',views.course_list,name='short_course_list'),
    path('course/profile',views.change_password,name='change_password'),
    path('profile/', views.index, name='profile'),
    path('logout/',views.user_logout,name='logout'),
    
    

]


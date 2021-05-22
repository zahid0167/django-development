from django.urls import path
from .import views
 
app_name = 'App_author'



urlpatterns = [
    path('', views.Bloglist.as_view(), name='blog_list'),
    path('weite/', views.CreatBlog.as_view(), name='create_blog'),
    path('details/<slug>', views.blog_details, name='blog_details'),
    path('my_blog/', views.Myblog.as_view(), name='my_blog'),
    path('edit/<pk>', views.updateblog.as_view(), name='edit_blog'),
    
    ]

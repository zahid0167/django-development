from django.urls import path
from .import views


app_name = 'App_login'

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('signin/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('changeprofile/', views.user_change, name='user_change'),
    path('changepass/', views.pass_change, name='changepass'), 
    
    
]


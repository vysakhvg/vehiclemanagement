from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('login', views.login_pg, name='login'),
    path('loginout', views.logout_pg, name='logout'),
    path('addpg', views.add_vdetails, name='addpg'),
    path('vlistpg', views.view_vlist, name='view_vlist'),
    path('vdetailpg/<int:v_id>/', views.view_vdetails, name='view_vdetails'),
    path('editpg/<int:id>/', views.editpg, name='editpg'),
    path('deletepg/<int:id>/', views.deletepg, name='deletepg'),
]

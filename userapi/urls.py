from django.urls import path
from . import views

urlpatterns = [
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('create_medic', views.create_medic, name='create_medic'),
    path('<int:pk>/update_medic', views.update_medic, name='update_medic'),
    path('<int:pk>/delete-med', views.delete_product, name='delete-med'),
    path('list-med',views.listmed,name='list-med'),
    path('search',views.searchmed,name='search'),

]
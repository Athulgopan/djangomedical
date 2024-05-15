from django.urls import path
from . import views
urlpatterns = [
   path('v',views.product_create,name='createproduct'),
   path('',views.med_retrieve,name='retrieve'),
   path('update/<int:id>/',views.med_update,name='updateproduct'),
   path('delete/<int:id>',views.delete_med,name='deleteproduct'),
   path('list',views.list_med,name='list'),
  
    
] 
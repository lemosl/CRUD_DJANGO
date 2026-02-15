from django.urls import path 
from .import views 

urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
    # Mark as done 
    path('mask_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),

    # Mark as unfinished 
    path('mark_as_unfinished/<int:pk>/', views.mark_as_unfinished, name='mark_as_unfinished'),

    # edit task

    path('edit_task/<int:pk>/', views.edit_task, name = 'edit_task'),

    # delete task 
    path('delele_task/<int:pk>/', views.delete_task, name = 'delete_task'),

]
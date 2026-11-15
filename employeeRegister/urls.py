from django.urls import path
from . import views

urlpatterns = [
    # for get and post for insert request
    path('', views.employee_form, name='employee_insert'),
    # to get and retrieve and display  all records
    path('list/', views.employee_list, name='employee_list'),
    # get and post request for update operation
    path("<int:id>", views.employee_form,name='employee_update'),
    
    # delete a record
    path('delete/<int:id>/', views.employee_delete, name='employee_delete')
]
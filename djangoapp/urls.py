from django.urls import path
from .views import *

urlpatterns=[
    path('first/',first),
    path('second/',second),
    path('third/',third),
    path('register/',reg),
    path('login/',loginacc),
    path('index/',index),
    path('file_upload/',file_upload),
    path('employee/',emp),
    path('Search_Employee/',emp_search),
    path('product/',product_add),
    path('Search_Product/',product_search),
    path('Upload_files/',uploadfiles),
    path('Select_Checkbox/',select_checkbox),
    path('display/',display),
    path('display_emp/', display_emp),
    path('display_file/', display_file),
    path('display_allfiles/',display_allfiles),
    path('update/<int:id>',update_data),
    path('update_emp/<int:id>',update_emp),
    path('update_file/<int:id>',update_file),
    path('update_allfile/<int:id>',update_allfiles),
    path('delete/<int:id>',delete_data),
    path('delete_emp/<int:id>',delete_emp),
    path('delete_file/<int:id>',delete_file),
    path('delete_allfile/<int:id>',delete_allfiles),
    path('authuser/',userregistration),
    path('authuserlogin/',custom_login),
    path('classregister/',reg_classbase.as_view(),name='register'),
    path('classlogin/',login_classbase.as_view(),name='login'),
    path('todosmovie/',mytodos.as_view(),name='todo'),
    path('hotelapi/',hotelview.as_view(),name='hotel'),


]
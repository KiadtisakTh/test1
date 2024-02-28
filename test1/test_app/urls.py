from django.urls import path , include
from test_app.views import *


urlpatterns = [
    path("" ,index ,name='home'),
    path('search',search,name="search"),
    path("update/<int:id>/",update,name="update_item"),
    path("delete/<int:id>",delete_item,name="delete_item"),
]

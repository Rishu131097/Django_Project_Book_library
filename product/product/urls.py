from django.contrib import admin
from django.urls import path
from mainApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('add/',views.addRecord),
    path('delete/<int:id>/',views.deleteRecord),
    path('update/<int:id>/',views.updateRecord),
]

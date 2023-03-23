from django.urls import path
from . import views

app_name = 'learning_log_again'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
]
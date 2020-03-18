from django.urls import path, re_path
from . import views

app_name = 'user'

urlpatterns = [
    re_path(r'^$', views.store, name='user_store')
]

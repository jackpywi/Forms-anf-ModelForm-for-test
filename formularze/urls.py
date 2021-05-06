from django.urls import path
from . import views

app_name="formularze"

urlpatterns = [
    path('', views.contact),
    path('snippet', views.snippet_detail, name='snippet'),
]

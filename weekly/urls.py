from django.urls import path
from . import views

urlpatterns = [
    # Your URL patterns go here
    # Example: path('example/', views.example_view, name='example'),
    path("", views.index, name="index")
]

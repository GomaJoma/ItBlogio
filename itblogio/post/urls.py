from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.post_index, name="post_index"),
    path('<int:post_id>/', views.post_detail, name="post_detail"),
]

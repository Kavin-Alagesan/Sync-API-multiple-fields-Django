from django.urls import path
from api.views import BlogListCreateAPI,BlogListViewUpdateDelete

urlpatterns = [
    path('api/',BlogListCreateAPI.as_view()),
    path('api/<int:pk>/',BlogListViewUpdateDelete.as_view())
    ]

from rest_framework import generics
from api.models import Blogmodel
from api.serializers import BlogSerializer

class BlogListCreateAPI(generics.ListCreateAPIView):
    queryset=Blogmodel.objects.all()
    serializer_class=BlogSerializer

class BlogListViewUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset=Blogmodel.objects.all()
    serializer_class=BlogSerializer

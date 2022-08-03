from rest_framework import viewsets
from .serializers import CategorySerializer
from .models import Category

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().filter(deleted_at=None).order_by('name')
    serializer_class = CategorySerializer
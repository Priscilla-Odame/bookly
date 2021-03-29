from app.submodels.category import Category
from app.serializers.category import CategorySerializer
from rest_framework import viewsets


class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    filterset_fields = ['name', 'books']
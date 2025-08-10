from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Item
from .serializers import ItemSerializer

class ItemListCreateView(generics.ListCreateAPIView):
    """
    API view to retrieve list of items or create a new one.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
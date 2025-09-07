from rest_framework import viewsets
from .models import Listing
from .serializers import ListingSerializer
from .tasks import notify_new_listing
class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all().order_by('-created_at')
    serializer_class = ListingSerializer
    def perform_create(self, serializer):
        instance = serializer.save()
        notify_new_listing.delay(instance.id)

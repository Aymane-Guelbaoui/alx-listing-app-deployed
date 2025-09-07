from celery import shared_task
from time import sleep
from .models import Listing
@shared_task
def notify_new_listing(listing_id):
    try:
        listing = Listing.objects.get(id=listing_id)
        sleep(1)
        return f'Notified about listing {listing.title} ({listing.id})'
    except Listing.DoesNotExist:
        return 'Listing not found'

from django.db.models import Count, F
from spaces.models import Space
from bookings.models import Booking

def get_occupancy_stats():
    return Space.objects.annotate(
        total_seats=F('capacity'),
        occupied_seats=Count('bookings', filter=Q(bookings__status='active')),
        vacancy=F('capacity') - Count('bookings', filter=Q(bookings__status='active'))
    ).values('id', 'name', 'district', 'total_seats', 'occupied_seats', 'vacancy')
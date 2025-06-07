from django.urls import path
from .views import FitnessClassList, BookClass, BookingList

urlpatterns = [
    path('classes/', FitnessClassList.as_view(), name='fitnessclass-list'),
    path('book/', BookClass.as_view(), name='book-class'),
    path('bookings/', BookingList.as_view(), name='booking-list')
]
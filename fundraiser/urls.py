from django.urls import path
from .views import EventListCreateView, EventDetailView, DonationCreateView

urlpatterns = [
    path('events/', EventListCreateView.as_view(), name='event-list'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('donate/', DonationCreateView.as_view(), name='donate'),
]

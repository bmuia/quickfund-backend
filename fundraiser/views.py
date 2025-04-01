from rest_framework import generics,status
from .models import Event, Donation
from .serializers import EventSerializer, DonationSerializer
from rest_framework.response import Response
from decimal import Decimal

class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetailView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class DonationCreateView(generics.CreateAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer

    def create(self, request, *args, **kwargs):
        event_id = request.data.get("event")
        amount = Decimal(request.data.get("amount"))  # Convert to Decimal

        try:
            event = Event.objects.get(id=event_id)

            # Ensure donation doesn't exceed goal
            if event.amount_raised + amount > event.goal_amount:
                return Response({"error": "Donation exceeds goal amount"}, status=status.HTTP_400_BAD_REQUEST)

            # Save donation
            donation = Donation.objects.create(
                event=event,
                donor_name=request.data.get("donor_name"),
                amount=amount
            )

            # Update event amount_raised
            event.amount_raised += amount
            event.save()

            return Response(DonationSerializer(donation).data, status=status.HTTP_201_CREATED)

        except Event.DoesNotExist:
            return Response({"error": "Event not found"}, status=status.HTTP_404_NOT_FOUND)
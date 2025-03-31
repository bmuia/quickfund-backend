from django.core.management.base import BaseCommand
from faker import Faker
from fundraiser.models import Event, Donation
import random

class Command(BaseCommand):
    help = 'Generate fake data for events and donations'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Generate 50 events
        for _ in range(50):
            event = Event.objects.create(
                title=fake.company(),
                description=fake.text(),
                goal_amount=random.randint(1000, 5000),
                amount_raised=random.randint(0, 1000),
            )
            self.stdout.write(self.style.SUCCESS(f'Created event: {event.title}'))

            # Generate 50 donations for each event
            for _ in range(50):
                Donation.objects.create(
                    event=event,
                    donor_name=fake.name(),
                    amount=random.randint(10, 500),
                )
                self.stdout.write(self.style.SUCCESS(f'Created donation for event: {event.title}'))

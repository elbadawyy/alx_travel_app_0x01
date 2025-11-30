from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth.models import User
import random


class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        # Create dummy user if not exists
        if not User.objects.filter(username='demo').exists():
            User.objects.create_user(username='demo', password='password123')

        user = User.objects.get(username='demo')

        sample_listings = [
            {
                'title': 'Beach House',
                'description': 'A beautiful house by the ocean.',
                'price_per_night': 120.00,
                'location': 'Miami'
            },
            {
                'title': 'Mountain Cabin',
                'description': 'Cozy cabin in the mountains.',
                'price_per_night': 80.00,
                'location': 'Denver'
            },
            {
                'title': 'City Apartment',
                'description': 'Modern apartment in the city center.',
                'price_per_night': 150.00,
                'location': 'New York'
            }
        ]

        for data in sample_listings:
            listing, created = Listing.objects.get_or_create(**data)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created listing: {listing.title}"))
            else:
                self.stdout.write(self.style.WARNING(f"Listing already exists: {listing.title}"))

        self.stdout.write(self.style.SUCCESS("Seeding completed successfully."))

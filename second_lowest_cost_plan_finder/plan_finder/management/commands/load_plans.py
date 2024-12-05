import csv
from django.core.management.base import BaseCommand
from plan_finder.models import Plan
from plan_finder.constants import PlanCsvLocation


class Command(BaseCommand):
    help = "Import plans from a CSV file"

    def add_arguments(self, parser):
        parser.add_argument(
            "csv_file",
            type=str,
            help="The path to the CSV file with plan data.",
            default=PlanCsvLocation.DEFAULT,
            nargs="?",
        )

    def handle(self, *args, **kwargs):
        csv_file = kwargs["csv_file"]

        with open(csv_file, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            if Plan.objects.exists():
                self.stdout.write(
                    self.style.WARNING("Wiping table before populating again...")
                )
                Plan.objects.all().delete()
            for row in reader:
                Plan.objects.create(
                    plan_id=row["plan_id"],
                    state=row["state"],
                    metal_level=row["metal_level"],
                    rate=row["rate"],
                    rate_area=row["rate_area"],
                )
        self.stdout.write(self.style.SUCCESS("Plans imported successfully!"))

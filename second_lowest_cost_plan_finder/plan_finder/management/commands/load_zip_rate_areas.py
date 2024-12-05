import csv
from django.core.management.base import BaseCommand
from plan_finder.models import ZipRateArea
from plan_finder.constants import ZipRateAreaCsvLocation


class Command(BaseCommand):
    help = "Import zip/rate areas from a CSV file"

    def add_arguments(self, parser):
        parser.add_argument(
            "csv_file",
            type=str,
            help="The path to the CSV file with zip/rate data.",
            default=ZipRateAreaCsvLocation.DEFAULT,
            nargs="?",
        )

    def handle(self, *args, **kwargs):
        csv_file = kwargs["csv_file"]

        with open(csv_file, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            if ZipRateArea.objects.exists():
                self.stdout.write(
                    self.style.WARNING("Wiping table before populating again...")
                )
                ZipRateArea.objects.all().delete()
            self.stdout.write(
                self.style.SUCCESS(
                    "Seeding database with Zip and Rate Area data - this will take a minute."
                )
            )
            for row in reader:
                ZipRateArea.objects.create(
                    zipcode=row["zipcode"],
                    state=row["state"],
                    county_code=row["county_code"],
                    county_name=row["name"],
                    rate_area=row["rate_area"],
                )
        self.stdout.write(self.style.SUCCESS("Zip/Rate Areas imported successfully!"))

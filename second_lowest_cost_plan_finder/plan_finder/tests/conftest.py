import csv
import pytest

from plan_finder.constants import (
    PlanCsvLocation,
    ZipRateAreaCsvLocation,
)
from plan_finder.models import Plan, ZipRateArea


@pytest.fixture
def populate_plans():
    with open(PlanCsvLocation.TEST, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            Plan.objects.create(
                plan_id=row["plan_id"],
                state=row["state"],
                metal_level=row["metal_level"],
                rate=row["rate"],
                rate_area=row["rate_area"],
            )
        file.close()


@pytest.fixture
def populate_zips():
    with open(ZipRateAreaCsvLocation.TEST, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            ZipRateArea.objects.create(
                zipcode=row["zipcode"],
                state=row["state"],
                county_code=row["county_code"],
                county_name=row["name"],
                rate_area=row["rate_area"],
            )
        file.close()

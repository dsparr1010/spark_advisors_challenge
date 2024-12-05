from decimal import Decimal
from typing import List
from django.core.validators import MinValueValidator
from django.db import models

from plan_finder.constants import MetalLevel


class PlanManager(models.Manager):

    def filter_by_state_rate_level(
        self,
        state: str,
        rate_area: int,
        metal_level: str = MetalLevel.SILVER,
    ) -> List[Decimal]:
        if found_plans := self.filter(
            state=state,
            metal_level=metal_level,
            rate_area=rate_area,
        ):
            if found_plans.count() > 1:
                return [plan.rate for plan in found_plans]

        # Cannot find rates or only one exists
        return ""


class Plan(models.Model):
    plan_id = models.CharField(unique=True, max_length=50)
    state = models.CharField(max_length=2)
    metal_level = models.CharField(max_length=15)
    rate = models.DecimalField(
        max_digits=6, decimal_places=2, validators=[MinValueValidator(0.01)]
    )
    rate_area = models.PositiveSmallIntegerField()

    objects = PlanManager()


class ZipRateAreaManager(models.Manager):

    def filter_by_zip_and_check_for_validity(self, zipcode: str):
        zip_rate_qs = ZipRateArea.objects.filter(zipcode=zipcode)
        if not zip_rate_qs.exists():
            return ""  # Zip info not found

        # Ambiguity checks

        state_values_are_different = (
            zip_rate_qs.values("state").distinct().count() > 1
        )  # Cannot infer if zipcode belongs to different states
        rate_area_values_are_different = (
            zip_rate_qs.values("rate_area").distinct().count() > 1
        )  # Cannot infer if the state is the same, but multiple rate_areas are returned
        if state_values_are_different or rate_area_values_are_different:
            return ""

        return zip_rate_qs.first()


class ZipRateArea(models.Model):
    zipcode = models.PositiveIntegerField()
    state = models.CharField(max_length=2)
    county_code = models.PositiveIntegerField()
    county_name = models.CharField(max_length=30)
    rate_area = models.PositiveSmallIntegerField()

    objects = ZipRateAreaManager()

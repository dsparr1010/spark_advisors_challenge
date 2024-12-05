import pytest

from plan_finder.models import Plan, ZipRateArea
from plan_finder.constants import MetalLevel


class TestPlan:

    @pytest.mark.django_db
    @pytest.mark.parametrize(
        "state,rate_area,metal_level,numb_result_expected",
        (
            ("MO", 6, MetalLevel.SILVER, 2),
            ("MO", 6, MetalLevel.GOLD, 0),
            ("MS", 2, MetalLevel.SILVER, 10),
            ("IA", 7, MetalLevel.SILVER, 0),
            ("FL", 3, MetalLevel.SILVER, 0),
        ),
    )
    def test_filter_by_state_rate_level(
        self, state, rate_area, metal_level, numb_result_expected, populate_plans
    ):

        result = Plan.objects.filter_by_state_rate_level(
            state=state, rate_area=rate_area, metal_level=metal_level
        )
        assert len(result) == numb_result_expected


class TestZipRateArea:

    @pytest.mark.django_db
    def test_filter_by_zip_and_check_for_validity_returns_correct_instance(
        self, populate_zips
    ):
        result = ZipRateArea.objects.filter_by_zip_and_check_for_validity(zipcode=77586)
        assert result.state == "TX"
        assert result.rate_area == 10

    @pytest.mark.django_db
    def test_filter_by_zip_and_check_for_validity_one_zip_for_state_with_different_rate_areas(
        self, populate_zips
    ):
        result = ZipRateArea.objects.filter_by_zip_and_check_for_validity(zipcode=63359)
        assert result == ""

    @pytest.mark.django_db
    def test_filter_by_zip_and_check_for_validity_returns_correct_instance_when_rateareas_are_same_for_state(
        self, populate_zips
    ):
        result = ZipRateArea.objects.filter_by_zip_and_check_for_validity(zipcode=52654)
        assert result.state == "IA"
        assert result.rate_area == 5

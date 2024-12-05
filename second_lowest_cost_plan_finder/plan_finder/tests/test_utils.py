import pytest
from decimal import Decimal

from plan_finder.constants import (
    ZipsToFindSecondLowestCostLocation,
)
from plan_finder.utils import (
    aggregate_second_lowest_cost_silver_plans_by_csv,
    aggregate_zips_from_csv,
    find_second_lowest_cost,
)


class TestUtils:
    def test_find_second_lowest_cost(self):
        rates = [
            Decimal("414.84"),
            Decimal("293.11"),
            Decimal("398.47"),
            Decimal("393.26"),
            Decimal("393.65"),
            Decimal("306.56"),
            Decimal("418.38"),
            Decimal("409.09"),
        ]
        assert find_second_lowest_cost(rates) == Decimal("306.56")

    def test_aggregate_zips_from_csv(self):
        rows = aggregate_zips_from_csv(filename=ZipsToFindSecondLowestCostLocation.TEST)
        assert len(rows) == 6
        assert rows[0][0] == "64148"
        assert rows[0][1] == ""
        assert rows[2][0] == "77586"
        assert rows[2][1] == ""

    @pytest.mark.django_db
    def test_aggregate_second_lowest_cost_silver_plans_by_csv(
        self, populate_plans, populate_zips
    ):
        zips_list = aggregate_zips_from_csv(
            filename=ZipsToFindSecondLowestCostLocation.TEST
        )
        result = aggregate_second_lowest_cost_silver_plans_by_csv(csv_data=zips_list)
        assert result[0] == ("64148", "")
        assert result[2] == ("77586", "243.72")

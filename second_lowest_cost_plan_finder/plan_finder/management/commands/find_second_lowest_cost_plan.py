from django.core.management.base import BaseCommand
from plan_finder.constants import (
    ZipsToFindSecondLowestCostLocation,
)
from plan_finder.utils import (
    aggregate_second_lowest_cost_silver_plans_by_csv,
    aggregate_zips_from_csv,
    write_file_data_to_terminal,
    write_zip_and_rate_to_csv,
)


class Command(BaseCommand):
    help = "Import zip/rate areas from a CSV file"

    def add_arguments(self, parser):
        parser.add_argument(
            "csv_file",
            help="The path to the CSV file with zips to find the second lowest cost plan.",
            type=str,
            default=ZipsToFindSecondLowestCostLocation.DEFAULT,
            nargs="?",
        )

    def handle(self, *args, **kwargs):
        csv_file = kwargs["csv_file"]
        csv_data = aggregate_zips_from_csv(csv_file)
        rows_to_write = aggregate_second_lowest_cost_silver_plans_by_csv(
            csv_data=csv_data
        )

        write_zip_and_rate_to_csv(csv_file=csv_file, data=rows_to_write)
        write_file_data_to_terminal(csv_file=csv_file)

import csv
from django.core.management.base import BaseCommand

from plan_finder.management.commands.find_second_lowest_cost_plan import (
    ZipsToFindSecondLowestCostLocation,
)
from plan_finder.constants import CsvHeaders


zips = (
    64148,
    67118,
    40813,
    18229,
    51012,
    79168,
    54923,
    67651,
    49448,
    27702,
    47387,
    50014,
    33608,
    "06239",
    54919,
    46706,
    14846,
    48872,
    43343,
    77052,
    "07734",
    95327,
    12961,
    26716,
    48435,
    53181,
    52654,
    58703,
    91945,
    52146,
    56097,
    21777,
    42330,
    38849,
    77586,
    39745,
    "03299",
    63359,
    60094,
    15935,
    39845,
    48418,
    28411,
    37333,
    75939,
    "07184",
    86313,
    61232,
    20047,
    47452,
    31551,
)


class Command(BaseCommand):
    help = "For testing purposes, generates a new slcsp.csv without rates populated"

    def handle(self, *args, **kwargs):
        with open(
            ZipsToFindSecondLowestCostLocation.DEFAULT,
            mode="w+",
            newline="",
            encoding="utf-8",
        ) as file:
            writer = csv.writer(file)
            # Write header
            writer.writerow([CsvHeaders.ZIP_RATE[0], CsvHeaders.ZIP_RATE[1]])
            for zip in zips:
                writer.writerow([zip, ""])

            file.close()

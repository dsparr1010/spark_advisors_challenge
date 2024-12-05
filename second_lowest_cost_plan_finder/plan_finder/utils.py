import csv
from decimal import Decimal
import sys
from typing import List

from plan_finder.constants import (
    CsvHeaders,
    MetalLevel,
    ZipsToFindSecondLowestCostLocation,
)
from plan_finder.models import Plan, ZipRateArea


def find_second_lowest_cost(rates_list: List[Decimal]) -> Decimal:
    """Given a list of rates, determines which value is the second lowest"""

    second_lowest = max(rates_list)
    lowest = min(rates_list)
    for rate in rates_list:
        if rate == lowest:  # skip multiple instance of the lowest number
            continue
        elif rate < second_lowest:
            second_lowest = rate
    return second_lowest


def aggregate_zips_from_csv(
    filename: str = ZipsToFindSecondLowestCostLocation.DEFAULT,
) -> List[str]:
    """Opens a csv file and converts rows into a series of lists"""
    with open(filename, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Skipping CSV header
        return list(reader)


def aggregate_second_lowest_cost_silver_plans_by_csv(csv_data: List[str]) -> List[str]:
    """Finds Plan instances that are valid for a given zipcode"""
    zip_and_rate_list = []
    for row in csv_data:
        zipcode_to_find = row[0]
        rate = ""
        if zip_rate := ZipRateArea.objects.filter_by_zip_and_check_for_validity(
            zipcode=zipcode_to_find
        ):
            if rates := Plan.objects.filter_by_state_rate_level(
                state=zip_rate.state,
                metal_level=MetalLevel.SILVER,
                rate_area=zip_rate.rate_area,
            ):
                rate = find_second_lowest_cost(rates)

        zip_and_rate_list.append((zipcode_to_find, str(rate)))
    return zip_and_rate_list


def write_zip_and_rate_to_csv(
    data: List[List[str]], csv_file: str = ZipsToFindSecondLowestCostLocation.DEFAULT
):
    """Writes zip and rate to a given file"""
    with open(csv_file, mode="w+", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Writing headers
        writer.writerow(CsvHeaders.ZIP_RATE)
        writer.writerows(data)

        file.close()


def write_file_data_to_terminal(csv_file: str):
    """Writes a csv file to terminal"""
    with open(csv_file, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            sys.stdout.write(",".join(row) + "\n")

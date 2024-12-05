class MetalLevel:
    BRONZE = "Bronze"
    SILVER = "Silver"
    GOLD = "Gold"
    PLATINUM = "Platinum"
    CATASTROPHIC = "Catastrophic"


class CsvHeaders:
    ZIP_RATE = ("zipcode", "rate")


class ZipsToFindSecondLowestCostLocation:
    DEFAULT = "static_files/slcsp.csv"
    TEST = "plan_finder/tests/sample_slcsp.csv"


class ZipRateAreaCsvLocation:
    DEFAULT = "static_files/zips.csv"
    TEST = "plan_finder/tests/sample_zips.csv"


class PlanCsvLocation:
    DEFAULT = "static_files/plans.csv"
    TEST = "plan_finder/tests/sample_plans.csv"

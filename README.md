

# Parking Rates API


## Table of Contents
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Custom Commands](#custom-commands)
- [Running Tests](#running-tests)
- [Assumptions](#assumptions)
- [Limitations](#limitations)
- [Improvements](#improvements)
- [Credits](#credits)


## Installation

Setup requirements:
- Python 3.13
- Poetry 1.8.4


## Getting Started

#### Allow the script to be executed on...
```bash
chmod +x run_app.sh
```

#### ... Then execute the script :)
```bash
./run_app.sh
```


## Custom Commands

#### Find the second lowest cost silver plans

```bash
./manage.py find_second_lowest_cost_plan
```
- Description: Opens CSV file, finds the second lowest rate silver plans, and regenerates the CSV file.
- Parameters: Path to CSV file with zips. Defaults to provided slcsp.csv file.


#### Regenerate slcsp.csv file
```bash
./manage.py generate_blank_slcsp
```
- Description: Regenerates slcsp.csv file without rates populated.
- Parameters: Does not allow for parameters.


#### Loads plans
```bash
./manage.py load_plans
```
- Description: Persists plan data from csv.
- Parameters: Path to CSV file with plans. Defaults to provided plans.csv file.


#### Loads zips
```bash
./manage.py load_zips_rate_areas
```
- Description: Persists zip data from csv.
- Parameters: Path to CSV file with zips. Defaults to provided zipz.csv file.


## Running Tests

To run the tests, make sure dev dependencies are installed first.
Then, simply enter:

```bash
pytest {optional: route to specific test or test suite}
```
==Note: A route to a specific test, test suite, or file, can be used as an argument==


## Assumptions

1. **Persisting data is okay.**
- Given there was a lot of data, I assumed that using a database to store the data was an acceptable solution. 
    - *Optimized:* This unlocked the ability to use Django's ORM, which is already optimized out of the box. 
    - *Quick reads:* While loading the data has some latency, reads of the data execute quickly.
    - *Relational DB agnostic:* While I am using SQLite because it is a quick setup, we can connect to any relational database that has a supported driver. If we keep the potential future of this small project in mind, we can easily add to it.

2. **Hiding keys is always good practice - but overkill for this challenge.**
- Adhering to industry standards, I do not commit potentially sensitive stuff, though I fully realize that creating an environment variable for the Django SECRET KEY is probably overkill for this scenario.

3. **Field-tracking or upserts not considered**
- This small app only allows for wiping data and uploading data from the given CSVs. There is no field-tracking or upserting functionality, as the directions did not request it, though would be something to consider if this data was expected to be added to or altered in any way.


## Limitations

1. Only Silver plans considered
- Per the directions, I opted to only filter for silver plans; however, with extensibility in mind, I made the metal levels an argument for filtering methods so that any additional filtering on different levels would be a light lift.

2. Rerunning 'load_zip_rate_areas' or 'load_plans' wipes data
- For sake of ease and the time constraint, I opted to wipe the table if it is already populated so that dealing with duplicates is not an issue I've made for myself.

## Improvements

1. A slimmer tech stack could have been used
- A web framework was not necessary to solve this challenge. Something like pandas and/or SQLAlchemy could have been used, however I am most familiar with Django and must respect the 2 hour time limit placed on coding a solution.
    - If this small functionality did need to be added to, say to create a web app where agents can look up the second lowest cost silver plans in a browser, then we could easily add the web components and even make those commands a task that runs to update zips and rates nightly.

2. Service layer
- All the logic that relates to the CSV functionality could be relocated to its own service layer instead of in a utils file. I think things would separate function responsibility nicely. 

3. More tests!
- Given more time I would have preferred to add more robust tests and created more fixtures. The commands are untested currently.

4. Normalized metal level
- for consistency sake, the metal_level CharField should have been normalized before saving. i.e. "SILVER" or "silver" instead of "Silver"

5. More documentation
- I specifically mean in the form of docstrings.


## Credits

##### A special thank you to:

- the team at Spark Advisors for reviewing my work. I had a lot of fun thinking through this problem and welcome your feedback.
- [open source libraries and the brains behind them](https://qph.cf2.quoracdn.net/main-qimg-ea57b52aff0903332036ada67f05d3f6) that have created these frameworks and libraries that we all use, free of charge.
- the folks that I have worked with in the past that have taken me under their wing. I'm eternally grateful :D <3

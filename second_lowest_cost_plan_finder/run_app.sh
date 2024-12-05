#!/bin/bash

# start environment
poetry shell

# install dependencies
poetry install

# migrate
python3 manage.py migrate

# run custom command to seed database
python3 manage.py load_zip_rate_areas
python3 manage.py load_plans

# run custom command to find second lowest cost silver plans for given zipcodes
python3 manage.py find_second_lowest_cost_plan

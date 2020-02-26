import json
import os
import re

import ckan.plugins.toolkit as toolkit
from ckanext.cct_metadata import CITY_STRUCTURE_FILENAME


def load_city_structure():
    cwd, = os.path.split(__file__)[:-1]
    city_structure_path_file = os.path.join(cwd, CITY_STRUCTURE_FILENAME)

    with open(city_structure_path_file) as city_structure_file:
        city_structure_data = json.load(city_structure_file)

    return city_structure_data


def build_structure_mappings():
    city_structure = load_city_structure()
    city_structure_mappings = {
        label_to_value(directorate["name"]): {
            "{}_{}".format(label_to_value(directorate["name"]), label_to_value(department["name"])): {
                "{}_{}_{}".format(label_to_value(directorate["name"]),
                                  label_to_value(department["name"]),
                                  label_to_value(branch["name"]))
                for branch in department.get("branches", [])
            }
            for department in directorate.get("departments", [])
        }
        for directorate in city_structure
    }

    return city_structure_mappings


def label_to_value(label):
    sanitised_string = (
        label.strip()
             .lower()
             .replace(" ", "_")
    )

    pattern = re.compile(r'\W')
    sanitised_string = re.sub(
        pattern, "",
        sanitised_string
    )

    return sanitised_string


def get_departments(*args):
    city_structure = load_city_structure()
    departments = [
        {
            "label": department["name"] + " ({})".format(directorate_dict["name"]),
            "value": label_to_value("{}_{}".format(directorate_dict["name"], department["name"]))
        }
        for directorate_dict in city_structure
        for department in directorate_dict["departments"]
    ]

    return departments


def get_branches(*args):
    city_structure = load_city_structure()
    branches = [
        {
            "label": branch["name"] + " ({} / {})".format(directorate_dict["name"], department["name"]),
            "value": label_to_value("{}_{}_{}".format(directorate_dict["name"], department["name"], branch["name"]))
        }
        for directorate_dict in city_structure
        for department in directorate_dict["departments"]
        for branch in department["branches"]
    ]

    return branches

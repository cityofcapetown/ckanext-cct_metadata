import json
import os

import ckanext
from ckanext.cct_metadata import helpers
from ckan.lib.navl import dictization_functions


def department_check(key, data, errors, context):
    department = data[key]
    city_structure_mappings = helpers.load_city_structure_mappings()

    directorate_id = data[('owner_org',)]
    model = context['model']
    directorate = helpers.label_to_value(model.Group.get(directorate_id).title)

    if department not in city_structure_mappings.get(directorate, {}):
        raise dictization_functions.Invalid("Department is not in Directorate")

    return department


def branch_check(key, data, errors, context):
    branch = data[key]
    city_structure_mappings = helpers.load_city_structure_mappings()

    directorate_id = data[('owner_org',)]
    model = context['model']
    directorate = helpers.label_to_value(model.Group.get(directorate_id).title)
    department = data[('dstr_department',)]

    departments = city_structure_mappings.get(directorate, {})
    branches = departments.get(department, {})
    if branch not in branches:
        raise dictization_functions.Invalid("Branch is not in Department")

    return branch
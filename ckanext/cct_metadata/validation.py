from ckanext.cct_metadata import helpers
from ckan.lib.navl import dictization_functions

from ckanext.cct_metadata import UNDER_CONSTRUCTION


def department_check(key, data, errors, context):
    department = data[key]
    city_structure_mappings = helpers.build_structure_mappings()

    directorate_id = data[('owner_org',)]
    model = context['model']
    directorate = helpers.label_to_value(model.Group.get(directorate_id).title)

    departments = city_structure_mappings.get(directorate, {})
    if department not in departments and directorate != UNDER_CONSTRUCTION:
        raise dictization_functions.Invalid("Department is not in selected directorate")

    return department


def branch_check(key, data, errors, context):
    branch = data[key]
    city_structure_mappings = helpers.build_structure_mappings()

    directorate_id = data[('owner_org',)]
    model = context['model']
    directorate = helpers.label_to_value(model.Group.get(directorate_id).title)
    department = data[('dstr_department',)]

    departments = city_structure_mappings.get(directorate, {})
    branches = departments.get(department, {})
    if branch not in branches and directorate != UNDER_CONSTRUCTION:
        raise dictization_functions.Invalid("Branch is not in selected department")

    return branch

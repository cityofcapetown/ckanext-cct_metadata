from ckanext.cct_metadata import helpers
from ckan.lib.navl import dictization_functions

from ckanext.cct_metadata import UNDER_CONSTRUCTION


def _get_directorate_from_model_with_id(model, directorate_id):
    directorate_group = model.Group.get(directorate_id)
    directorate = helpers.label_to_value(directorate_group.title) if directorate_group is not None else None

    return directorate

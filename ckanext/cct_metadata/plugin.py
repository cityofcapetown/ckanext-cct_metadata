import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

from ckanext.cct_metadata import helpers, validation


class Cct_MetadataPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IValidators)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'cct_metadata')

    def get_helpers(self):
        return {
            'cct_metadata_get_departments': helpers.get_departments,
            'cct_metadata_get_branches': helpers.get_branches
        }

    def get_validators(self):
        return {
            'cct_metadata_check_department': validation.department_check,
            'cct_metadata_check_branch': validation.branch_check
        }
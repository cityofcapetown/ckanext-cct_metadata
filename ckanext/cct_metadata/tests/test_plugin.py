"""Tests for plugin.py."""
import unittest
import logging
import pprint

import ckanext.cct_metadata.plugin as plugin


def _load_city_structure_mock():
    test_structure = [
        {
            "name": "Gordon's Directorate of Doom",
            "departments": [
                {
                    "name": "Gordon's Department of Delight",
                    "branches": [
                        {
                            "name": "Gordon's Branch of Bounty"
                        }
                    ]
                },
                {
                    "name": "Gordon's Department of Despair",
                    "branches": []
                }
            ]
        }
    ]

    return test_structure


class Cct_MetadataPluginHelpersTest(unittest.TestCase):
    def setUp(self):
        plugin.helpers.load_city_structure = _load_city_structure_mock

    def test_build_structure_mappings(self):
        test_structure_mappings = {
            'gordons_directorate_of_doom': {
                'gordons_directorate_of_doom_gordons_department_of_delight': {
                    'gordons_directorate_of_doom_gordons_department_of_delight_gordons_branch_of_bounty'
                },
                'gordons_directorate_of_doom_gordons_department_of_despair': set([])
            }
        }
        # logging.debug("test_structure_mapping=\n{}".format(
        #     pprint.pformat(test_structure_mappings)
        # ))

        structure_mapping = plugin.helpers.build_structure_mappings()
        # logging.debug("structure_mapping=\n{}".format(
        #     pprint.pformat(structure_mapping)
        # ))
        self.maxDiff = None
        self.assertDictEqual(test_structure_mappings, structure_mapping)

    def test_get_departments(self):
        test_departments = [
            {
                "label": "Gordon's Department of Delight (Gordon's Directorate of Doom)",
                "value": "gordons_directorate_of_doom_gordons_department_of_delight"
            },
            {
                "label": "Gordon's Department of Despair (Gordon's Directorate of Doom)",
                "value": "gordons_directorate_of_doom_gordons_department_of_despair"
            }
        ]
        departments = plugin.helpers.get_departments()
        self.assertListEqual(departments, test_departments)

    def test_get_branches(self):
        test_branches = [
            {
                "label": "Gordon's Branch of Bounty (Gordon's Directorate of Doom / Gordon's Department of Delight)",
                "value": "gordons_directorate_of_doom_gordons_department_of_delight_gordons_branch_of_bounty"
            }
        ]
        branches = plugin.helpers.get_branches()
        self.assertListEqual(branches, test_branches)


class Cct_MetadataPluginValidationTest(unittest.TestCase):
    def _get_directorate_from_model_with_id(self):
        class TestModel:
            def __init__(self, Group={}):
                self.Group = Group
        class TestGroup:
            def __init__(self, title=""):
                self.title = title

        test_good_directorate_id = "definitely_exists"
        test_good_directorate = "Definitely Exists"
        test_good_model = TestModel({test_good_directorate_id: TestGroup(test_good_directorate)})

        directorate = plugin.validation._get_directorate_from_model_with_id(test_good_model, test_good_directorate_id)
        self.assertEquals(directorate, test_good_directorate)

        test_bad_directorate_id = "definitely_doesnt_exist"
        test_bad_model = TestModel()

        directorate = plugin.validation._get_directorate_from_model_with_id(test_bad_model, test_bad_directorate_id)
        self.assertIsNone(directorate)

    def test_department_check(self): pass

    def test_branch_check(self): pass


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s-%(module)s.%(funcName)s [%(levelname)s]: %(message)s')

    unittest.main()

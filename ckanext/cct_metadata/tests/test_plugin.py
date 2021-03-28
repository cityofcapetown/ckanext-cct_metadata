"""Tests for plugin.py."""
import unittest
import logging

import ckanext.cct_metadata.plugin as plugin


class Cct_MetadataPluginHelpersTest(unittest.TestCase):
    def setUp(self): pass


class Cct_MetadataPluginValidationTest(unittest.TestCase):
    def _get_directorate_from_model_with_id(self):
        class TestModel:
            def __init__(self, group={}):
                self.Group = group

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


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s-%(module)s.%(funcName)s [%(levelname)s]: %(message)s')

    unittest.main()

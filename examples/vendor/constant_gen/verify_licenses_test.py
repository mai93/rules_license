"""Test that we see the expected licenses for some generated code."""

import codecs
import os

import unittest
from tests import license_test_utils

class VerifyLicensesTest(unittest.TestCase):

  def test_generater_license(self):
    package_base = license_test_utils.LICENSE_PACKAGE_BASE
    licenses_info = license_test_utils.load_licenses_info(
        os.path.join(os.path.dirname(__file__), "generator_licenses.json"))

    expected = {
        "examples/vendor/constant_gen:constant_generator": [
            "examples/vendor/constant_gen:license"
        ],
    }
    license_test_utils.check_licenses_of_dependencies(
        self, licenses_info, expected)

  def test_generated_code_license(self):
    package_base = license_test_utils.LICENSE_PACKAGE_BASE
    licenses_info = license_test_utils.load_licenses_info(
        os.path.join(os.path.dirname(__file__), "generated_code_licenses.json"))

    expected = {
        "examples/vendor/constant_gen:libhello": [
            "/constant_gen:license_for_emitted_code",
        ],
        "examples/vendor/constant_gen:libhello_src_": [
            "/constant_gen:license_for_emitted_code",
        ],
    }
    license_test_utils.check_licenses_of_dependencies(
        self, licenses_info, expected)

if __name__ == "__main__":
  unittest.main()


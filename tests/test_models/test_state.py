#!/usr/bin/python3
""" """
import os

from models.city import City
from tests.test_models.test_base_model import TestBasemodel


class TestState(TestBasemodel):
    """Test model for state"""

    def __init__(self, *args, **kwargs):
        """TEST CALSS INITALIZATION."""
        super().__init__(*args, **kwargs)
        self.args = args
        self.kwargs = kwargs

    def TestName(self):
        """TYPE OF NAME TESTING"""
        n = self.value()
        self.assertEqual(
            type(n.name),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

#!/usr/bin/python3
"""
test class state
"""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.state import State
import unittest
import models


class TestState(unittest.TestCase):
    """
    test cases
    """
    def test_create_state(self):
        """
        create test state
        """
        state = State()
        self.assertIsInstance(state, State)

    def test_state_name(self):
        """
        test state name
        """
        state = State()
        self.assertEqual(state.name, "")

    def test_set_state_name(self):
        """
        test set state name
        """
        state = State()
        state.name = "Oxford"
        self.assertEqual(state.name, "Oxford")

    def test_to_dict(self):
        """
        test to dict
        """
        state = State()
        state.name = "Oxford"
        state_dict = state.to_dict()
        self.assertEqual(state_dict['name'], "Oxford")
        self.assertEqual(state_dict['__class__'], 'State')


if __name__ == '__main__':
    unittest.main()

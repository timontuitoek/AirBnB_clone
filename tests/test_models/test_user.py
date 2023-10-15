#!/usr/bin/python3
"""
test user
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
import unittest
import models


class TestUser(unittest.TestCase):
    """
    test user docs
    """
    def test_modulesDocs(self):
        """
        test_docs
        """
        moduleDoc = (
                __import__("models.user")
                .user.__doc__)
        self.assertGreater(len(moduleDoc), 0)

    def test_classDocs(self):
        '''
        Docs
        '''
        classDoc = (
                __import__("models.user")
                .user.User.__doc__)
        self.assertGreater(len(classDoc), 0)

    def test_attributes_Type(self):
        '''
        Docs
        '''
        user = User()
        self.assertIs(type(user.email), str)
        self.assertIs(type(user.password), str)
        self.assertIs(type(user.first_name), str)
        self.assertIs(type(user.last_name), str)


if __name__ == "__main__":
    unittest.main()

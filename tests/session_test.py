import unittest

from models.session import Session

class TestSession(unittest.TestCase):
    def setUp(self):
        self.session = Session("No Pain No Gains", "07:00", "Strength")
    
    def test_session_has_name(self):
        self.assertEqual("No Pain No Gains", self.session.name)
    
    def test_session_has_time(self):
        self.assertEqual("07:00", self.session.time)

    def test_session_has_category(self):
        self.assertEqual("Strength", self.session.category)


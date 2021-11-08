import unittest
from models.member import Member

class TestMember(unittest.TestCase):
    def setUp(self):
        self.member = Member("Sam", "Adams", 24, "Strength")

    def test_member_has_first_name(self):
        self.assertEqual("Sam", self.member.first_name)
    
    def test_member_has_last_name(self):
        self.assertEqual("Adams", self.member.last_name)
    
    def test_member_has_age(self):
        self.assertEqual(24, self.member.age)
    
    def test_member_has_category(self):
        self.assertEqual("Strength", self.member.category)
    
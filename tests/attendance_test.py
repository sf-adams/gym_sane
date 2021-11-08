import unittest

import unittest
from models.member import Member
from models.session import Session
from models.attendance import Attendance

class TestAttendance(unittest.TestCase):
    def setUp(self):
        self.member = Member("Sam", "Adams", 24, "Strength")
        self.session = Session("No Pain No Gains", "07:00", "Strength")
        self.attendance = Attendance(self.member, self.session)

    def test_attendance_can_have_member(self):
        self.assertEqual(self.member, self.attendance.member)
    
    def test_attendance_can_have_session(self):
        self.assertEqual(self.session, self.attendance.session)
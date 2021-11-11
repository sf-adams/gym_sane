import unittest

import unittest
from models.member import Member
from models.session import Session
from models.booking import Booking

class TestBooking(unittest.TestCase):
    def setUp(self):
        self.member = Member("Sam", "Adams", 24, "Strength")
        self.session = Session("No Pain No Gains", "07:00", "Strength")
        self.booking = Booking(self.member, self.session)

    def test_attendance_can_have_member(self):
        self.assertEqual(self.member, self.booking.member)
    
    def test_attendance_can_have_session(self):
        self.assertEqual(self.session, self.booking.session)
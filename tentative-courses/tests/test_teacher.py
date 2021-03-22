# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 19:42:42 2021

@author: belen
"""
import unittest
import sys
sys.path.insert(0, '..')
import Teacher, Student, Company
import settings as st


class TestTeacher(unittest.TestCase):

    def test_teacher_availability(self):
        """
        Test that course time matches teacher's and student's availability.
        """
        
        s1 = Student.Student(1, "Juan", "Perez", "Individual", "Beginner", [["Monday", "13:00"], ["Wednesday", "15:00"], ["Friday", "19:00"]])
        t1 = Teacher.Teacher("Mariana", "Polak", [["Monday", "13:00"], ["Wednesday", "15:00"], ["Thursday", "15:00"], ["Friday", "19:00"]])
        c1 = Company.Company("TestTeacher")
        
        c1.students.append(s1)
        st.teachers.append(t1)
        
        c1.make_courses()
        
        self.assertEqual(len(c1.courses), 1, "Course hasn't been created")
        self.assertEqual(c1.courses[0].time, ["Monday", "13:00"], "Course time failed")
        
    def test_teacher_availability_fail(self):
        """
        Test that no course is created when teacher's and student's availability don't match.
        """
        
        s2 = Student.Student(1, "Juan", "Perez", "Individual", "Beginner", [["Monday", "13:00"], ["Wednesday", "15:00"], ["Friday", "19:00"]])
        t2 = Teacher.Teacher("Mariana", "Polak", [["Monday", "9:00"], ["Wednesday", "9:00"], ["Thursday", "9:00"], ["Friday", "11:00"]])
        c2 = Company.Company("TestTeacher")
        
        c2.students.append(s2)
        st.teachers.append(t2)
        
        c2.make_courses()
        
        self.assertEqual(len(c2.courses), 0, "Course has been created")
        

if __name__ == "__main__":
    unittest.main()


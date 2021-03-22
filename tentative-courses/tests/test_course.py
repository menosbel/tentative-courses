# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 12:19:56 2021

@author: belen
"""
import unittest
import sys
sys.path.insert(0, '..')
import Teacher, Student, Company
import settings as st


class TestCourse(unittest.TestCase):

    def test_course_level(self):
        """
        Test that course and students' level matches.
        """
        
        s1 = Student.Student(1, "Juan", "Perez", "Group", "Beginner", [["Monday", "13:00"], ["Wednesday", "15:00"], ["Friday", "19:00"]])
        s2 = Student.Student(2, "Carla", "Marino", "Group", "Intermediate", [["Monday", "13:00"], ["Wednesday", "15:00"], ["Friday", "18:00"]])
        s3 = Student.Student(3, "Pedro", "Perez", "Group", "Beginner", [["Monday", "13:00"], ["Wednesday", "15:00"], ["Friday", "18:00"]])
        t1 = Teacher.Teacher("Mariana", "Polak", [["Monday", "13:00"], ["Wednesday", "15:00"], ["Thursday", "15:00"], ["Friday", "19:00"]])
        c1 = Company.Company("TestCourse")
        
        c1.students = [s1, s2, s3]
        st.teachers.append(t1)
        
        c1.make_courses()
        
        # There should be only two students in this course
        self.assertEqual(len(c1.courses[0].student_list), 2, "One of the students is in the wrong course.")
        
        # Both of them should be Beginners
        self.assertEqual(c1.courses[0].student_list[0].level, c1.courses[0].student_list[1].level, "Students in group don't have same level")


    def test_group_course_num(self):
        """
        Test that group course complies with max amonunt of students requirement.
        """
        
        s1 = Student.Student(1, "Lucas", "Savorido", "Group", "Advanced", [["Monday", "9:00"], ["Thursday", "19:00"]])
        s2 = Student.Student(2, "Mariana", "Pasos", "Group", "Advanced", [["Monday", "10:00"], ["Thursday", "19:00"]])
        s3 = Student.Student(3, "Juliana", "Gonzalez", "Group", "Advanced", [["Monday", "11:00"], ["Thursday", "19:00"]])
        s4 = Student.Student(4, "Irina", "Manta", "Group", "Advanced", [["Monday", "12:00"], ["Thursday", "19:00"]])
        s5 = Student.Student(5, "Facundo", "Marques", "Group", "Advanced", [["Monday", "13:00"], ["Thursday", "19:00"]])
        s6 = Student.Student(6, "Liliana", "Romero", "Group", "Advanced", [["Monday", "14:00"], ["Thursday", "19:00"]])
        s7 = Student.Student(7, "Julia", "Pepenek", "Group", "Advanced", [["Monday", "15:00"], ["Thursday", "19:00"]])

        t2 = Teacher.Teacher("Mary", "Smith", [["Thursday", "19:00"], ["Friday", "9:00"]])
        c2 = Company.Company("TestCourse2")
        
        c2.students = [s1, s2, s3, s4, s5, s6, s7]
        st.teachers.append(t2)
        
        c2.make_courses()
        
        # There should only be 6 students in this course although there are 7 with same availability
        self.assertEqual(len(c2.courses[0].student_list), 6, "Number of students in course is incorrect")
        
        
    def test_individual_course_num(self):
        """
        Test that individual group has only one student
        """
        
        s1 = Student.Student(1, "Lucas", "Savorido", "Individual", "Advanced", [["Monday", "9:00"], ["Thursday", "19:00"]])
        s2 = Student.Student(2, "Mariana", "Pasos", "Individual", "Advanced", [["Monday", "9:00"], ["Thursday", "19:00"]])
        
        t3 = Teacher.Teacher("Johanna", "Millford", [["Monday", "9:00"], ["Wednesday", "18:00"], ["Thursday", "19:00"]])
        c3 = Company.Company("TestCourse3")
        
        c3.students = [s1, s2]
        st.teachers.append(t3)
        
        c3.make_courses()
        
        # There should be two courses with one student each
        self.assertEqual(len(c3.courses), 2, "Number of courses given those students is incorrect")
        self.assertEqual(len(c3.courses[0].student_list), 1, "There are too many students in that course")
        self.assertEqual(len(c3.courses[1].student_list), 1, "There are too many students in that course")


    def test_group_course_modality(self):
        """
        Test that all students in group had chosen same modality.
        """
        
        # All three students have same day available. Two chose to be in a group and one didn't
        s1 = Student.Student(1, "Lucas", "Savorido", "Group", "Advanced", [["Monday", "9:00"], ["Thursday", "19:00"]])
        s2 = Student.Student(2, "Mariana", "Pasos", "Individual", "Advanced", [["Monday", "10:00"], ["Thursday", "19:00"]])
        s3 = Student.Student(3, "Juliana", "Gonzalez", "Group", "Advanced", [["Monday", "11:00"], ["Thursday", "19:00"]])
        
        t4 = Teacher.Teacher("Milfred", "Wainfield", [["Thursday", "19:00"]])
        c4 = Company.Company("TestCourse4")
        
        c4.students = [s1, s2, s3]
        st.teachers.append(t4)
        
        c4.make_courses()
        
        # There should be only 2 students in the group
        self.assertEqual(len(c4.courses[0].student_list), 2, "Someone who chose the individual modality is in a group")

if __name__ == "__main__":
    unittest.main()




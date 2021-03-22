# -*- coding: utf-8 -*-

import Company as company

"""
CREATE NEW COMPANY
"""

c = company.Company("Disney")


"""
GET TEACHERS AND STUDENTS

"""
c.get_teachers()
c.get_students()     

"""
MAKE FIRST COURSES

"""
c.make_courses()


"""
MAKE A LIST OF STUDENTS WHO DON'T HAVE A COURSE

"""
c.list_students_without_course()


""""
FIND COURSE FOR STUDENTS WHO DON'T HAVE ONE

"""
c.find_aprox_course()


"""
DELETE COURSES THAT DON'T MEET REQUIREMENTS
    
"""
c.check_requirements_all_courses()
c.delete_courses()


"""
PRINT COURSES

Print all remaining courses for that company

"""
c.print_all_courses()


"""
PRINT STUDENTS WITHOUT COURSE

Print students who haven't been assigned to a course

"""
c.list_students_without_course()

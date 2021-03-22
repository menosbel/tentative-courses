# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 11:02:02 2021

@author: belen
"""
import json
import settings as st
import Student as student
import Teacher as teacher
import Course as course


class Company:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.courses = []
        self.students_without_course = []
        st.teachers = []
        
        
    def __str__(self):
        return f"""
    Company name: {self.name}
    Employees: {self.employees}
    Courses: {self.courses}
    Students without course: {self.students_without_course}
    """
    
    # Get teachers from .json and make a list   
    def get_teachers(self):
        with open(st.teachers_file) as f:       
            data_teachers = json.load(f)
        for t in data_teachers['teachers']:
            first = t['first']
            last = t['last']
            availability = t['availability']
            
            t = teacher.Teacher(first, last, availability)
            
            st.teachers.append(t)
            
            
    # Get students from .json, instantiate it and make a list as a Company attribute
    def get_students(self):
        with open(st.students_file) as f:       
            data_students = json.load(f)
        for s in data_students['students']:
            id_student = s['id']
            first = s['first']
            last = s['last']
            modality = s['modality']
            level = s['level']
            availability = s['availability']
            
            new_student = student.Student(id_student, first, last, modality, level, availability)
            self.students.append(new_student)
           
            
    # Create courses for company's students     
    def make_courses(self):
        for s in self.students:
            if s.modality == 'Individual':  # If chosen modality is individual
                for time in s.availability:
                    self.find_teacher(s, time) # Find a teacher matching availability
                    
                    if s.has_course:
                        break
                
            elif s.modality == 'Group': # If chosen modality is group
                if self.courses:
                    for c in self.courses: # Check existing groups
                        accepted = c.accept_new_student(s) # See if they meet student's requirements
                        if accepted:
                            c.student_list.append(s)
                            
                            s.has_course = True
                            s.assigned_course = c.id_course
                            break
                
                # If no course matches student's requirements, create a new one
                if s.has_course == False:
                    self.start_new_group(s, s.availability)
                    
    
    # Match student's and teacher's availability and create new Course
    def find_teacher(self, lonely_student, student_time, multiple_hours=False):
        for t in st.teachers:
            if student_time in t.availability:
                teacher_name = t.full_name
                modality = lonely_student.modality
                level = lonely_student.level
                time = student_time
                
                c = course.Course(teacher_name, modality, level, time)
                self.courses.append(c)
                
                c.student_list.append(lonely_student)
                
                # If new course starts an hour before or after student's availability. Wait for confirmation
                if multiple_hours:
                    c.needs_student_confirmation.append(lonely_student)
                    print(f'{lonely_student.full_name} has been assigned to course #{c.id_course}')
                    print(c)
                
                lonely_student.assigned_course = c.id_course
                lonely_student.has_course = True
                
                t.availability.remove(time)
                
                break
                
    # Creates a new group according to student's availability    
    def start_new_group(self, lonely_student, student_availability):
        for time in student_availability:
            self.find_teacher(lonely_student, time)
            
            if lonely_student.has_course == True:
                break
    
    # Look for group one hour before or after student's availability
    def find_aprox_group(self, lonely_student):
        for c in self.courses:
            # Check if student meets requirements to join group
            accepted = c.accept_new_student(lonely_student, multiple_hours = True)
            
            if accepted:
                c.student_list.append(lonely_student)
                c.needs_student_confirmation.append(lonely_student)
                
                lonely_student.has_course = True
                lonely_student.assigned_course = c.id_course
    
                print(f'{lonely_student.full_name} has been assigned to course #{c.id_course}')
                break
            
            if lonely_student.has_course == True:
                break
            # If there is no group, look for a partner to create a new one
            else:
                self.find_partner()
                
                
    # MEJORA: lista de posibilidades para estudiante
    # Look for teacher for individual course within range (+n -n student's availability)
    def find_aprox_individual(self, s):
        aprox_availability = []
        
        for time in s.availability:
            time = int(self.time[1].split(':')[0])
            time_1 = str(time - st.hour_range) + ':00'
            time_2 = str(time + st.hour_range) + ':00'
            day = self.time[0]
            
            availability_1 = [day, time_1]
            availability_2 = [day, time_2]
            
            aprox_availability.append(availability_1)
            aprox_availability.append(availability_2)
            
        for av in aprox_availability:
            self.find_teacher(s, av, multiple_hours=True)
            
            if s.has_course:
                break
            
    
    def find_partner(self):
        pass
        # print('Looks for partner')
            
            
    # Check if courses meet requirenments. List students without course
    def check_requirements_all_courses(self):
        for c in self.courses:
            c.check_requirements()
                
    
    # Print list of students without course
    def list_students_without_course(self):
        print('List of students without course')
        for s in self.students:
            if s.has_course == False:
                self.students_without_course.append(s)
                print(f'{s.full_name}')
    
    
    # Find group course by aprox time for students without course. List courses that need confirmation
    def find_aprox_course(self):
        for s in self.students_without_course:
            if s.modality == 'Group':
                self.find_aprox_group(s)
            elif s.modality == 'Individual':
                self.find_aprox_individual(s)
        
        # Make list of students who need to confirm if they join the course
        self.list_confirmation_needed()
    
    
    # Find courses with students whose time confirmation is needed        
    def list_confirmation_needed(self):
        for c in self.courses:
            if c.needs_student_confirmation:
                for s in c.needs_student_confirmation:
                    print(f'Course #{c.id_course} needs confimation from {s.full_name}')
                
                
    # Delete courses that don't meet requirements
    def delete_courses(self):
        must_delete = []
        for c in self.courses:
            if (c.num_approved == False) or (c.modality_approved == False) or (c.level_approved == False):
                must_delete.append(c)
                print(f'Course #{c.id_course} has been deleted')
                for s in c.student_list:
                    for stu in self.students:
                        if stu.id_student == s.id_student:
                            stu.has_course = False
                            print(f'{stu.full_name} has not got a course anymore')
                            break
        for d_course in must_delete:
            self.courses.remove(d_course)
    
    
    # Print all courses
    def print_all_courses(self):
        for c in self.courses:
            print(c)
        
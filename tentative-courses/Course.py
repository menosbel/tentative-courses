# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 19:24:40 2021

@author: belen
"""
import settings as st

class Course:
    course_counter = 0
    
    def __init__(self, teacher, modality, level, time):
        Course.course_counter += 1
        self.id_course = Course.course_counter
        self.teacher = teacher
        self.modality = modality
        self.level = level
        self.time = time
        self.student_list = []
        self.needs_student_confirmation = []
        self.num_approved = False
        self.modality_approved = False
        self.level_approved = False
         
        
    def __str__(self):
        student_names = []
        for stu in self.student_list:
            student_names.append(stu.full_name)
        return f'''
    ----
    COURSE #{self.id_course}
    Teacher: {self.teacher}
    Modality: {self.modality}
    Level: {self.level}
    Time: {self.time[0] + ' ' + self.time[1]}
    Student list: {student_names}
    '''
    
    # Check if student can join course
    def accept_new_student(self, lonely_student, multiple_hours = False):
        # If looking for a match within hour range (+n -n student's availability)
        if multiple_hours:
            time = int(self.time[1].split(':')[0])
            time_1 = str(time - st.hour_range) + ':00'
            time_2 = str(time + st.hour_range) + ':00'
            day = self.time[0]
            
            availability_1 = [day, time_1]
            availability_2 = [day, time_2]
            
            course_time = [availability_1, availability_2]
            
        # If looking for exact availability match
        else:
            course_time = [self.time]
            
        # Check if modality, level and availability of student matches the course's.
        if self.modality == lonely_student.modality:
            if self.level == lonely_student.level:
                for time in course_time:
                    if time in lonely_student.availability:
                        if len(self.student_list) < st.max_students:
                            return True
        return False
                
    # Check if course meets all requirements
    def check_requirements(self):
        self.check_num_approved()
        self.check_modality_approved()
        self.check_level_approved()
        
        if self.num_approved and self.modality_approved and self.level_approved:
            print(f'Course #{self.id_course} meets all requirements')
        elif self.num_approved == False:
            print(f'Course #{self.id_course} does\'t meet all requirements. WARNING: number of students')
        elif self.modality_approved == False:
            print(f'Course #{self.id_course} does\'t meet all requirements. WARNING: modality of students')
        elif self.level_approved == False:
            print(f'Course #{self.id_course} does\'t meet all requirements. WARNING: level of students')
        print('----')
        
    # Check if number of students in course is right
    def check_num_approved(self):
        if self.modality == 'Individual':
            if len(self.student_list) == 1:
                self.num_approved = True
            elif len(self.student_list) > 1:
                self.num_approved = False
        
        elif self.modality == 'Group':
            if len(self.student_list) > st.max_students:
                self.num_approved = False
            elif len(self.student_list) < st.min_students_group:
                self.num_approved = False
            else:
                self.num_approved = True
                
    # Check if all students in course have same modality
    def check_modality_approved(self):
        for s in self.student_list:                
            if s.modality == self.modality:
                self.modality_approved = True
            else:
                self.modality_approved = False
            
    # Check if all students have same level        
    def check_level_approved(self):
        for s in self.student_list:                
            if s.level == self.level:
                self.level_approved = True
            else:
                self.level_approved = False
    
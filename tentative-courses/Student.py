class Student:
    def __init__(self, id_student, first, last, modality, level, availability):
        self.id_student = id_student
        self.first = first
        self.last = last
        self.modality = modality
        self.level = level
        self.availability = availability
        self.full_name = self.first + ' ' + self.last
        self.has_course = False
        self.assigned_course = ''
        
        
    def __str__(self):
        return f'''
    Id: {self.id_student}
    Name: {self.first} 
    Last: {self.last}
    Modality: {self.modality}
    Level: {self.level}
    Availability: {self.availability}
    '''
    
    # Check if student has been asigned to a course or not
    def check_has_course(self):
        if self.has_course == True:
            print(f'{self.full_name} has been assigned to group {self.assigned_course}')
        else:
            print(f'{self.full_name} hasn\'t been assigned to a course yet')
# Tentative Courses

This program creates new courses for students by matching the students' and the teachers' availabilities.
Students are assigned to courses in a first come first served basis.


## How it works

1. Create a new company and makes two lists: one with all teachers and another one with the company's students.

2. Assign students to courses in a first come first served basis.

    If the student chose individual modality:
    - Loop through students availability and find them a match by looping through each teachers availability.
    
    If the student chose group modality:
    - Check if there is an existing group course that meets student's requirements (availability and level).
    - If there is none, create a new one by looping through the student's availability and finding an available teacher.
    
    Each time a course is created and assigned to a teacher. That availability is deleted from the teachers list of availabilities.

3. Make a list of students who haven't been assigned to a course yet.

4. Find a course for students who don't have one ye.

    If the student chose individual modality:
    - Look for a teacher with availability one hour before of after student's availability.
    
    If the  student chose group modality:
    - Try to fit them in an already created course that starts an hour later or before of student's availability.
    - (UPGRADE TO BE DEVELOPED) If there isn't one, find them a partner to create a new one. A match is made if students' availability varies by one hour.
   
   In any case, make a list inside each course with students who need to confirm if they can join it or not.

5. Check if all courses meet the requirements and delete the ones that don't.
     - Groups should have between 2 and 6 students
     - All students in a group should have chosen same modality
     - All students in a group should have the same level
     - Individual groups should only have one student

## Getting Started

These instructions will help you run the program in your terminal.

### Prerequisites

Python >= 3


### Running the program

From the main directory run the following command:

```
python main.py
```


## Running the tests

These tests check that no course is created if the requirements are not met.

1. To check if the course is only created if the student's availability matches the teacher's availability.

    From the tests directory run the following command:
    
    ```
    python test_teacher.py
    ```

2. To check if the following requirements are met:

    - All students in a course have the same level and no one else is included even though their availability matches the course's time.
    - Individual courses have only one student
    - Group courses have between 2 and 6 students
    - All students in a group course had chosen group modality 
    
    From the tests directory run the following command:
    
    ```
    python test_course.py
    ```

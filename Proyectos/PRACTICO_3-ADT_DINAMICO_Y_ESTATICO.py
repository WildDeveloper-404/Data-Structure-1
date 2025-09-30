# Example of an ADT for a Classroom, with static and dynamic models

class Classroom:
    """
    Representation of a Classroom object.

    Parameters:
        name (str): The name of the classroom.
        subject (str): The subject taught in this classroom.
        capacity (int): Maximum number of students allowed.
    """

    def __init__(self, name=None, subject=None, capacity=5):
        """
        Constructor for the Classroom class.
        """
        self.__name = name
        self.__subject = subject
        self.__capacity = capacity
        self.__students = [None] * capacity  # Fixed space for students

    # -----------------------
    # Property: name
    # -----------------------
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    # -----------------------
    # Property: subject
    # -----------------------
    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, value):
        self.__subject = value

    # -----------------------
    # Static ADT Model: Students
    # -----------------------
    def add_student(self, student_name):
        """
        Add a student in the first empty position.

        Args:
            student_name (str): Name of the student.

        Returns:
            bool: True if added, False if full.
        """
        for i in range(self.__capacity):
            if self.__students[i] is None:
                self.__students[i] = student_name
                return True
        return False  # No space left

    def remove_student(self, student_name):
        """
        Remove a student by name.

        Args:
            student_name (str): Name of the student to remove.

        Returns:
            bool: True if removed, False if not found.
        """
        for i in range(self.__capacity):
            if self.__students[i] == student_name:
                self.__students[i] = None
                return True
        return False

    @property
    def students(self):
        """
        Returns the list of students currently in the classroom.
        """
        return [s for s in self.__students if s is not None]

    # -----------------------
    # String representation
    # -----------------------
    def __str__(self):
        return f"Classroom {self.name} ({self.subject})"


# -----------------------
# Dynamic ADT Model: Queue of Classrooms
# -----------------------
class ClassroomQueue:
    def __init__(self):
        self.classrooms = []
    
    def add_classroom(self, classroom):
        self.classrooms.append(classroom)
    
    def remove_classroom(self, classroom):
        if classroom in self.classrooms:
            self.classrooms.remove(classroom)

    @property
    def list_of_classrooms(self):
        # Return only the name of each classroom
        return [str(c) for c in self.classrooms]


# -----------------------
# Example usage
# -----------------------
room1 = Classroom("A1", "Math")
room2 = Classroom("B2", "Science")
room3 = Classroom("C3", "History")

# Static ADT: Students
room1.add_student("Alice")
room1.add_student("Bob")
room1.add_student("Charlie")
room1.add_student("Diana")
room1.add_student("Eve")

print(room1.students)  # ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']

room1.add_student("Frank")  # Won’t be added, room is full
room1.remove_student("Charlie")
room1.add_student("Frank")  # Now Frank can join

print(room1.students)  # ['Alice', 'Bob', 'Diana', 'Eve', 'Frank']

# Dynamic ADT: Queue of classrooms
queue = ClassroomQueue()
queue.add_classroom(room1)
queue.add_classroom(room2)

print(queue.list_of_classrooms)  # ['Classroom A1 (Math)', 'Classroom B2 (Science)']

queue.remove_classroom(room1)

print(queue.list_of_classrooms)  # ['Classroom B2 (Science)']
#!/usr/bin/env python

from user import User
import random  # Ensure the random module is imported

knowledge = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]

class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)  # Call the User's __init__ method
        self.knowledge = knowledge  # Initialize the knowledge attribute

    def teach(self):
        # Get a random index from the knowledge list
        random_index = random.randint(0, len(self.knowledge) - 1)
        # Return the knowledge string at that index
        return self.knowledge[random_index]

# Example of creating a Teacher instance and teaching
teacher = Teacher("Jane", "Smith")
print(teacher.teach())  # Output: A random knowledge string from the list
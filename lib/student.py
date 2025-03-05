#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)  # Call the User's __init__ method
        self.knowledge = []  # Initialize knowledge as an empty list

    def learn(self, knowledge_string):
        """Adds a knowledge string to the student's knowledge list."""
        self.knowledge.append(knowledge_string)  # Add the string to the knowledge list

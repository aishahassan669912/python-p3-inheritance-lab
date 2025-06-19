#!/usr/bin/env python

from user import User
import random

class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = ["Algebra", "Biology", "History"]  # make sure this is added here

    def teach(self):
        return random.choice(self.knowledge)


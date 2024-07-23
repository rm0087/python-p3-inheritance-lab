#!/usr/bin/env python

from user import User

class Student(User):
    

    def learn(self, knowledge):
        self._knowledge.append(knowledge)
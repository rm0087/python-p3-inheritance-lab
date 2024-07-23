#!/usr/bin/env python

class User:
    def __init__(self, first_name, last_name,knowledge=[]):
        self.first_name = first_name
        self.last_name = last_name
        self.knowledge = knowledge

    @property ##knowledge.getter
    def knowledge(self):
        return self._knowledge

    @knowledge.setter
    def knowledge(self, knowledge):
        self._knowledge = knowledge

    def learn(self, knowledge):
        self._knowledge.append(knowledge)
        

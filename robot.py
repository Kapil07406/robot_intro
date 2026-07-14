# Robot Introduction

class Robot:

    def __init__(self, name, purpose):
        self.name = name
        self.purpose = purpose

    def introduce(self):
        print("Hello!")
        print("My name is", self.name)
        print("My purpose is", self.purpose)

robot1 = Robot("RoboX", "Teaching Python")
robot2 = Robot("HelperBot", "Helping Students")

robot1.introduce()

print()

robot2.introduce()
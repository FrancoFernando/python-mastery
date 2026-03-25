# Exercise 41: A Bigger Bowl

## Description

Implement BigBowl for this exercise, such that the only difference between it and the Bowl class we created earlier is that it can have five scoops, rather than three. And yes, this means that you should use inheritance to achieve this goal. You can modify Scoop and Bowl if you must, but such changes should be minimal and justifiable.

## Learning

- inerithance syntax class Derived(Base):
- self.variable_name looks up the attribute on the instance first; if not found, falls back to the class attribute. So if an individual instance overrides variable_name, it uses that value.
- class_name.variable_name always reads the class attribute directly, ignoring any per-instance override
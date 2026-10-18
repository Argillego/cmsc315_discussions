# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview
This project demonstrates object-oriented programming in Python through a
smart-home device simulation. A parent `Device` class and a child `SmartDevice`
class model inheritance and method overriding, while dedicated functions
demonstrate class/instance namespaces and the difference between shallow and
deep copying.

## Implementation Summary
- **Device (parent class):** I implemented a class variable `category`, a
  constructor with two instance variables (`name`, `status`), an event `log`
  list, and a `describe()` method that returns the device's information.
- **SmartDevice (child class):** I extended `Device` using inheritance,
  added a `network` class variable and two new instance variables
  (`firmware`, `schedule`), implemented a new `sync()` method, and overrode
  `describe()` to display the extended details. The child constructor called
  `super().__init__()` to reuse the parent's initialization logic.
- **Namespace demonstration:** I created two `SmartDevice` objects, accessed
  the `network` class variable through both the class and an instance, added
  a `location` attribute to only one object after creation, and displayed each
  object's `__dict__` alongside the class namespace. The output showed that
  instance namespaces are independent while class variables are shared.
- **Copy demonstration:** I created a device containing a nested mutable list,
  produced a shallow copy (`copy.copy()`) and a deep copy (`copy.deepcopy()`),
  and modified the original's nested data. The shallow copy's list changed
  along with the original because both share the same inner list, while the
  deep copy remained fully independent.
- **Main function:** I created and tested a parent object and a child object
  (demonstrating inherited and overridden behavior), then called both
  demonstration functions with labeled output.

## Student-Created Extension
I added a `reset()` method to the parent `Device` class that restores the
device's status to standby and clears its event log, and I overrode it in
`SmartDevice` so a smart device also clears its schedule when reset. To test
the extension, I gave a device a status of `"active"` and a non-empty log,
called `reset()`, and printed its state to confirm both the parent and child
versions restored their respective attributes correctly.

## Reflection
Completing this assignment taught me how Python classes organize state and
behavior: class variables live in the class namespace and are shared, while
instance variables live in each object's own `__dict__`. The hardest challenge
was the copying demonstration — I initially assumed `copy.copy()` produced a
fully independent object, but the shallow copy's nested list changed when I
modified the original, which only `deepcopy()` prevented. Comparing OOP to
procedural programming, OOP bundles data with behavior, so `SmartDevice` could
extend `Device` without touching tested code — something procedural duplication
makes difficult. That improves maintainability and reusability, though it adds
overhead: more structure and indirection than a small script needs. For real
applications, that trade-off pays off as systems grow.
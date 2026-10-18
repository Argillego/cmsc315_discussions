"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================
"""

from copy import copy, deepcopy


# TODO 1: Parent class — class variable, constructor, two instance
# variables, and an information method.
class Device:
    """Parent class representing a generic smart-home device."""
    category = "General Device"          # class variable (shared by all)

    def __init__(self, name, status="standby"):
        self.name = name                 # instance variable 1
        self.status = status             # instance variable 2
        self.log = []                    # nested mutable data (for copy demo)

    def describe(self):
        return f"Device: {self.name} | Status: {self.status} | Category: {Device.category}"

    def add_log(self, entry):
        self.log.append(entry)

    def reset(self):
        """Extension: restore default status and clear the event log."""
        self.status = "standby"
        self.log = []
        return f"{self.name} has been reset."


# TODO 2: Child class — inherits, adds a class variable, two new
# instance variables, a new method, and overrides describe().
class SmartDevice(Device):
    """Child class adding connectivity features."""
    network = "HomeMesh-WiFi"            # new class variable

    def __init__(self, name, status="standby", firmware="v1.0"):
        super().__init__(name, status)   # reuse parent constructor
        self.firmware = firmware         # new instance variable 1
        self.schedule = []               # new instance variable 2

    def describe(self):                  # override of parent method
        return (f"Smart Device: {self.name} | Status: {self.status} | "
                f"Firmware: {self.firmware} | Network: {SmartDevice.network}")

    def sync(self):                      # new method
        return f"{self.name} synced with {SmartDevice.network}"

    def reset(self):
        """Extension override: reset like a Device, plus clear the schedule."""
        parent_message = super().reset()
        self.schedule = []
        return f"{parent_message} Schedule cleared."


# TODO 3: Namespace demonstration
def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")
    t1 = SmartDevice("Thermostat")
    t2 = SmartDevice("Security Camera")

    print("Class variable via class:     ", SmartDevice.network)
    print("Class variable via object t1: ", t1.network)
    print("Same lookup — objects fall back to the class namespace.")

    t1.location = "Living Room"          # new attribute on ONE object, after creation
    print("\nAdded t1.location = 'Living Room' AFTER creation.")
    print("t1.__dict__:", t1.__dict__)
    print("t2.__dict__:", t2.__dict__)
    print("Only t1's namespace has 'location' — instance namespaces are independent.")

    print("\nClass namespace (SmartDevice.__dict__):", SmartDevice.__dict__)
    print("Note: 'location' is not here; the class namespace holds network, methods, etc.")


# TODO 4: Shallow vs. deep copy demonstration
def demonstrate_copying():
    print("\n=== Copy Demonstration ===")
    original = Device("Thermostat")
    original.log.append("booted")

    shallow = copy(original)             # shallow copy — shares the nested list
    deep = deepcopy(original)            # deep copy — fully independent

    original.log.append("overheated")    # modify the original's nested data
    original.name = "Thermostat v2"

    print("Original name:", original.name, "| log:", original.log)
    print("Shallow copy: ", shallow.name, "| log:", shallow.log)
    print("Deep copy:    ", deep.name, "| log:", deep.log)
    print("\nShallow copy shares the inner list (log changed too) but got a fresh name.")
    print("Deep copy is fully independent (log and name untouched).")


# TODO 5: Main function
def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\n--- Parent object ---")
    d = Device("Door Sensor")
    print(d.describe())
    d.add_log("checked battery")
    print("Log:", d.log)

    print("\n--- Child object (inheritance + override) ---")
    s = SmartDevice("Smart Lock", "active", "v2.3")
    print(s.describe())
    print(s.sync())

    print("\n--- Extension: reset demonstration ---")
    print(s.reset())
    print("Status:", s.status, "| Log:", s.log, "| Schedule:", s.schedule)
    d.reset()
    print("Parent reset:", d.status, "| Log:", d.log)

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()
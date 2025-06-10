class Height:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches
        self.normalize()

    def normalize(self):
        if self.inches >= 12:
            self.feet += self.inches // 12
            self.inches = self.inches % 12

    def total_inches(self):
        return self.feet * 12 + self.inches

    def __str__(self):
        return f"{self.feet} feet {self.inches} inches"

    # Existing methods for <, <=, ==
    def __lt__(self, other):
        return self.total_inches() < other.total_inches()

    def __le__(self, other):
        return self.total_inches() <= other.total_inches()

    def __eq__(self, other):
        return self.total_inches() == other.total_inches()

    # New methods for >, >=, !=
    def __gt__(self, other):
        return self.total_inches() > other.total_inches()

    def __ge__(self, other):
        return self.total_inches() >= other.total_inches()

    def __ne__(self, other):
        return self.total_inches() != other.total_inches()
h1 = Height(4, 6)
h2 = Height(4, 5)
h3 = Height(4, 5)
h4 = Height(5, 9)
h5 = Height(5, 10)

print(h1 > h2)   # Expected: True
print(h2 >= h3)  # Expected: True
print(h4 != h5)  # Expected: True

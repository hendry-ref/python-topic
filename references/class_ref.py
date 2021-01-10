class Student:
    def __init__(self, name, gpa, is_human):
        self.name = name
        self.gpa = gpa
        self.is_human = is_human

    def is_pass(self):
        return self.gpa >= 3.0


def instance_topic():
    st1 = Student("hendry", 4.0, True)
    st2 = Student("george", 2.2, False)
    print(f"{st1.name} has gpa of {st1.gpa}, is pass = {st1.is_pass()}")
    print(f"{st2.name} has gpa of {st2.gpa}, is pass = {st2.is_pass()}")


def main():
    instance_topic()


if __name__ == "__main__":
    main()

class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


person_a = Person("Rakibul", "Bashar", None)
person_b = Person("Abul", "Bashar", person_a)
person_c = Person("Bashir", "Uddin", person_b)


def print_depth(input_data, start=1):
    if isinstance(input_data, Person):
        obj_details(input_data, start)
        if isinstance(input_data.father, Person):
            print_depth(input_data.father, start + 1)

    elif isinstance(input_data, dict):
        for key in input_data:
            print(f"{key} {start}")
            if isinstance(input_data[key], object):
                print_depth(input_data[key], start + 1)


def obj_details(person, start):
    listOffields = ["first_name", "last_name", "father"]
    for fieldkey in listOffields:
        print(f"{getattr(person, fieldkey)}: {start}")


a = {
    "key1": 1,
    "key2": {
        "key3": 1,
        "key4": {
            "key5": 4,
            "user": person_c,
        }
    },
}

print_depth(a)

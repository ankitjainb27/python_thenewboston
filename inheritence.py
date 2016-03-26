class Parent():
    def print_last_name(self):
        print 'Roberts'


class Child(Parent):
    def print_first_name(self):
        print 'Bucky'

    def print_last_name(self):
        print 'Snitzlberg'

bucky = Child()
bucky.print_first_name()
bucky.print_last_name()

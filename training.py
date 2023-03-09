class A:
    a: int = 10

    def show_a(self):
        print(f'a is: {self.a}')

    @classmethod
    def show_real_a(cls):
        print(f'real a is: {cls.a}')


obj_1 = A()
obj_2 = A()

# что будет выводить метод show_a() для каждого из объектов?
obj_1.show_a()  # 10
obj_2.show_a()  # 10
print('Do some fancy staff')
A.a = 20

# что будет выводить метод show_a() для каждого из объектов?
obj_1.show_a()  # 20
obj_2.show_a()  # 20
print('Do some fancy staff')
obj_1.a = 30

# что будет выводить метод show_a() для каждого из объектов?
obj_1.show_a()  # 30
obj_2.show_a()  # 20
print('Do some fancy staff')
A.a = 40

# что будет выводить метод show_a() для каждого из объектов?
obj_1.show_a()  # 30
obj_2.show_a()  # 40

# что будет выводить метод show_real_a() для каждого из объектов?
obj_1.show_real_a()  # 40
obj_2.show_real_a()  # 40

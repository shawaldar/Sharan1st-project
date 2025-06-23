class A:
    def function_one(self):
        print('class A function one')
    def function_two(self):
        print('class A function two')
class B(A):
    def function_two(self):
        super().function_two()
        print('class B function two')
    def function_three(self):
        print('class B function three')
one=B()
one.function_one()
one.function_two()
one.function_three()




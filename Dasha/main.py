import time

class A:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)

class B(A):
    def __init__(self, name):
        super().__init__(name)

class C(B):
    def __init__(self, name):
        super().__init__(name)

model_1 = A("a")
model_2 = B("b")
model_3 = C("c")

for i in [model_1, model_2, model_3]:
    i.show()

time.sleep(50)
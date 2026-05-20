class Base:
    def __init__(self, x):
        print("Inside class Base constructor, value is ", x)

class Derived(Base):
    def __init__(self):
        super().__init__(100)
        print("Inside class Derived constructor")


if __name__ == "__main__":
    obj = Derived()

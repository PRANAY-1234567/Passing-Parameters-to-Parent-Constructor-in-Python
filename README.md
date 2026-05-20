# 🧬 Passing Parameters to Parent Constructor in Python

## 📌 Description

This Python program demonstrates how a child class can pass arguments to a parent class constructor using the `super()` function.

When an object of `Derived` is created:

1. `Derived` constructor executes
2. It calls the parent (`Base`) constructor with value `100`
3. Parent constructor prints the value
4. Control returns to child constructor

---

## 🚀 Features

* Demonstrates inheritance
* Uses parameterized constructor
* Passes arguments using `super()`
* Shows constructor execution flow

---

## 🛠️ How It Works

### 1️⃣ Parent Class – `Base`

Contains parameterized constructor:

```python id="m7q2pl"
def __init__(self, x)
```

Prints:

```python id="r4m8zx"
Inside class Base constructor, value is 100
```

---

### 2️⃣ Child Class – `Derived`

```python id="n9x3qa"
class Derived(Base)
```

Uses:

```python id="k5m1pt"
super().__init__(100)
```

👉 Calls parent constructor and passes value `100`.

Then prints:

```python id="p2q7mv"
Inside class Derived constructor
```

---

## 💻 Code

```python id="x6m8pl"
class Base:
    def __init__(self, x):
        print("Inside class Base constructor, value is", x)


class Derived(Base):
    def __init__(self):
        super().__init__(100)
        print("Inside class Derived constructor")


if __name__ == "__main__":
    obj = Derived()
```

---

## ▶️ Output

```id="v3m9qa"
Inside class Base constructor, value is 100
Inside class Derived constructor
```

---

## 🧠 Key Concepts

### ✔ Parameterized Parent Constructor

Parent constructor requires:

```python id="a8q4zx"
x
```

---

### ✔ Passing Arguments with `super()`

```python id="j1m7pl"
super().__init__(100)
```

👉 Sends value to parent constructor.

---

### ✔ Constructor Execution Flow

```text id="w5q2mv"
Derived()
   ↓
Base(100)
   ↓
Derived()
```

---

## 📚 Concepts Used

* Inheritance
* Parameterized constructor
* Constructor chaining
* `super()` method

---

## ⚠️ Important Note

If you write:

```python id="d4m8qa"
super().__init__()
```

❌ Error occurs because `Base` constructor expects parameter `x`.

---

## 🎯 Why This is Important

Used in:

* Real-world OOP systems
* Framework development
* GUI applications
* Parent-child object initialization

---

## 🔧 Future Improvements

* Accept user input for `x`
* Add multilevel inheritance
* Store values as instance variables
* Demonstrate overriding with parameters

---

## 📄 License

This project is open-source and free to use.

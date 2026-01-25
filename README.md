<!-- Center-aligned Header -->
<div align="center">
  <h1>🐍 Python Object-Oriented Programming (OOP)</h1>
  <p><i>A comprehensive guide to mastering Classes, Objects, and OOP principles in Python.</i></p>
  
  <!-- GitHub Badges -->
  
</div>

<hr>

## 📖 Introduction
This repository covers the fundamental and advanced concepts of **Object-Oriented Programming** in Python. 

### 🚀 Core Concepts Included:
1. **Classes & Objects**: The blueprints and their instances.
2. **Encapsulation**: Keeping data safe within classes.
3. **Inheritance**: Reusing code by creating child classes.
4. **Polymorphism**: Using a single interface for different data types.

<hr>

## 💻 Sample Project: Student Management
<details>
<summary><b>Click to expand the Student Class code</b></summary>

```python
class Student:
    def __init__(self, name, mark1, mark2, mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def avg(self):
        """Calculates the average of three marks."""
        return (self.mark1 + self.mark2 + self.mark3) / 3

# Usage
s1 = Student("Alice", 85, 90, 88)
print(f"{s1.name}'s Average: {s1.avg():.2f}")

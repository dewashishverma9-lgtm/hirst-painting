# 🎨 Hirst-Style Dot Painting

A Python Turtle Graphics project that generates a colorful **Hirst-style dot painting** using a custom RGB color palette and randomized colors.

This project was built to practice **Python loops, nested loops, functions from the Turtle module, RGB colors, randomness, and basic graphics programming**.

## 🖼️ Project Preview

The program creates a grid of colorful dots, with each dot randomly assigned a color from the predefined RGB palette.

## 🚀 Features

* 🎨 Randomly selects colors from an RGB palette
* 🐢 Uses Python's `turtle` module for drawing
* 🔄 Uses nested loops to create the dot pattern
* 🌈 Supports RGB colors using Turtle's `colormode(255)`
* 📐 Generates a structured grid automatically
* ⚡ Creates a different color arrangement each time the program runs

## 🛠️ Technologies Used

* **Python 3**
* **Turtle Graphics**
* **Random Module**
* **RGB Color System**

## 📂 Project Structure

```text
Hirst-Painting/
│
├── main.py
└── README.md
```

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Open the project

Open the project in **PyCharm** or any Python IDE.

### 3. Run the program

```bash
python main.py
```

A Turtle graphics window will open and generate the dot painting.

## 🧠 Concepts Practiced

This project helped me practice:

* `for` loops
* Nested loops
* `random.choice()`
* Tuples
* Lists
* RGB color values
* `turtle.Turtle()`
* `penup()`
* `forward()`
* `left()` and `right()`
* `dot()`
* Screen configuration

## 🎯 How It Works

The program stores a collection of RGB color values:

```python
colour_list = [
    (240, 242, 246),
    (193, 160, 123),
    (73, 92, 124),
    ...
]
```

For every dot, a random color is selected:

```python
tut.pencolor(random.choice(colour_list))
```

The Turtle then moves across the screen and changes direction at the end of each row to create the grid pattern.

## 📚 What I Learned

Through this project, I learned how to:

* Work with RGB colors in Python Turtle
* Generate randomized visual patterns
* Use nested loops for structured repetition
* Control Turtle movement programmatically
* Combine randomness with deterministic patterns to create graphics

## 🔮 Possible Improvements

Future improvements could include:

* Extracting colors automatically from an input image using `colorgram`
* Allowing users to choose the grid size
* Allowing users to choose dot size and spacing
* Adding an image-based color palette
* Creating different geometric patterns

## 👨‍💻 Author

**Dewashish Verma**

Building Python projects while developing practical programming and problem-solving skills.

---

⭐ If you found this project interesting, consider giving the repository a star!

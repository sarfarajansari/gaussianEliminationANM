
# Gauss Elimination - Streamlit App 🔢

This app implements the **Gauss Elimination** method to solve systems of linear equations of the form \( AX = B \), where \( A \) is a coefficient matrix, \( X \) is the variable matrix, and \( B \) is the result matrix. The app allows users to input matrices for \( A \) and \( B \), and then solves for \( X \) step-by-step using the Gauss Elimination algorithm.

> **Note**: I built this app while learning **Applied Numerical Methods** during my college studies. It was a great way to apply theoretical concepts into a practical tool!



https://github.com/user-attachments/assets/86dc95af-9733-4df8-97a1-4ff32a75ca41


## Features

- **Input Matrices**: Users can input matrix \( A \) and vector \( B \) for the system of equations.
- **Gauss Elimination Solver**: The app solves the system using the Gauss Elimination method and displays the solution matrix \( X \).
- **Step-by-Step Process**: Users can see the algorithm’s step-by-step process to understand how the solution is reached.

## Tech Stack

- **Streamlit**: A framework for building interactive web applications in Python.
- **NumPy**: For matrix manipulation and numerical operations.
- **Python**: The primary programming language.

## How to Run

1. Clone or download the repository:
   ```bash
   git clone https://github.com/yourusername/gaussianEliminationANM.git
   cd gaussianEliminationANM
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

4. The app will open in your web browser, where you can input matrices and solve the system of equations.

## Usage

- **Input the Matrix \( A \)**: Enter the elements of the coefficient matrix.
- **Input the Matrix \( B \)**: Enter the result vector.
- **Click "Solve"**: The app will display the solution matrix \( X \) along with the intermediate steps of the Gauss Elimination process.

## Why This Project?

I created this app as a learning tool during my **Applied Numerical Methods** course in college. The project helped me deepen my understanding of numerical methods and linear algebra while providing a user-friendly way for others to explore Gauss Elimination.


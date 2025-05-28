Sure! Here's a polished and professional `README.md` for your project:

---

# 🍪 Food Calorie Analyzer

A lightweight Python-based tool that takes in a recipe and calculates the calorie breakdown of each ingredient. Perfect for anyone looking to analyze the nutritional content of home-cooked meals.

---

## 📁 Project Structure

```
├── App.py                         # Main script for calorie calculation
├── Food.ipynb                     # Jupyter notebook for interactive exploration
├── recipe.csv                    # Input recipe with ingredient names and amounts
├── recipe_calorie_breakdown.csv  # Output file with calories per ingredient
└── .idea/                         # IntelliJ/PyCharm project configuration
```

---

## 🧠 How It Works

1. **Input File (`recipe.csv`)**
   Contains a list of ingredients and their respective amounts in common kitchen units (e.g., cups, tsp).

2. **Calorie Lookup Logic (`App.py`)**
   Parses the recipe file, estimates calorie values using known approximations (e.g., 64 cal per tbsp of honey), and aggregates totals.

3. **Output File (`recipe_calorie_breakdown.csv`)**
   Includes calories per unit, total calories, and the adjusted calorie count per ingredient.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/NathanG1en/Food.git
cd Food
```

### 2. Install Dependencies

This project only requires standard Python libraries like `pandas`. You can install them via:

```bash
pip install pandas
```

### 3. Run the Script

```bash
python App.py
```

This will read `recipe.csv`, perform the calculations, and output `recipe_calorie_breakdown.csv`.

---

## 📊 Example Output

| Ingredient              | Amount           | Calories per Unit          | Total Calories |
| ----------------------- | ---------------- | -------------------------- | -------------- |
| White whole wheat flour | 2 cups (\~240g)  | \~110 cal per 30g          | 816            |
| Honey                   | 1/3 cup (\~113g) | \~64 cal per tbsp (\~15g)  | 343            |
| Coconut oil             | 1/4 cup (\~55g)  | \~117 cal per tbsp (\~15g) | 486            |
| ...                     | ...              | ...                        | ...            |

---

## 🛠 Developer Notes

* Built using Python 3.x
* Optimized for use with PyCharm (project files under `.idea/`)
* Notebook (`Food.ipynb`) included for experimentation or visualization

---

## 📌 TODOs / Future Improvements

* Automate unit conversion (e.g., cups to grams)
* Integrate with the [USDA FoodData Central API](https://fdc.nal.usda.gov/)
* Add macro breakdown (fat, protein, carbs)
* Build a Streamlit UI

---

## 🧑‍🍳 Inspiration

Designed for home chefs, food bloggers, and nutrition enthusiasts who want quick, interpretable calorie feedback from their favorite recipes.

---

## 📄 License

MIT License. See `LICENSE` for details.

---

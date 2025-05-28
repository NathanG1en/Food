import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Define Edamam API credentials
API_ID = os.getenv("EDAMAM_API_ID")
API_KEY = os.getenv("EDAMAM_API_KEY")
URL = 'https://api.edamam.com/api/nutrition-details'


# Function to analyze recipe
def analyze_recipe(ingredients):
    data = {
        "title": "Recipe Analysis",
        "ingr": ingredients
    }
    response = requests.post(f"{URL}?app_id={API_ID}&app_key={API_KEY}", json=data)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Error: Could not retrieve nutritional data.")
        return None


# Compliance check
def check_compliance_per_serving(nutritional_data, servings):
    total_calories = nutritional_data.get('calories', 0)
    sodium = nutritional_data['totalNutrients'].get('NA', {}).get('quantity', 0)
    total_fat = nutritional_data['totalNutrients'].get('FAT', {}).get('quantity', 0)
    saturated_fat = nutritional_data['totalNutrients'].get('FASAT', {}).get('quantity', 0)
    trans_fat = nutritional_data['totalNutrients'].get('FATRN', {}).get('quantity', 0)
    total_sugars = nutritional_data['totalNutrients'].get('SUGAR', {}).get('quantity', 0)
    recipe_weight = nutritional_data.get('totalWeight', 0)

    # Per-serving values
    calories_per_serving = total_calories / servings
    sodium_per_serving = sodium / servings
    total_fat_per_serving = total_fat / servings
    saturated_fat_per_serving = saturated_fat / servings
    trans_fat_per_serving = trans_fat / servings
    total_sugars_per_serving = total_sugars / servings
    weight_per_serving = recipe_weight / servings

    # Compliance results
    compliance = {
        'Calories': calories_per_serving <= 200,
        'Sodium': sodium_per_serving <= 200,
        'Total Fat': (total_fat_per_serving * 9) <= 0.35 * calories_per_serving,
        'Saturated Fat': (saturated_fat_per_serving * 9) < 0.1 * calories_per_serving,
        'Trans Fat': trans_fat_per_serving <= 0.05,
        'Total Sugars': total_sugars_per_serving <= 0.35 * weight_per_serving
    }
    return compliance, {
        'Calories': calories_per_serving,
        'Sodium': sodium_per_serving,
        'Total Fat': total_fat_per_serving,
        'Saturated Fat': saturated_fat_per_serving,
        'Trans Fat': trans_fat_per_serving,
        'Total Sugars': total_sugars_per_serving
    }


# Streamlit App UI
st.title("Nutritional Compliance Checker")
st.header("Check if your recipe meets USDA Smart Snack guidelines")

# User input for ingredients
st.subheader("Enter Ingredients")
ingredients_input = st.text_area("Enter each ingredient on a new line, e.g., '2 cups white whole wheat flour'")

# User input for servings
servings = st.number_input("Enter number of servings")

# Analyze button
if st.button("Analyze Recipe"):
    # Parse ingredients
    ingredients_list = [line.strip() for line in ingredients_input.split("\n") if line.strip()]

    if ingredients_list:
        # Call API and analyze
        nutritional_data = analyze_recipe(ingredients_list)

        if nutritional_data:
            # Check compliance
            compliance_results, per_serving_values = check_compliance_per_serving(nutritional_data, servings)

            st.subheader("Per Serving Nutritional Values")
            for key, value in per_serving_values.items():
                st.write(f"{key}: {value:.2f}")

            st.subheader("Compliance Check")
            for nutrient, compliant in compliance_results.items():
                st.write(f"{nutrient}: {'✅ Meets Guidelines' if compliant else '❌ Exceeds Guidelines'}")
    else:
        st.warning("Please enter at least one ingredient.")

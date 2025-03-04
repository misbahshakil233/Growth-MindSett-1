import streamlit as st

# Streamlit App Title
st.title("🔄 Unit Converter App")

# Unit Categories
categories = {
    "Length": ["Meters", "Kilometers", "Miles", "Feet"],
    "Weight": ["Grams", "Kilograms", "Pounds", "Ounces"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"]
}

# Select Category
category = st.selectbox("Select Conversion Type:", list(categories.keys()), index=0)

# Select Units
unit_from = st.selectbox("From:", categories[category])
unit_to = st.selectbox("To:", categories[category])

# User Input
value = st.number_input("Enter Value:", min_value=0.0, format="%.2f")

# Conversion Logic
def convert(value, unit_from, unit_to):
    if category == "Length":
        length_conversion = {
            "Meters": 1, "Kilometers": 0.001, "Miles": 0.000621371, "Feet": 3.28084
        }
        return value * (length_conversion[unit_to] / length_conversion[unit_from])

    elif category == "Weight":
        weight_conversion = {
            "Grams": 1, "Kilograms": 0.001, "Pounds": 0.00220462, "Ounces": 0.035274
        }
        return value * (weight_conversion[unit_to] / weight_conversion[unit_from])

    elif category == "Temperature":
        if unit_from == "Celsius":
            return (value * 9/5 + 32) if unit_to == "Fahrenheit" else value + 273.15
        elif unit_from == "Fahrenheit":
            return (value - 32) * 5/9 if unit_to == "Celsius" else (value - 32) * 5/9 + 273.15
        elif unit_from == "Kelvin":
            return value - 273.15 if unit_to == "Celsius" else (value - 273.15) * 9/5 + 32

    return value  # Default case

# Convert Button
if st.button("Convert"):
    result = convert(value, unit_from, unit_to)
    output_text = f"{value} {unit_from} is equal to {result:.2f} {unit_to}"
    
    # Display result
    st.success(f"✅ {output_text}")

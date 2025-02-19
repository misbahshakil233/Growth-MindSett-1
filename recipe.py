import streamlit as st

# Recipe images mapping
recipe_images = {
    "Biryani": "https://th.bing.com/th/id/R.a93cc12229bc372738290a1f92d3f5d4?rik=up%2fiBpYCxmDIww&pid=ImgRaw&r=0",
    "Nihari": "https://thumbs.dreamstime.com/b/nihari-nehari-special-meat-stew-prepared-mutton-buffalo-meat-popular-pakistan-india-nihari-nehari-249956871.jpg",
    "Karahi": "https://hinzcooking.com/wp-content/uploads/2020/12/chicken-karahi-recipe.jpg",
    "Haleem": "https://thumbs.dreamstime.com/b/haleem-pakistani-dish-black-background-269951630.jpg",
    "Samosa": "https://th.bing.com/th/id/R.8337cb8ad6be8e0e9486fd137c0f1166?rik=SYNbq3t4E5%2fMgw&pid=ImgRaw&r=0"
}

# Karachi Famous Recipes Database
recipes = {
    "Biryani": ["Chicken", "Rice", "Tomato", "Yogurt", "Salt", "Chili"],
    "Nihari": ["Beef", "Ginger", "Salt", "Chili", "Yogurt", "Turmeric"],
    "Karahi": ["Chicken", "Tomato", "Ginger", "Yogurt", "Chili"],
    "Haleem": ["Lentils", "Wheat", "Beef", "Onion", "Salt", "Chili"],
    "Samosa": ["Potato", "Flour", "Salt", "Chili", "Oil"]
}

# Streamlit UI
st.set_page_config(page_title="Karachi Recipe Finder", page_icon="🍽️", layout="centered")
st.title("🍽️ Karachi Recipe Finder")
st.write("Find the best dishes you can make with your available ingredients!")

# Show Available Dishes
st.subheader("Available Dishes:")
st.markdown("**Here are some delicious Karachi dishes you can try:**")
for dish in recipes.keys():
    st.write(f"- 🍛 **{dish}**")

# User Ingredient Selection
user_ingredients = st.multiselect("Select your available ingredients:", 
                                  list(set(ingredient for recipe in recipes.values() for ingredient in recipe)),
                                  placeholder="Choose ingredients...", help="Select ingredients from the list")

# Function to Find Recipes
def find_recipes(selected_ingredients):
    suggested_recipes = []
    for recipe, ingredients in recipes.items():
        if all(item in selected_ingredients for item in ingredients):
            suggested_recipes.append(recipe)
    return suggested_recipes

# Display Results
if st.button("Find Recipes"):
    matched_recipes = find_recipes(user_ingredients)
    
    if matched_recipes:
        st.success("🎉 Yahoo! You selected the correct ingredients for this dish! 🎉")
        st.subheader("You can cook the following dishes:")
        
        for r in matched_recipes:
            st.markdown(f"### 🍽️ {r}")
            if r in recipe_images:
                st.image(recipe_images[r], caption=r, use_container_width=True)
            st.write("---")  # Divider for better UI
    
    else:
        st.warning("⚠️ No matching recipe found. Try selecting more ingredients or check the available dishes!")

# Run app using: streamlit run filename.py

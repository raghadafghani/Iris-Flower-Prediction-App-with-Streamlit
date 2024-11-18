
import streamlit as st
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

# Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target
target_names = iris.target_names

# Machine learning model
clf = RandomForestClassifier(random_state=42)
clf.fit(iris.data, iris.target)

# Sidebar for user input
st.sidebar.title("Iris Flower Predictor")
st.sidebar.markdown("Adjust the values below to predict the flower type:")

# Sliders for feature inputs
sepal_length = st.sidebar.slider("Sepal length (cm)", 
    float(df["sepal length (cm)"].min()), 
    float(df["sepal length (cm)"].max()), 
    float(df["sepal length (cm)"].mean())
)
sepal_width = st.sidebar.slider("Sepal width (cm)", 
    float(df["sepal width (cm)"].min()), 
    float(df["sepal width (cm)"].max()), 
    float(df["sepal width (cm)"].mean())
)
petal_length = st.sidebar.slider("Petal length (cm)", 
    float(df["petal length (cm)"].min()), 
    float(df["petal length (cm)"].max()), 
    float(df["petal length (cm)"].mean())
)
petal_width = st.sidebar.slider("Petal width (cm)", 
    float(df["petal width (cm)"].min()), 
    float(df["petal width (cm)"].max()), 
    float(df["petal width (cm)"].mean())
)

# Predict button
if st.sidebar.button("Predict Iris Flower Type"):
    # Prediction
    user_input = [[sepal_length, sepal_width, petal_length, petal_width]]
    prediction = clf.predict(user_input)
    prediction_name = target_names[prediction[0]]
    
    # Prediction probability
    prediction_proba = clf.predict_proba(user_input)
    max_proba = np.max(prediction_proba) * 100
    
    # Main UI
    st.title("Iris Flower Prediction App")
    st.write("This app predicts the type of Iris flower based on user input.")
    
    st.write("### Your Input")
    st.write(f"Sepal Length: {sepal_length} cm")
    st.write(f"Sepal Width: {sepal_width} cm")
    st.write(f"Petal Length: {petal_length} cm")
    st.write(f"Petal Width: {petal_width} cm")
    
    st.write("### Prediction")
    st.write(f"The predicted Iris flower type is: **{prediction_name}**")
    st.write(f"Confidence: {max_proba:.2f}%")
    
    # Feature importance visualization
    st.write("### Feature Importance")
    feature_importance = pd.DataFrame({
        'Feature': iris.feature_names,
        'Importance': clf.feature_importances_
    }).sort_values('Importance', ascending=False)
    
    st.bar_chart(feature_importance.set_index('Feature'))
else:
    st.write("Adjust the sliders and click 'Predict Iris Flower Type' to see the prediction.")

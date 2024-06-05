import streamlit as st
import joblib

# Load the trained model
model = joblib.load('model.pkl')

# Function to make predictions
def predict(open_price, high_price, low_price, volume):
    input_data = [[open_price, high_price, low_price, volume]]
    prediction = model.predict(input_data)
    return prediction[0]

def main():
    st.title("Stock Price Prediction")

    # Input fields for the model
    open_price = st.number_input("Open Price", min_value=0.0, format="%f")
    high_price = st.number_input("High Price", min_value=0.0, format="%f")
    low_price = st.number_input("Low Price", min_value=0.0, format="%f")
    volume = st.number_input("Volume", min_value=0.0, format="%f")

    if st.button("Predict Close Price"):
        # Ensure all inputs are provided
        if open_price and high_price and low_price and volume:
            close_price = predict(open_price, high_price, low_price, volume)
            st.success(f"The predicted close price is {close_price}")
        else:
            st.error("Please enter all the required fields")

if __name__ == "__main__":
    main()

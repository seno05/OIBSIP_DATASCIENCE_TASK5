# Step 1: Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Step 2: Load dataset
data = pd.read_csv("Advertising.csv")

# Step 3: Remove unnecessary column
data = data.drop(columns=["Unnamed: 0"])

# Step 4: Define features and target
X = data[['TV', 'Radio', 'Newspaper']]
y = data['Sales']

# Step 5: Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 6: Create model
model = LinearRegression()

# Step 7: Train model
model.fit(X_train, y_train)

# Step 8: Predict test data
predictions = model.predict(X_test)

# Step 9: Evaluate model
error = mean_absolute_error(y_test, predictions)
print("Mean Absolute Error:", error)

# Step 10: Predict new sales
new_ad = [[230.1, 37.8, 69.2]]
predicted_sales = model.predict(new_ad)

print("Predicted Sales:", predicted_sales[0])
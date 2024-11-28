import pandas as pd
import os
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

# Load the dataset
file_path = os.path.join(os.path.dirname(__file__), "Iris.csv")
data = pd.read_csv(file_path)

# Drop the 'Id' column
data = data.drop(columns=['Id'])

# Normalize the numeric columns
scaler = MinMaxScaler()
numeric_columns = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
data[numeric_columns] = scaler.fit_transform(data[numeric_columns])

# Encode the 'Species' column
encoder = LabelEncoder()
data['Species'] = encoder.fit_transform(data['Species'])

# Save the preprocessed file
preprocessed_file_path = 'preprocessed_iris.csv'
data.to_csv(preprocessed_file_path, index=False)

print(f"Preprocessed data saved to {preprocessed_file_path}")

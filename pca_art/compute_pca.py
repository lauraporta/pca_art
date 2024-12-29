import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import CountVectorizer

# Load your dataset
data = pd.read_csv('docs/data/dataset.csv')

# Process "palette" and "materials" columns
def process_list_column(column):
    vectorizer = CountVectorizer(tokenizer=lambda x: x.split(", "), binary=True)
    return vectorizer.fit_transform(column.fillna("")).toarray(), vectorizer.get_feature_names_out()

palette_features, palette_names = process_list_column(data['palette'])
materials_features, materials_names = process_list_column(data['materials'])

palette_df = pd.DataFrame(palette_features, columns=[f"palette_{name}" for name in palette_names])
materials_df = pd.DataFrame(materials_features, columns=[f"materials_{name}" for name in materials_names])

# Process "subject" and "reference"
subject_features, subject_names = process_list_column(data['subject'])
reference_features, reference_names = process_list_column(data['reference'])

subject_df = pd.DataFrame(subject_features, columns=[f"subject_{name}" for name in subject_names])
reference_df = pd.DataFrame(reference_features, columns=[f"reference_{name}" for name in reference_names])

# Process "size"
size_dummies = pd.get_dummies(data['size'], prefix="size")

# Combine all enhanced features
enhanced_data = pd.concat([
    data.drop(columns=['palette', 'materials', 'subject', 'reference', 'size'], errors="ignore").reset_index(drop=True),
    palette_df,
    materials_df,
    subject_df,
    reference_df,
    size_dummies.reset_index(drop=True)
], axis=1)

# Normalize numeric features
numeric_features = enhanced_data.select_dtypes(include=['float64', 'int64']).drop(columns=['satisfacion'], errors='ignore')
scaler = StandardScaler()
scaled_features = scaler.fit_transform(numeric_features)

# Apply PCA
pca = PCA(n_components=2)
pca_result = pca.fit_transform(scaled_features)

# Create a DataFrame with PCA results and image filenames
pca_data = pd.DataFrame({
    'x': pca_result[:, 0],
    'y': pca_result[:, 1],
    'image': data['id'].apply(lambda x: f"photos/IMG_{x if x > 1000 else f'0{x}'}.png"),  # Ensure proper formatting
    'satisfaction': data['satisfacion']  # Add satisfaction as a separate field
})

# Save the PCA data to a JSON file
pca_data.to_json('docs/data/pca_data.json', orient='records')

print("PCA data has been saved to 'pca_data.json'.")

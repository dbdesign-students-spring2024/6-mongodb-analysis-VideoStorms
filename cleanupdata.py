import pandas as pd

data = pd.read_csv('listings.csv')

# Standardize capitalization
data['name'] = data['name'].str.title()
data['neighbourhood'] = data['neighbourhood'].str.title()

# Remove dollar signs and commas, then convert to float
data['price'] = data['price'].str.replace('$', '').str.replace(',', '').astype(float)

# Perform the filtering
data = data[(data['price'] > 0) & (data['price'] <= 10000)]

# When adding the dollar sign back, consider formatting the float to two decimal places
data['price'] = '$' + data['price'].round(2).astype(str)

# Fill missing review scores with the average score
average_score = data['review_scores_rating'].mean()
data['review_scores_rating'] = data['review_scores_rating'].fillna(average_score)

german_char_mapping = {
    'ä': 'ae', 'ö': 'oe', 'ü': 'ue',
    'Ä': 'Ae', 'Ö': 'Oe', 'Ü': 'Ue',
    'ß': 'ss', 
}

def remove_german_characters(s):
    for german_char, ascii_char in german_char_mapping.items():
        s = s.replace(german_char, ascii_char)
    return s

# Apply the function to clean up the 'neighbourhood_cleansed' column
data['neighbourhood_cleansed'] = data['neighbourhood_cleansed'].apply(remove_german_characters)


# Save the cleaned data
data.to_csv('listings_clean.csv', index=False)




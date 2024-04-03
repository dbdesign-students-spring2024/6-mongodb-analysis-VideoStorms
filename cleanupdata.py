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


# Save the cleaned data
data.to_csv('listings_clean.csv', index=False)

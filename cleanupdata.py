import pandas as pd

data = pd.read_csv('listings.csv')

# Standardize capitalization
data['name'] = data['name'].str.title()
data['neighbourhood'] = data['neighbourhood'].str.title()

# Remove unrealistic prices
data = data[(data['price'] > 0) & (data['price'] <= 10000)]

# Fill missing review scores with the average score
average_score = data['review_scores_rating'].mean()
data['review_scores_rating'].fillna(average_score, inplace=True)

# Save the cleaned data
data.to_csv('listings_clean.csv', index=False)

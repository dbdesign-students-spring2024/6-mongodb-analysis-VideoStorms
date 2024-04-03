# AirBnB MongoDB Analysis

A little assignment to practice importing and analyzing data within a MongoDB database.


## Part 1

### Data Set Report: Airbnb Listings in Vienna

#### Origin of the Data Set

The data set originates from **Inside Airbnb**, a website providing Airbnb data for cities around the world. The specific dataset for Vienna can be found at [Inside Airbnb's Vienna page](https://insideairbnb.com/get-the-data/). This dataset offers detailed information on Airbnb listings in Vienna, including descriptions, locations, prices, and reviews.

#### Data Format

The original data file is in **CSV (Comma-Separated Values)** format. CSV files are simple text files where each line represents a data record, and each field within a record is separated by a comma.

#### Raw Data Sample

Below is a sample of the first 20 rows from the dataset, showing a selection of fields to give an idea of the data structure. Note that some text in fields has been clipped to prevent line-wrapping, and not all columns are displayed due to space constraints.


| id     | listing_url                         | name                         | host_id | host_name | neighbourhood | latitude | longitude | room_type       | price | minimum_nights | number_of_reviews | last_review | reviews_per_month |
| ------ | ----------------------------------- | ---------------------------- | ------- | --------- | ------------- | -------- | --------- | --------------- | ----- | -------------- | ----------------- | ----------- | ----------------- |
| 38768  | https://www.airbnb.com/rooms/38768  | Rental unit in Vienna · ...  | ...     | ...       | ...           | ...      | ...       | Entire home/apt | ...   | ...            | ...               | ...         | ...               |
| 40625  | https://www.airbnb.com/rooms/40625  | Rental unit in Vienna · ...  | ...     | ...       | ...           | ...      | ...       | Entire home/apt | ...   | ...            | ...               | ...         | ...               |
| ...    | ...                                 | ...                          | ...     | ...       | ...           | ...      | ...       | ...             | ...   | ...            | ...               | ...         | ...               |
| 208734 | https://www.airbnb.com/rooms/208734 | Private room in Vienna · ... | ...     | ...       | ...           | ...      | ...       | Private room    | ...   | ...            | ...               | ...         | ...               |

("..." indicates clipped or omitted data.)

#### Data Problems and Scrubbing Tasks

Upon initial review, the dataset appears to be well-structured; however, common issues in such datasets that might require attention include:

1. **Missing Values**: Fields like `reviews_per_month` might contain null values, especially for listings without any reviews.
2. **Inconsistent Data**: The `name` field might contain various formats, making it challenging to extract structured information.
3. **Incorrect encoding** The `neighbourhood_cleansed` field does not handle german umlauts correctly, they are encoded improperly so they have to be fixed.
4. **Outliers**: Prices or minimum nights might have unrealistic values due to data entry errors or unique listings.

Example of a Python snippet to handle missing values:


## Part 2
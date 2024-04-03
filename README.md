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

|id    |listing_url                        |scrape_id     |last_scraped|source         |name                                                                |description|neighborhood_overview                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |picture_url                                                                                            |host_id |host_url                                  |host_name    |host_since|host_location      |host_about                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |host_response_time|host_response_rate|host_acceptance_rate|host_is_superhost|host_thumbnail_url                                                                                                              |host_picture_url                                                                                                                   |host_neighbourhood  |host_listings_count|host_total_listings_count|host_verifications              |host_has_profile_pic|host_identity_verified|neighbourhood        |neighbourhood_cleansed|neighbourhood_group_cleansed|latitude|longitude|property_type              |room_type      |accommodates|bathrooms|bathrooms_text  |bedrooms|beds|amenities|price  |minimum_nights|maximum_nights|minimum_minimum_nights|maximum_minimum_nights|minimum_maximum_nights|maximum_maximum_nights|minimum_nights_avg_ntm|maximum_nights_avg_ntm|calendar_updated|has_availability|availability_30|availability_60|availability_90|availability_365|calendar_last_scraped|number_of_reviews|number_of_reviews_ltm|number_of_reviews_l30d|first_review|last_review|review_scores_rating|review_scores_accuracy|review_scores_cleanliness|review_scores_checkin|review_scores_communication|review_scores_location|review_scores_value|license|instant_bookable|calculated_host_listings_count|calculated_host_listings_count_entire_homes|calculated_host_listings_count_private_rooms|calculated_host_listings_count_shared_rooms|reviews_per_month|
|------|-----------------------------------|--------------|------------|---------------|--------------------------------------------------------------------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|--------|------------------------------------------|-------------|----------|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|------------------|--------------------|-----------------|--------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|--------------------|-------------------|-------------------------|--------------------------------|--------------------|----------------------|---------------------|----------------------|----------------------------|--------|---------|---------------------------|---------------|------------|---------|----------------|--------|----|---------|-------|--------------|--------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------|----------------|---------------|---------------|---------------|----------------|---------------------|-----------------|---------------------|----------------------|------------|-----------|--------------------|----------------------|-------------------------|---------------------|---------------------------|----------------------|-------------------|-------|----------------|------------------------------|-------------------------------------------|--------------------------------------------|-------------------------------------------|-----------------|
|38768 |https://www.airbnb.com/rooms/38768 |20231215032838|2023-12-15  |city scrape    |Rental unit in Vienna · ★4.75 · 1 bedroom · 3 beds · 1 bath         |           |the Karmeliterviertel became very popular in the last years. It offers many new pubs and restaurants and is located next to Augarten (huge garden good for jogging), to the concert hall of Wiener Sängerknaben (muth), and has the Karmelitermarket, which is best to visit on Saturday morning to get biological products. In summer the best nightbars are at the donaukanal, which is 5 minutes away.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |https://a0.muscache.com/pictures/ad4089a3-5355-4681-96bb-e3ad70684987.jpg                              |166283  |https://www.airbnb.com/users/show/166283  |Hannes       |2010-07-14|Vienna, Austria    |I am open minded and like travelling myself. I have spent many months in Latinamerica and Asia, where I got  in touch with Indian philosophie and meditation... Now I mostly work in the field of contemporary art and I do my best to offer you a nice apartment next to the citycenter...!                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |within an hour    |100%              |100%                |f                |https://a0.muscache.com/im/users/166283/profile_pic/1435040494/original.jpg?aki_policy=profile_small                            |https://a0.muscache.com/im/users/166283/profile_pic/1435040494/original.jpg?aki_policy=profile_x_medium                            |Leopoldstadt        |3                  |3                        |['email', 'phone']              |t                   |t                     |Vienna, Austria      |Leopoldstadt          |                            |48.21924|16.37831 |Entire rental unit         |Entire home/apt|5           |         |1 bath          |        |3   |[]       |$77.00 |4             |75            |3                     |28                    |1125                  |1125                  |9.1                   |1125.0                |                |t               |12             |42             |72             |159             |2023-12-15           |384              |27                   |4                     |2011-03-23  |2023-12-14 |4.75                |4.81                  |4.65                     |4.91                 |4.94                       |4.77                  |4.7                |       |t               |3                             |3                                          |0                                           |0                                          |2.48             |
|40625 |https://www.airbnb.com/rooms/40625 |20231215032838|2023-12-15  |city scrape    |Rental unit in Vienna · ★4.85 · 2 bedrooms · 4 beds · 1 bath        |           |The neighbourhood offers plenty of restaurants and grocery shops. In the apartment you will find an area map marked with the different restaurants and shops in the area, including opening hours for your ease of reference.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |https://a0.muscache.com/pictures/11509144/d55c2742_original.jpg                                        |175131  |https://www.airbnb.com/users/show/175131  |Ingela       |2010-07-20|Vienna, Austria    |I´m originally from Sweden but have been living in Vienna for many years. I love this city and I love meeting guests from different parts of the world :-) During my travel, both privately and on duty, I have learned the importance of safe, clean and comfortable accommodation in a central location with good infrastructure. This is what I offer you with my apartments.   Most of my apartments are located in the same building right on the underground U4 Meidling Hauptstrase that connects to the city center in less than 10min, and at the same time walking distance to Palace Schönbrunn - Austria´s biggest tourist attraction.   My city centre apartment is located next to Hofburg Palace with walking distance to all the inner city attractions.  As the majority of my apartments are located in the same building it is very convenient for groups as well to stay with me. My offer spans from studio apartments of 30m2 to 3 bedroom apartments of 100m2 sleeping up to 14 persons.  Since 1 January 2015 I have been an Airbnb Super Host. This is such an honour and I will do everything I can to make YOUR stay perfect as well!!  Kind regards,  Ingela Johansson :-)|within an hour    |98%               |85%                 |t                |https://a0.muscache.com/im/users/175131/profile_pic/1279660518/original.jpg?aki_policy=profile_small                            |https://a0.muscache.com/im/users/175131/profile_pic/1279660518/original.jpg?aki_policy=profile_x_medium                            |Rudolfsheim-Fünfhaus|17                 |19                       |['email', 'phone']              |t                   |t                     |Vienna, Austria      |Rudolfsheim-Fnfhaus  |                            |48.18434|16.32701 |Entire rental unit         |Entire home/apt|6           |         |1 bath          |        |4   |[]       |$150.00|1             |180           |1                     |3                     |180                   |180                   |1.0                   |180.0                 |                |t               |19             |49             |79             |350             |2023-12-15           |202              |17                   |1                     |2010-08-04  |2023-11-19 |4.85                |4.91                  |4.88                     |4.89                 |4.94                       |4.59                  |4.72               |       |t               |15                            |14                                         |1                                           |0                                          |1.24             |
|51287 |https://www.airbnb.com/rooms/51287 |20231215032838|2023-12-15  |city scrape    |Rental unit in Vienna · ★4.66 · Studio · 2 beds · 1 bath            |           |The neighbourhood has a lot of very nice little pubs and restaurants. 200 meters away you have the karmelitermarket, which is especially great on saturday morning. Aswell I like the Augarten, which is one of the biggist gardens in Vienna and just 5 minutes away! Beautiful old buildings are around and nearby is the modern Noveltower, including a skybar at the Sofitel (Praterstraße 1) which has a terrific view above the city!                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |https://a0.muscache.com/pictures/25163038/1c4e1334_original.jpg                                        |166283  |https://www.airbnb.com/users/show/166283  |Hannes       |2010-07-14|Vienna, Austria    |I am open minded and like travelling myself. I have spent many months in Latinamerica and Asia, where I got  in touch with Indian philosophie and meditation... Now I mostly work in the field of contemporary art and I do my best to offer you a nice apartment next to the citycenter...!                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |within an hour    |100%              |100%                |f                |https://a0.muscache.com/im/users/166283/profile_pic/1435040494/original.jpg?aki_policy=profile_small                            |https://a0.muscache.com/im/users/166283/profile_pic/1435040494/original.jpg?aki_policy=profile_x_medium                            |Leopoldstadt        |3                  |3                        |['email', 'phone']              |t                   |t                     |Vienna, Austria      |Leopoldstadt          |                            |48.21778|16.37847 |Entire rental unit         |Entire home/apt|3           |         |1 bath          |        |2   |[]       |$73.00 |5             |90            |3                     |14                    |1125                  |1125                  |8.4                   |1125.0                |                |t               |12             |42             |72             |72              |2023-12-15           |370              |14                   |1                     |2011-01-27  |2023-12-09 |4.66                |4.78                  |4.52                     |4.92                 |4.95                       |4.86                  |4.59               |       |f               |3                             |3                                          |0                                           |0                                          |2.36             |
|70637 |https://www.airbnb.com/rooms/70637 |20231215032838|2023-12-15  |city scrape    |Rental unit in Vienna · ★4.77 · 1 bedroom · 2 beds · 2 shared baths |           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |https://a0.muscache.com/pictures/925691/c8c1bdd6_original.jpg                                          |358842  |https://www.airbnb.com/users/show/358842  |Elxe         |2011-01-23|Vienna, Austria    |Ich lebe in der Stadt und am Land, ich liebe es, meine Freund*innen zu treffen, zu tanzen, kochen, essen gehen, kulturell was unternehmen und ich liebe es auch, in der Natur zu sein, den Schmetterlingen lauschen, zu gärtnern, im Chor zu singen, mal im Dirndl, mal im Cocktailkleid auszugehen, Zeit mit meiner Familie zu verbringen und mit meinem Freund zu lachen und ihn necken.  * )                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |within an hour    |100%              |94%                 |t                |https://a0.muscache.com/im/pictures/user/User-358842/original/7d3fe8db-d311-496e-8430-b9bb55f8e77a.jpeg?aki_policy=profile_small|https://a0.muscache.com/im/pictures/user/User-358842/original/7d3fe8db-d311-496e-8430-b9bb55f8e77a.jpeg?aki_policy=profile_x_medium|Leopoldstadt        |4                  |4                        |['email', 'phone']              |t                   |t                     |                     |Leopoldstadt          |                            |48.2176 |16.38018 |Private room in rental unit|Private room   |2           |         |2 shared baths  |        |2   |[]       |$50.00 |2             |1000          |2                     |2                     |1000                  |1000                  |2.0                   |1000.0                |                |t               |1              |1              |1              |111             |2023-12-15           |116              |1                    |0                     |2011-03-28  |2023-01-18 |4.77                |4.74                  |4.68                     |4.8                  |4.76                       |4.81                  |4.72               |       |f               |3                             |1                                          |2                                           |0                                          |0.75             |
|75500 |https://www.airbnb.com/rooms/75500 |20231215032838|2023-12-15  |city scrape    |Rental unit in Vienna · ★4.45 · 2 bedrooms · 2 beds · 1 bath        |           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |https://a0.muscache.com/pictures/549090/b51ce46d_original.jpg                                          |400857  |https://www.airbnb.com/users/show/400857  |Sabine       |2011-02-20|Geneva, Switzerland|I am Austrian, from Salzburg, but I spent 5 years in Vienna to study. Currently I am living in Switzerland and therefore my flat is very often available for guests.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |within a day      |100%              |75%                 |f                |https://a0.muscache.com/im/pictures/user/5d5abab3-922c-45c4-add2-dda022e5c4ab.jpg?aki_policy=profile_small                      |https://a0.muscache.com/im/pictures/user/5d5abab3-922c-45c4-add2-dda022e5c4ab.jpg?aki_policy=profile_x_medium                      |                    |1                  |1                        |['email', 'phone']              |t                   |t                     |                     |Brigittenau           |                            |48.23493|16.36752 |Entire rental unit         |Entire home/apt|4           |         |1 bath          |        |2   |[]       |$85.00 |4             |90            |4                     |4                     |90                    |90                    |4.0                   |90.0                  |                |t               |9              |39             |69             |327             |2023-12-15           |12               |0                    |0                     |2011-07-20  |2019-12-01 |4.45                |4.67                  |4.67                     |4.67                 |4.67                       |4.08                  |4.42               |       |f               |1                             |1                                          |0                                           |0                                          |0.08             |
|90247 |https://www.airbnb.com/rooms/90247 |20231215032838|2023-12-15  |city scrape    |Rental unit in Vienna · ★4.85 · 1 bedroom · 2 beds · 1 bath         |           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |https://a0.muscache.com/pictures/miso/Hosting-90247/original/d53fcd96-c015-4821-966c-863a1b0e533d.jpeg |489611  |https://www.airbnb.com/users/show/489611  |Diana        |2011-04-06|Vienna, Austria    |Born in Romania and living in Vienna. I love to host international guests and to travel abroad being hosted as well. The eternal student I am always involved in learning something new. I speak Romanian, English, Spanish and German. I love good food, especially Asian cuisine and Spanish tapas.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |within an hour    |100%              |100%                |t                |https://a0.muscache.com/im/users/489611/profile_pic/1302126965/original.jpg?aki_policy=profile_small                            |https://a0.muscache.com/im/users/489611/profile_pic/1302126965/original.jpg?aki_policy=profile_x_medium                            |Neubau              |3                  |3                        |['email', 'phone']              |t                   |t                     |                     |Neubau                |                            |48.20599|16.3489  |Entire rental unit         |Entire home/apt|4           |         |1 bath          |        |2   |[]       |$128.00|1             |1125          |1                     |1                     |1125                  |1125                  |1.0                   |1125.0                |                |t               |11             |41             |57             |268             |2023-12-15           |743              |54                   |3                     |2011-04-21  |2023-11-29 |4.85                |4.92                  |4.93                     |4.91                 |4.87                       |4.82                  |4.81               |       |t               |2                             |2                                          |0                                           |0                                          |4.82             |
|98210 |https://www.airbnb.com/rooms/98210 |20231215032838|2023-12-15  |city scrape    |Rental unit in Vienna · ★4.55 · 1 bedroom · 1 bed · Shared half-bath|           |2 minutes to the old city with the subway from our street. The Naschmarkt and State Opera area is the place to be in Vienna, with many trendy restaurants, bars and galleries.<br /><br />It is ery easy to get here from the airport and train and bus stations. No taxi is needed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |https://a0.muscache.com/pictures/1757461/3938b800_original.jpg                                         |518644  |https://www.airbnb.com/users/show/518644  |Michael      |2011-04-18|Vienna, Austria    |I studied Musicology, German Literature and singing as a counter tenor, mainly Renaissance and Baroque music.  Two of my passions are cooking (Vegan, Macrobiotic, also viennese kitchen) and the city of Vienna and what it has to offer. I do yoga, jogging, walking and biking tours.  It's nice to meet all those people from all over the world and helping them through their way in Vienna. Vienna is not as famous as Paris or Londen, but has so much to offer, so many hidden interessting corners, full of history and art.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |within an hour    |90%               |75%                 |f                |https://a0.muscache.com/im/pictures/user/f5d057ee-4f72-44f1-a01a-54b7c1712dd0.jpg?aki_policy=profile_small                      |https://a0.muscache.com/im/pictures/user/f5d057ee-4f72-44f1-a01a-54b7c1712dd0.jpg?aki_policy=profile_x_medium                      |Margareten          |34                 |74                       |['email', 'phone']              |t                   |t                     |Vienna, Austria      |Margareten            |                            |48.19409|16.35857 |Private room in rental unit|Private room   |2           |         |Shared half-bath|        |1   |[]       |$50.00 |1             |180           |1                     |6                     |1125                  |1125                  |1.1                   |1125.0                |                |t               |14             |44             |74             |164             |2023-12-15           |139              |15                   |0                     |2011-05-08  |2023-09-17 |4.55                |4.62                  |4.73                     |4.76                 |4.79                       |4.81                  |4.57               |       |f               |34                            |17                                         |17                                          |0                                          |0.91             |
|109679|https://www.airbnb.com/rooms/109679|20231215032838|2023-12-15  |city scrape    |Rental unit in Vienna · ★4.87 · Studio · 4 beds · 1 bath            |           |The neighbourhood offers plenty of restaurants and grocery shops. In the apartment you will find an area map marked with the different restaurants and shops in the area, including opening hours for your ease of reference.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |https://a0.muscache.com/pictures/1982234/1fc346f2_original.jpg                                         |175131  |https://www.airbnb.com/users/show/175131  |Ingela       |2010-07-20|Vienna, Austria    |I´m originally from Sweden but have been living in Vienna for many years. I love this city and I love meeting guests from different parts of the world :-) During my travel, both privately and on duty, I have learned the importance of safe, clean and comfortable accommodation in a central location with good infrastructure. This is what I offer you with my apartments.   Most of my apartments are located in the same building right on the underground U4 Meidling Hauptstrase that connects to the city center in less than 10min, and at the same time walking distance to Palace Schönbrunn - Austria´s biggest tourist attraction.   My city centre apartment is located next to Hofburg Palace with walking distance to all the inner city attractions.  As the majority of my apartments are located in the same building it is very convenient for groups as well to stay with me. My offer spans from studio apartments of 30m2 to 3 bedroom apartments of 100m2 sleeping up to 14 persons.  Since 1 January 2015 I have been an Airbnb Super Host. This is such an honour and I will do everything I can to make YOUR stay perfect as well!!  Kind regards,  Ingela Johansson :-)|within an hour    |98%               |85%                 |t                |https://a0.muscache.com/im/users/175131/profile_pic/1279660518/original.jpg?aki_policy=profile_small                            |https://a0.muscache.com/im/users/175131/profile_pic/1279660518/original.jpg?aki_policy=profile_x_medium                            |Rudolfsheim-Fünfhaus|17                 |19                       |['email', 'phone']              |t                   |t                     |Vienna, Austria      |Rudolfsheim-Fnfhaus  |                            |48.18467|16.32795 |Entire rental unit         |Entire home/apt|5           |         |1 bath          |        |4   |[]       |$130.00|1             |180           |1                     |3                     |180                   |180                   |1.0                   |180.0                 |                |t               |0              |27             |57             |325             |2023-12-15           |135              |6                    |0                     |2012-04-02  |2023-09-23 |4.87                |4.87                  |4.91                     |4.91                 |4.92                       |4.64                  |4.81               |       |t               |15                            |14                                         |1                                           |0                                          |0.95             |
|111059|https://www.airbnb.com/rooms/111059|20231215032838|2023-12-15  |city scrape    |Rental unit in Vienna · ★4.91 · 1 bedroom · 1 bed · 1 bath          |           |The apartment is located in a quiet one-way side street in the centre of Vienna's 17th district, Hernals. Small shopping center with supermarket, restaurants, pharmacy, and bakery is about 50 m away; several shops, cafes, tobacco shop, banks and restaurants are located nearby.<br />In the neighbourhood there three parking garages (Dornerplatz, Parhameplatz, Interspar Garage Hernals) available for a long term parking (90-115 €/month), further in 20 min away with public transport there are two Park-and-Ride parkings for cheaper week (around 20€) or monthly (around 70€) parking.                                                                                                                                                                                                                                                                                                                                                                                                                                  |https://a0.muscache.com/pictures/11308805/d0d7e800_original.jpg                                        |569644  |https://www.airbnb.com/users/show/569644  |Kateryna     |2011-05-09|Vienna, Austria    |I am Kateryna and I am a Biologist. I am a real family person. In my spare time I enjoy reading, travelling, cooking - or just watching "Friends" (guess, I am a big fan) - Long story short: I am a Optimistic Realist.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |within an hour    |100%              |88%                 |f                |https://a0.muscache.com/im/users/569644/profile_pic/1342560325/original.jpg?aki_policy=profile_small                            |https://a0.muscache.com/im/users/569644/profile_pic/1342560325/original.jpg?aki_policy=profile_x_medium                            |Hernals             |2                  |2                        |['email', 'phone']              |t                   |t                     |Vienna, Austria      |Hernals               |                            |48.22042|16.33377 |Entire rental unit         |Entire home/apt|4           |         |1 bath          |        |1   |[]       |$71.00 |5             |365           |5                     |5                     |365                   |365                   |5.0                   |365.0                 |                |t               |0              |0              |0              |0               |2023-12-15           |167              |4                    |0                     |2011-06-26  |2023-04-01 |4.91                |4.95                  |4.96                     |4.97                 |4.98                       |4.67                  |4.89               |       |f               |2                             |2                                          |0                                           |0                                          |1.10             |
|114505|https://www.airbnb.com/rooms/114505|20231215032838|2023-12-15  |city scrape    |Rental unit in Vienna · ★4.88 · Studio · 4 beds · 1 bath            |           |The neighbourhood offers plenty of restaurants and grocery shops. In the apartment you will find an area map marked with the different restaurants and shops in the area, including opening hours for your ease of reference.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |https://a0.muscache.com/pictures/11536257/906555e0_original.jpg                                        |175131  |https://www.airbnb.com/users/show/175131  |Ingela       |2010-07-20|Vienna, Austria    |I´m originally from Sweden but have been living in Vienna for many years. I love this city and I love meeting guests from different parts of the world :-) During my travel, both privately and on duty, I have learned the importance of safe, clean and comfortable accommodation in a central location with good infrastructure. This is what I offer you with my apartments.   Most of my apartments are located in the same building right on the underground U4 Meidling Hauptstrase that connects to the city center in less than 10min, and at the same time walking distance to Palace Schönbrunn - Austria´s biggest tourist attraction.   My city centre apartment is located next to Hofburg Palace with walking distance to all the inner city attractions.  As the majority of my apartments are located in the same building it is very convenient for groups as well to stay with me. My offer spans from studio apartments of 30m2 to 3 bedroom apartments of 100m2 sleeping up to 14 persons.  Since 1 January 2015 I have been an Airbnb Super Host. This is such an honour and I will do everything I can to make YOUR stay perfect as well!!  Kind regards,  Ingela Johansson :-)|within an hour    |98%               |85%                 |t                |https://a0.muscache.com/im/users/175131/profile_pic/1279660518/original.jpg?aki_policy=profile_small                            |https://a0.muscache.com/im/users/175131/profile_pic/1279660518/original.jpg?aki_policy=profile_x_medium                            |Rudolfsheim-Fünfhaus|17                 |19                       |['email', 'phone']              |t                   |t                     |Vienna, Austria      |Rudolfsheim-Fnfhaus  |                            |48.18445|16.32722 |Entire rental unit         |Entire home/apt|5           |         |1 bath          |        |4   |[]       |$130.00|1             |180           |1                     |3                     |180                   |180                   |1.0                   |180.0                 |                |t               |3              |33             |63             |335             |2023-12-15           |125              |2                    |0                     |2011-06-07  |2022-12-30 |4.88                |4.9                   |4.89                     |4.96                 |4.96                       |4.71                  |4.8                |       |f               |15                            |14                                         |1                                           |0                                          |0.82             |
|121026|https://www.airbnb.com/rooms/121026|20231215032838|2023-12-15  |city scrape    |Rental unit in Vienna · ★4.96 · 1 bedroom · 2 beds · 1 bath         |           |Prater Park - one step away, Metro stations "Nestroyplatz" (U1), "Praterstern" (U1, U2) - 3 min walk, St. Stephan's cathedral (Stephansdom) - 20 min walk (2 stops metro U1), Messe Prater Wien - 10 min walk or 1 stop metro U2, UNO-city and Vienna International Center (VIC) - 3 stops metro U1. Direct train S7 to the airport from the station "Praterstern", which is on a 5 min walk from the apartment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |https://a0.muscache.com/pictures/miso/Hosting-121026/original/2b66c6ca-f6bc-48b6-921c-c052630e7b9f.jpeg|608240  |https://www.airbnb.com/users/show/608240  |Andrei       |2011-05-20|Vienna, Austria    |I have been working in a hospitality industry long and used to travel a lot, so I always look at my apartments with the eyes of a traveler and think to myself - what would make me happy at this place. :-)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |within an hour    |100%              |100%                |t                |https://a0.muscache.com/im/pictures/user/29794a45-0f93-4a91-bc79-3d14706d8263.jpg?aki_policy=profile_small                      |https://a0.muscache.com/im/pictures/user/29794a45-0f93-4a91-bc79-3d14706d8263.jpg?aki_policy=profile_x_medium                      |Leopoldstadt        |3                  |6                        |['email', 'phone']              |t                   |t                     |Vienna, Austria      |Leopoldstadt          |                            |48.2158 |16.39034 |Entire rental unit         |Entire home/apt|4           |         |1 bath          |        |2   |[]       |$104.00|3             |90            |3                     |4                     |1125                  |1125                  |3.0                   |1125.0                |                |t               |8              |35             |60             |276             |2023-12-15           |397              |44                   |2                     |2011-06-10  |2023-11-23 |4.96                |4.97                  |4.97                     |4.98                 |4.98                       |4.81                  |4.88               |       |f               |2                             |2                                          |0                                           |0                                          |2.60             |
|131628|https://www.airbnb.com/rooms/131628|20231215032838|2023-12-15  |previous scrape|Rental unit in Vienna · 2 bedrooms ·`1 bed · 1 bath                 |           |Bakerys, Viennese wine taverns (“Heurige“) within walking distance. <br />Brunnenmarkt (market with hip bars and restaurants) only a few tram stations away. <br />Just a few minutes to Wilhelminenberg and its castle (with restaurant/café and a great view), to recreation area <br />Steinhofgründe and Kuffner Sternwarte (historical observatory). <br />Various public means of transport within walking distance (underground, rapid train, 3 tram lines, buses).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |https://a0.muscache.com/pictures/35385584/a900b897_original.jpg                                        |647465  |https://www.airbnb.com/users/show/647465  |Sylvia       |2011-05-31|Vienna, Austria    |Ich bin Wienerin und freue mich darauf mit Gästen aus aller Welt zu plaudern. Bis bald in Wien!                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |N/A               |N/A               |100%                |f                |https://a0.muscache.com/im/users/647465/profile_pic/1306859399/original.jpg?aki_policy=profile_small                            |https://a0.muscache.com/im/users/647465/profile_pic/1306859399/original.jpg?aki_policy=profile_x_medium                            |Ottakring           |2                  |2                        |['email', 'phone']              |t                   |t                     |Vienna, Austria      |Ottakring             |                            |48.21543|16.30939 |Entire rental unit         |Entire home/apt|4           |         |1 bath          |        |1   |[]       |$61.00 |7             |180           |7                     |7                     |180                   |180                   |7.0                   |180.0                 |                |t               |0              |0              |0              |0               |2023-12-15           |0                |0                    |0                     |            |           |                    |                      |                         |                     |                           |                      |                   |       |f               |2                             |2                                          |0                                           |0                                          |                 |
|203707|https://www.airbnb.com/rooms/203707|20231215032838|2023-12-15  |city scrape    |Rental unit in Vienna · ★4.56 · 1 bedroom · 2 beds · 1.5 baths      |           |It hardly can get more central than here, yet here its a bit off the official tourists routes, so its more authentic and the prices accordingly.<br /><br />With building arranging from the 13th century to begining of the 20th, a strol in the neighbourhood is never boring.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |https://a0.muscache.com/pictures/2078681/0c9371e2_original.jpg                                         |518644  |https://www.airbnb.com/users/show/518644  |Michael      |2011-04-18|Vienna, Austria    |I studied Musicology, German Literature and singing as a counter tenor, mainly Renaissance and Baroque music.  Two of my passions are cooking (Vegan, Macrobiotic, also viennese kitchen) and the city of Vienna and what it has to offer. I do yoga, jogging, walking and biking tours.  It's nice to meet all those people from all over the world and helping them through their way in Vienna. Vienna is not as famous as Paris or Londen, but has so much to offer, so many hidden interessting corners, full of history and art.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |within an hour    |90%               |75%                 |f                |https://a0.muscache.com/im/pictures/user/f5d057ee-4f72-44f1-a01a-54b7c1712dd0.jpg?aki_policy=profile_small                      |https://a0.muscache.com/im/pictures/user/f5d057ee-4f72-44f1-a01a-54b7c1712dd0.jpg?aki_policy=profile_x_medium                      |Margareten          |34                 |74                       |['email', 'phone']              |t                   |t                     |Vienna, Austria      |Margareten            |                            |48.19496|16.35896 |Entire rental unit         |Entire home/apt|4           |         |1.5 baths       |        |2   |[]       |$65.00 |30            |180           |30                    |30                    |180                   |180                   |30.0                  |180.0                 |                |t               |22             |52             |82             |357             |2023-12-15           |95               |0                    |0                     |2011-08-28  |2022-06-10 |4.56                |4.59                  |4.7                      |4.82                 |4.83                       |4.84                  |4.57               |       |f               |34                            |17                                         |17                                          |0                                          |0.63             |
|138264|https://www.airbnb.com/rooms/138264|20231215032838|2023-12-15  |city scrape    |Condo in Vienna · ★5.0 · 1 bedroom · 2 beds · 1 bath                |           |Around our site you will find numerous shops and restaurants. So you do not have to cook by yourself, but can explore Viennese and international delights.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |https://a0.muscache.com/pictures/030b0d47-de12-425a-bfcb-d89fcd178a54.jpg                              |675182  |https://www.airbnb.com/users/show/675182  |Stephanie    |2011-06-07|Vienna, Austria    |We are a family run business and therefore you always have contact with us personally.  See you soon in Vienna! Stephanie & Christian                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |within an hour    |100%              |100%                |t                |https://a0.muscache.com/im/pictures/user/2e564da7-5173-41f4-ae99-2cf72aa33504.jpg?aki_policy=profile_small                      |https://a0.muscache.com/im/pictures/user/2e564da7-5173-41f4-ae99-2cf72aa33504.jpg?aki_policy=profile_x_medium                      |Hernals             |15                 |16                       |['email', 'phone', 'work_email']|t                   |t                     |Vienna, Austria      |Hernals               |                            |48.22353|16.31773 |Entire condo               |Entire home/apt|4           |         |1 bath          |        |2   |[]       |$154.00|1             |730           |1                     |5                     |730                   |730                   |1.1                   |730.0                 |                |t               |18             |48             |78             |308             |2023-12-15           |6                |1                    |0                     |2018-10-30  |2023-05-07 |5.0                 |5.0                   |5.0                      |5.0                  |5.0                        |5.0                   |4.17               |       |t               |14                            |14                                         |0                                           |0                                          |0.10             |
|482052|https://www.airbnb.com/rooms/482052|20231215032838|2023-12-15  |city scrape    |Rental unit in Vienna · ★4.57 · 1 bedroom · 2 beds · 1 bath         |           |There are many supermarkets, drugstores, pharmacies, coffee shops, tobacco shop, a post office, cash machine (ATM) nearby.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |https://a0.muscache.com/pictures/55703045/77ac39b9_original.jpg                                        |13336646|https://www.airbnb.com/users/show/13336646|Hotel Und    |2014-03-20|Vienna, Austria    |"Wir leben alle unter dem gleichen Himmel, aber wir haben nicht alle den gleichen Horizont."  Ihr bekommt bei uns nicht nur ein gemütliches, neu eingerichtetes Apartment zu fairem Preis, wir sind sogar für Euch persönlich anzutreffen. Jeden Tag von 6:00 bis 22:00 Uhr... Wir freuen uns auf Euch und würden Euch gerne eine tolle Zeit in Wien bereiten.  Wir alle sind zusammengewürfelt aus anderen Ländern und studieren die unterschiedlichsten Fächer. Wir verwalten neben dem Studium diese Apartments und es macht uns große Freude anderen die Stadt unserer Wahl näher zu bringen. Als zusammengemischtes Team aus den unterschiedlichsten Ländern haben wir auch die verschiedensten Lebensstile, Einstellungen und Blickwinkel. Es ist schön in einer solch vielfältigen Gemeinschaft zu sein!                                                                                                                                                                                                                                                                                                                                                                                       |within a day      |50%               |100%                |f                |https://a0.muscache.com/im/users/13336646/profile_pic/1395933568/original.jpg?aki_policy=profile_small                          |https://a0.muscache.com/im/users/13336646/profile_pic/1395933568/original.jpg?aki_policy=profile_x_medium                          |Penzing             |9                  |9                        |['email', 'phone', 'work_email']|t                   |t                     |Vienna, Austria      |Penzing               |                            |48.19676|16.28851 |Entire rental unit         |Entire home/apt|4           |         |1 bath          |        |2   |[]       |$144.00|1             |365           |1                     |3                     |365                   |365                   |1.0                   |365.0                 |                |t               |22             |50             |80             |355             |2023-12-15           |8                |0                    |0                     |2012-08-03  |2022-09-25 |4.57                |3.63                  |4.63                     |4.75                 |4.88                       |4.63                  |4.63               |       |t               |9                             |9                                          |0                                           |0                                          |0.06             |
|163792|https://www.airbnb.com/rooms/163792|20231215032838|2023-12-15  |previous scrape|Rental unit in Vienna · ★4.84 · 2 bedrooms · 3 beds · 1 bath        |           |The apartment is situated in a very quiet and green area, but not far away from the city center. The street is a residential one, there's no traffic. Supermarkets, backery, restaurants and shopping mall are located in less than 10 minutes walking distance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |https://a0.muscache.com/pictures/f4c8252f-6e10-4df1-a1c0-3bb5c5be3964.jpg                              |651150  |https://www.airbnb.com/users/show/651150  |Klaus & Ligia|2011-06-01|Vienna, Austria    |Travelling and meeting interesting people are some of my major interests. Airbnb lets me do both at the same time :-)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |within an hour    |100%              |100%                |f                |https://a0.muscache.com/im/pictures/user/ef78506e-5e8f-4d56-9009-35f7770695e4.jpg?aki_policy=profile_small                      |https://a0.muscache.com/im/pictures/user/ef78506e-5e8f-4d56-9009-35f7770695e4.jpg?aki_policy=profile_x_medium                      |Simmering           |1                  |5                        |['email', 'phone']              |t                   |t                     |Vienna, Austria      |Simmering             |                            |48.18022|16.41955 |Entire rental unit         |Entire home/apt|4           |         |1 bath          |        |3   |[]       |$43.00 |3             |184           |3                     |3                     |1125                  |1125                  |3.0                   |1125.0                |                |t               |0              |0              |0              |0               |2023-12-15           |126              |17                   |0                     |2011-09-18  |2023-10-11 |4.84                |4.96                  |4.93                     |4.95                 |4.94                       |4.55                  |4.86               |       |f               |1                             |1                                          |0                                           |0                                          |0.85             |
|169672|https://www.airbnb.com/rooms/169672|20231215032838|2023-12-15  |city scrape    |Rental unit in Vienna · ★4.74 · 1 bedroom · 1 bed · 1 shared bath   |           |Lovely neighbourhood, full of trendy cafés, bars, shops and galleries (near the famous Naschmarkt).<br />Walking distance to the historical city centre.<br /><br />Some restaurants I can recommend:<br />- Cafe Bacco: Great authentic Italian restaurant in the same building (next door). Chef Alberto from Tuscany offers a daily varying menu based on fresh and seasonal products, starting with a range of bruschette, followed by various antipasti, a choice of pasta, a main course of meat and a dessert. The full menu costs €35, if you leave out some courses you will pay accordingly less.<br /><br />- Taste of India: Indian restaurant on the opposite side of the street: Tasty Indian dishes, reasonably priced.<br /><br />- Zweitbester, Heumühlgasse 2  (around the corner): Young and modern restaurant, very good food (vegeterian as well as meat and fish), creative recipes, excellent burgers, sunday brunch, in teh evenings occasionaly dj-music.<br /><br />- Altes Fassl, Ziegelofengasse 37: about 1|https://a0.muscache.com/pictures/c1a1e093-66da-4fd5-8764-2bfd85a72715.jpg                              |808772  |https://www.airbnb.com/users/show/808772  |Astrid       |2011-07-12|Vienna, Austria    |I am an art historian and paintings conservator, working in a museum in Vienna. As such, I regularly visit art exhibitons, and love to go on short trips to historical cities and cultural sites of Europe's past.  Since a few years however, much of my spare time is dedicated to my passion of Tango argentino, and whenever time allows I travel around visiting festivals and marathons, dancing days and nights in a row... Apart from that, I am interested in literature, film, theatre and music with a broad taste ranging from indie pop to classical music, from hip hop to world and crossover.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |within an hour    |100%              |92%                 |t                |https://a0.muscache.com/im/users/808772/profile_pic/1310468360/original.jpg?aki_policy=profile_small                            |https://a0.muscache.com/im/users/808772/profile_pic/1310468360/original.jpg?aki_policy=profile_x_medium                            |Wieden              |1                  |1                        |['email', 'phone']              |t                   |t                     |Vienna, Austria      |Wieden                |                            |48.19527|16.36374 |Private room in rental unit|Private room   |2           |         |1 shared bath   |        |1   |[]       |$46.00 |2             |30            |1                     |2                     |30                    |30                    |2.0                   |30.0                  |                |t               |12             |42             |69             |332             |2023-12-15           |405              |22                   |3                     |2011-08-11  |2023-12-09 |4.74                |4.79                  |4.69                     |4.79                 |4.74                       |4.9                   |4.75               |       |f               |1                             |0                                          |1                                           |0                                          |2.69             |
|482090|https://www.airbnb.com/rooms/482090|20231215032838|2023-12-15  |previous scrape|Rental unit in Vienna · 1 bedroom · 1 bed                           |           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |https://a0.muscache.com/pictures/5714716/6609d0ff_original.jpg                                         |2387347 |https://www.airbnb.com/users/show/2387347 |Manuela      |2012-05-16|                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |N/A               |N/A               |N/A                 |f                |https://a0.muscache.com/im/users/2387347/profile_pic/1337171296/original.jpg?aki_policy=profile_small                           |https://a0.muscache.com/im/users/2387347/profile_pic/1337171296/original.jpg?aki_policy=profile_x_medium                           |Rudolfsheim-Fünfhaus|1                  |1                        |['email']                       |t                   |f                     |                     |Rudolfsheim-Fnfhaus  |                            |48.1969 |16.31793 |Private room in rental unit|Private room   |2           |         |                |        |1   |[]       |$40.00 |14            |1125          |14                    |14                    |1125                  |1125                  |14.0                  |1125.0                |                |t               |0              |0              |0              |0               |2023-12-15           |0                |0                    |0                     |            |           |                    |                      |                         |                     |                           |                      |                   |       |f               |1                             |0                                          |1                                           |0                                          |                 |
|488723|https://www.airbnb.com/rooms/488723|20231215032838|2023-12-15  |city scrape    |Rental unit in Vienna · ★4.88 · 1 bedroom · 2 beds · 1.5 baths      |           |Your apartment enjoys a central but green and quiet location being just a few meters away from the Viennese baroque park, Augarten. In the immediate vicinity, you find grocery stores and drug stores and are also offered a bright range of cafes and restaurants. <br /><br />The most famous monuments of Vienna´s old town like the parlament or St. Steven´s Cathedral are easy to reach by tube while the tram gets you directly to the themepark Prater.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |https://a0.muscache.com/pictures/miso/Hosting-488723/original/072a632f-98eb-427d-bfa3-4994241e57fb.jpeg|2418146 |https://www.airbnb.com/users/show/2418146 |Gisella      |2012-05-20|Vienna, Austria    |Schon immer interessierte ich mich für Menschen und ihre verschiedenen Mentalitäten und begegnete und begegne ihnen mit Freude und Offenheit. Ich liebe Fotografieren, Filme, Bücher und Musik. Und außerdem liebe ich Reisen! Während meiner vielen traumhaft schönen, zum Teil auch abenteuerlichen Trips durch die Welt traf ich auf so viele wunderbare Gastgeber, welche mir durch ihre Gastfreundschaft zusätzliche bleibende Eindrücke hinterließen. Durch diese schönen Erfahrungen wuchs in mir der Wunsch, eine Art „Zuhause auf Zeit“ für andere zu gründen, eines, indem sich kreative Menschen und Familien, Wochenendreisende und Traveller, Fremde und Freunde an einem Ort begegnen. Ich freue mich auf Ihren, Euren Besuch.  Gisella                                                                                                                                                                                                                                                                                                                                                                                                                                                 |within an hour    |100%              |99%                 |f                |https://a0.muscache.com/im/pictures/user/e9689e04-aaa7-4dd7-8f1d-3cfe94a20097.jpg?aki_policy=profile_small                      |https://a0.muscache.com/im/pictures/user/e9689e04-aaa7-4dd7-8f1d-3cfe94a20097.jpg?aki_policy=profile_x_medium                      |Brigittenau         |20                 |31                       |['email', 'phone']              |t                   |t                     |Vienna, Austria      |Brigittenau           |                            |48.22875|16.37405 |Entire rental unit         |Entire home/apt|4           |         |1.5 baths       |        |2   |[]       |$79.00 |20            |1125          |6                     |20                    |365                   |1125                  |14.4                  |1118.0                |                |t               |8              |25             |35             |270             |2023-12-15           |124              |8                    |1                     |2013-04-25  |2023-12-07 |4.88                |4.88                  |4.92                     |4.96                 |4.93                       |4.74                  |4.75               |       |t               |18                            |18                                         |0                                           |0                                          |0.96             |
|208734|https://www.airbnb.com/rooms/208734|20231215032838|2023-12-15  |previous scrape|Rental unit in Vienna · ★4.27 · 2 bedrooms · 3 beds · 1 bath        |           |位于维也纳市中心, 但由于位置在一条小侧街，房间很安静。超市、药店、咖啡店、饭店（附近有N家有名的泰国餐厅、越南餐厅、印度餐厅、匈牙利餐厅、意大利餐厅、主题餐厅…… 还有亚洲餐厅、土耳其餐、奥地利餐、各种物美价廉的外卖店以及世界著名的麦当劳：））、烟店、篮球场、裁缝铺、美容院、健身中心都只有数步之遥。水族馆（楼顶有360度全景咖啡餐厅，视野很美）、IMAX电影院、邮局、有名的几家意大利餐厅、素食餐厅、希腊餐厅、啤酒吧、鸡尾酒吧、著名发型屋等步行几分钟可至。离最繁华的玛利亚大街步行街只需要步行5分钟，而且沿途有各种特色品牌店、特色咖啡馆，随时有小惊喜。<br /><br />门前街道晚上22点至早上9点停车免费,周六周日停车免费。<br />停车票请到附近烟店购买。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |https://a0.muscache.com/pictures/36ea3e50-9465-4e31-b2d6-5a360e60f08e.jpg                              |1028000 |https://www.airbnb.com/users/show/1028000 |Liang        |2011-08-27|Vienna, Austria    |累了就睡觉，醒了就微笑。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |N/A               |N/A               |N/A                 |f                |https://a0.muscache.com/im/pictures/user/7fff959a-09a2-4293-bb97-2888c852e607.jpg?aki_policy=profile_small                      |https://a0.muscache.com/im/pictures/user/7fff959a-09a2-4293-bb97-2888c852e607.jpg?aki_policy=profile_x_medium                      |Mariahilf           |1                  |1                        |['email', 'phone']              |t                   |t                     |Vienna, Wien, Austria|Mariahilf             |                            |48.19341|16.35082 |Entire rental unit         |Entire home/apt|6           |         |1 bath          |        |3   |[]       |       |3             |30            |3                     |3                     |30                    |30                    |3.0                   |30.0                  |                |                |0              |0              |0              |0               |2023-12-15           |22               |0                    |0                     |2017-06-17  |2019-05-21 |4.27                |4.5                   |4.45                     |4.77                 |4.45                       |4.59                  |4.14               |       |t               |1                             |1                                          |0                                           |0                                          |0.28             |
|210780|https://www.airbnb.com/rooms/210780|20231215032838|2023-12-15  |city scrape    |Rental unit in Vienna · ★4.87 · Studio · 3 beds · 1 bath            |           |The apartment is in a calm neighborhood within walking distance of Palace Schönbrunn, tasty local dining, and boutique shops. The underground station is nearby providing easy access to the historical district and central Vienna.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |https://a0.muscache.com/pictures/531052e9-e239-4e34-9230-d7790b10f465.jpg                              |175131  |https://www.airbnb.com/users/show/175131  |Ingela       |2010-07-20|Vienna, Austria    |I´m originally from Sweden but have been living in Vienna for many years. I love this city and I love meeting guests from different parts of the world :-) During my travel, both privately and on duty, I have learned the importance of safe, clean and comfortable accommodation in a central location with good infrastructure. This is what I offer you with my apartments.   Most of my apartments are located in the same building right on the underground U4 Meidling Hauptstrase that connects to the city center in less than 10min, and at the same time walking distance to Palace Schönbrunn - Austria´s biggest tourist attraction.   My city centre apartment is located next to Hofburg Palace with walking distance to all the inner city attractions.  As the majority of my apartments are located in the same building it is very convenient for groups as well to stay with me. My offer spans from studio apartments of 30m2 to 3 bedroom apartments of 100m2 sleeping up to 14 persons.  Since 1 January 2015 I have been an Airbnb Super Host. This is such an honour and I will do everything I can to make YOUR stay perfect as well!!  Kind regards,  Ingela Johansson :-)|within an hour    |98%               |85%                 |t                |https://a0.muscache.com/im/users/175131/profile_pic/1279660518/original.jpg?aki_policy=profile_small                            |https://a0.muscache.com/im/users/175131/profile_pic/1279660518/original.jpg?aki_policy=profile_x_medium                            |Rudolfsheim-Fünfhaus|17                 |19                       |['email', 'phone']              |t                   |t                     |Vienna, Austria      |Rudolfsheim-Fnfhaus  |                            |48.18444|16.32715 |Entire rental unit         |Entire home/apt|3           |         |1 bath          |        |3   |[]       |$99.00 |1             |180           |1                     |3                     |180                   |180                   |1.0                   |180.0                 |                |t               |11             |11             |11             |208             |2023-12-15           |178              |4                    |0                     |2011-10-06  |2023-06-04 |4.87                |4.93                  |4.93                     |4.93                 |4.93                       |4.77                  |4.86               |       |f               |15                            |14                                         |1                                           |0                                          |1.20             |
|212649|https://www.airbnb.com/rooms/212649|20231215032838|2023-12-15  |city scrape    |Rental unit in Vienna · ★4.91 · 3 bedrooms · 2 beds · 2 baths       |           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |https://a0.muscache.com/pictures/miso/Hosting-212649/original/98b3c82c-5324-4063-aeb8-51c3a2148526.jpeg|358842  |https://www.airbnb.com/users/show/358842  |Elxe         |2011-01-23|Vienna, Austria    |Ich lebe in der Stadt und am Land, ich liebe es, meine Freund*innen zu treffen, zu tanzen, kochen, essen gehen, kulturell was unternehmen und ich liebe es auch, in der Natur zu sein, den Schmetterlingen lauschen, zu gärtnern, im Chor zu singen, mal im Dirndl, mal im Cocktailkleid auszugehen, Zeit mit meiner Familie zu verbringen und mit meinem Freund zu lachen und ihn necken.  * )                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |within an hour    |100%              |94%                 |t                |https://a0.muscache.com/im/pictures/user/User-358842/original/7d3fe8db-d311-496e-8430-b9bb55f8e77a.jpeg?aki_policy=profile_small|https://a0.muscache.com/im/pictures/user/User-358842/original/7d3fe8db-d311-496e-8430-b9bb55f8e77a.jpeg?aki_policy=profile_x_medium|Leopoldstadt        |4                  |4                        |['email', 'phone']              |t                   |t                     |                     |Leopoldstadt          |                            |48.21971|16.37903 |Private room in rental unit|Private room   |2           |         |2 baths         |        |2   |[]       |$45.00 |2             |60            |2                     |2                     |60                    |60                    |2.0                   |60.0                  |                |t               |0              |0              |0              |110             |2023-12-15           |32               |3                    |0                     |2012-05-12  |2023-02-25 |4.91                |4.97                  |4.94                     |4.97                 |4.87                       |5.0                   |4.81               |       |f               |3                             |1                                          |2                                           |0                                          |0.23             |
|216214|https://www.airbnb.com/rooms/216214|20231215032838|2023-12-15  |city scrape    |Rental unit in Vienna · ★4.58 · 1 bedroom · 1 bed · Shared half-bath|           |The Naschmarkt area near the State Opera House and the old city is the place to be in Vienna.<br /><br />It is the place with the most bars, galleries and restaurants open day and night, with many alternative shopping and places to eat. It is the place where you feel the real Vienna.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |https://a0.muscache.com/pictures/7a5abee3-247c-4df3-ac06-ee54cc9aab78.jpg                              |518644  |https://www.airbnb.com/users/show/518644  |Michael      |2011-04-18|Vienna, Austria    |I studied Musicology, German Literature and singing as a counter tenor, mainly Renaissance and Baroque music.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                  |                  |                    |                 |                                                                                                                                |                                                                                                                                   |                    |                   |                         |                                |                    |                      |                     |                      |                            |        |         |                           |               |            |         |                |        |    |         |       |              |              |                      |                      |                      |                      |                      |                      |                |                |               |               |               |                |                     |                 |                     |                      |            |           |                    |                      |                         |                     |                           |                      |                   |       |                |                              |                                           |                                            |                                           |                 |

("..." indicates clipped or omitted data.)

#### Data Problems and Scrubbing Tasks

Upon initial review, the dataset appears to be well-structured; however, common issues in such datasets that might require attention include:

1. **Missing Values**: Fields like `reviews_per_month` might contain null values, especially for listings without any reviews. So we filled missing review scores with the average score.
```python
average_score = data['review_scores_rating'].mean()
data['review_scores_rating'] = data['review_scores_rating'].fillna(average_score)
```

2. **Inconsistent Data**: The `name` field might contain various formats, making it challenging to extract structured information. So we standarized the name and neighbourhood by capitalizing it.
```python
data['name'] = data['name'].str.title()
data['neighbourhood'] = data['neighbourhood'].str.title()
```
3. **Incorrect encoding** The `neighbourhood_cleansed` field does not handle german umlauts correctly, they are encoded improperly so they have to be fixed. So we encoded them properly.
```python
replacements = {
    'Rudolfsheim-Fnfhaus': 'Rudolfsheim-Fünfhaus',
    'Landstra§e': 'Landstraße',
    'Dbling': 'Döbling',
    'Whring': 'Währing'
}

for original, replacement in replacements.items():
    data['neighbourhood_cleansed'] = data['neighbourhood_cleansed'].str.replace(original, replacement)
```

4. **Outliers**: Prices or minimum nights might have unrealistic values due to data entry errors or unique listings. So we removed extreme values.
We did this by using this code 
```python
# Remove dollar signs and commas, then convert to float
data['price'] = data['price'].str.replace('$', '').str.replace(',', '').astype(float)

# Perform the filtering
data = data[(data['price'] > 0) & (data['price'] <= 10000)]

# When adding the dollar sign back, consider formatting the float to two decimal places
data['price'] = '$' + data['price'].round(2).astype(str)
```


## Part 2

### Show exactly two documents from the listings collection in any order
This query will do exactly what it says

The code we use to perform it is
```javascript
db.listings.find().limit(2)
```

The result we get is

```javascript
[
  {
    _id: ObjectId('660dbb6fb6515eb20577bba4'),
    id: 38768,
    listing_url: 'https://www.airbnb.com/rooms/38768',
    scrape_id: Long('20231215032838'),
    last_scraped: '2023-12-15',
    source: 'city scrape',
    name: 'Rental Unit In Vienna · ★4.75 · 1 Bedroom · 3 Beds · 1 Bath',
    description: '',
    neighborhood_overview: 'the Karmeliterviertel became very popular in the last years. It offers many new pubs and restaurants and is located next to Augarten (huge garden good for jogging), to the concert hall of Wiener Sängerknaben (muth), and has the Karmelitermarket, which is best to visit on Saturday morning to get biological products. In summer the best nightbars are at the donaukanal, which is 5 minutes away.',
    picture_url: 'https://a0.muscache.com/pictures/ad4089a3-5355-4681-96bb-e3ad70684987.jpg',
    host_id: 166283,
    host_url: 'https://www.airbnb.com/users/show/166283',
    host_name: 'Hannes',
    host_since: '2010-07-14',
    host_location: 'Vienna, Austria',
    host_about: 'I am open minded and like travelling myself. I have spent many months in Latinamerica and Asia, where I got  in touch with Indian philosophie and meditation...\n' +
      'Now I mostly work in the field of contemporary art and I do my best to offer you a nice apartment next to the citycenter...!\n' +
      '\n' +
      '\n',
    host_response_time: 'within an hour',
    host_response_rate: '100%',
    host_acceptance_rate: '100%',
    host_is_superhost: 'f',
    host_thumbnail_url: 'https://a0.muscache.com/im/users/166283/profile_pic/1435040494/original.jpg?aki_policy=profile_small',
    host_picture_url: 'https://a0.muscache.com/im/users/166283/profile_pic/1435040494/original.jpg?aki_policy=profile_x_medium',
    host_neighbourhood: 'Leopoldstadt',
    host_listings_count: 3,
    host_total_listings_count: 3,
    host_verifications: "['email', 'phone']",
    host_has_profile_pic: 't',
    host_identity_verified: 't',
    neighbourhood: 'Vienna, Austria',
    neighbourhood_cleansed: 'Leopoldstadt',
    neighbourhood_group_cleansed: '',
    latitude: 48.21924,
    longitude: 16.37831,
    property_type: 'Entire rental unit',
    room_type: 'Entire home/apt',
    accommodates: 5,
    bathrooms: '',
    bathrooms_text: '1 bath',
    bedrooms: '',
    beds: 3,
    amenities: '[]',
    price: '$77.0',
    minimum_nights: 4,
    maximum_nights: 75,
    minimum_minimum_nights: 3,
    maximum_minimum_nights: 28,
    minimum_maximum_nights: 1125,
    maximum_maximum_nights: 1125,
    minimum_nights_avg_ntm: 9.1,
    maximum_nights_avg_ntm: 1125,
    calendar_updated: '',
    has_availability: 't',
    availability_30: 12,
    availability_60: 42,
    availability_90: 72,
    availability_365: 159,
    calendar_last_scraped: '2023-12-15',
    number_of_reviews: 384,
    number_of_reviews_ltm: 27,
    number_of_reviews_l30d: 4,
    first_review: '2011-03-23',
    last_review: '2023-12-14',
    review_scores_rating: 4.75,
    review_scores_accuracy: 4.81,
    review_scores_cleanliness: 4.65,
    review_scores_checkin: 4.91,
    review_scores_communication: 4.94,
    review_scores_location: 4.77,
    review_scores_value: 4.7,
    license: '',
    instant_bookable: 't',
    calculated_host_listings_count: 3,
    calculated_host_listings_count_entire_homes: 3,
    calculated_host_listings_count_private_rooms: 0,
    calculated_host_listings_count_shared_rooms: 0,
    reviews_per_month: 2.48
  },
  {
    _id: ObjectId('660dbb6fb6515eb20577bba5'),
    id: 51287,
    listing_url: 'https://www.airbnb.com/rooms/51287',
    scrape_id: Long('20231215032838'),
    last_scraped: '2023-12-15',
    source: 'city scrape',
    name: 'Rental Unit In Vienna · ★4.66 · Studio · 2 Beds · 1 Bath',
    description: '',
    neighborhood_overview: 'The neighbourhood has a lot of very nice little pubs and restaurants. 200 meters away you have the karmelitermarket, which is especially great on saturday morning. Aswell I like the Augarten, which is one of the biggist gardens in Vienna and just 5 minutes away! Beautiful old buildings are around and nearby is the modern Noveltower, including a skybar at the Sofitel (Praterstraße 1) which has a terrific view above the city!',
    picture_url: 'https://a0.muscache.com/pictures/25163038/1c4e1334_original.jpg',
    host_id: 166283,
    host_url: 'https://www.airbnb.com/users/show/166283',
    host_name: 'Hannes',
    host_since: '2010-07-14',
    host_location: 'Vienna, Austria',
    host_about: 'I am open minded and like travelling myself. I have spent many months in Latinamerica and Asia, where I got  in touch with Indian philosophie and meditation...\n' +
      'Now I mostly work in the field of contemporary art and I do my best to offer you a nice apartment next to the citycenter...!\n' +
      '\n' +
      '\n',
    host_response_time: 'within an hour',
    host_response_rate: '100%',
    host_acceptance_rate: '100%',
    host_is_superhost: 'f',
    host_thumbnail_url: 'https://a0.muscache.com/im/users/166283/profile_pic/1435040494/original.jpg?aki_policy=profile_small',
    host_picture_url: 'https://a0.muscache.com/im/users/166283/profile_pic/1435040494/original.jpg?aki_policy=profile_x_medium',
    host_neighbourhood: 'Leopoldstadt',
    host_listings_count: 3,
    host_total_listings_count: 3,
    host_verifications: "['email', 'phone']",
    host_has_profile_pic: 't',
    host_identity_verified: 't',
    neighbourhood: 'Vienna, Austria',
    neighbourhood_cleansed: 'Leopoldstadt',
    neighbourhood_group_cleansed: '',
    latitude: 48.21778,
    longitude: 16.37847,
    property_type: 'Entire rental unit',
    room_type: 'Entire home/apt',
    accommodates: 3,
    bathrooms: '',
    bathrooms_text: '1 bath',
    bedrooms: '',
    beds: 2,
    amenities: '[]',
    price: '$73.0',
    minimum_nights: 5,
    maximum_nights: 90,
    minimum_minimum_nights: 3,
    maximum_minimum_nights: 14,
    minimum_maximum_nights: 1125,
    maximum_maximum_nights: 1125,
    minimum_nights_avg_ntm: 8.4,
    maximum_nights_avg_ntm: 1125,
    calendar_updated: '',
    has_availability: 't',
    availability_30: 12,
    availability_60: 42,
    availability_90: 72,
    availability_365: 72,
    calendar_last_scraped: '2023-12-15',
    number_of_reviews: 370,
    number_of_reviews_ltm: 14,
    number_of_reviews_l30d: 1,
    first_review: '2011-01-27',
    last_review: '2023-12-09',
    review_scores_rating: 4.66,
    review_scores_accuracy: 4.78,
    review_scores_cleanliness: 4.52,
    review_scores_checkin: 4.92,
    review_scores_communication: 4.95,
    review_scores_location: 4.86,
    review_scores_value: 4.59,
    license: '',
    instant_bookable: 'f',
    calculated_host_listings_count: 3,
    calculated_host_listings_count_entire_homes: 3,
    calculated_host_listings_count_private_rooms: 0,
    calculated_host_listings_count_shared_rooms: 0,
    reviews_per_month: 2.36
  }
]
```

This might bring insights on 2 data points in the data.

### Show exactly 10 documents in any order, but "prettyprint" in easier to read format, using the pretty() function
This query will use pretty in order to make it easier to read

The code we use is

```javascript
db.listings.find().limit(10).pretty()
```

The result we get is
```javascript
[
  {
    _id: ObjectId('660dbb6fb6515eb20577bba4'),
    id: 38768,
    listing_url: 'https://www.airbnb.com/rooms/38768',
    scrape_id: Long('20231215032838'),
    last_scraped: '2023-12-15',
    source: 'city scrape',
    name: 'Rental Unit In Vienna · ★4.75 · 1 Bedroom · 3 Beds · 1 Bath',
    description: '',
    neighborhood_overview: 'the Karmeliterviertel became very popular in the last years. It offers many new pubs and restaurants and is located next to Augarten (huge garden good for jogging), to the concert hall of Wiener Sängerknaben (muth), and has the Karmelitermarket, which is best to visit on Saturday morning to get biological products. In summer the best nightbars are at the donaukanal, which is 5 minutes away.',
    picture_url: 'https://a0.muscache.com/pictures/ad4089a3-5355-4681-96bb-e3ad70684987.jpg',
    host_id: 166283,
    host_url: 'https://www.airbnb.com/users/show/166283',
    host_name: 'Hannes',
    host_since: '2010-07-14',
    host_location: 'Vienna, Austria',
    host_about: 'I am open minded and like travelling myself. I have spent many months in Latinamerica and Asia, where I got  in touch with Indian philosophie and meditation...\n' +
      'Now I mostly work in the field of contemporary art and I do my best to offer you a nice apartment next to the citycenter...!\n' +
      '\n' +
      '\n',
    host_response_time: 'within an hour',
    host_response_rate: '100%',
    host_acceptance_rate: '100%',
    host_is_superhost: 'f',
    host_thumbnail_url: 'https://a0.muscache.com/im/users/166283/profile_pic/1435040494/original.jpg?aki_policy=profile_small',
    host_picture_url: 'https://a0.muscache.com/im/users/166283/profile_pic/1435040494/original.jpg?aki_policy=profile_x_medium',
    host_neighbourhood: 'Leopoldstadt',
    host_listings_count: 3,
    host_total_listings_count: 3,
    host_verifications: "['email', 'phone']",
    host_has_profile_pic: 't',
    host_identity_verified: 't',
    neighbourhood: 'Vienna, Austria',
    neighbourhood_cleansed: 'Leopoldstadt',
    neighbourhood_group_cleansed: '',
    latitude: 48.21924,
    longitude: 16.37831,
    property_type: 'Entire rental unit',
    room_type: 'Entire home/apt',
    accommodates: 5,
    bathrooms: '',
    bathrooms_text: '1 bath',
    bedrooms: '',
    beds: 3,
    amenities: '[]',
    price: '$77.0',
    minimum_nights: 4,
    maximum_nights: 75,
    minimum_minimum_nights: 3,
    maximum_minimum_nights: 28,
    minimum_maximum_nights: 1125,
    maximum_maximum_nights: 1125,
    minimum_nights_avg_ntm: 9.1,
    maximum_nights_avg_ntm: 1125,
    calendar_updated: '',
    has_availability: 't',
    availability_30: 12,
    availability_60: 42,
    availability_90: 72,
    availability_365: 159,
    calendar_last_scraped: '2023-12-15',
    number_of_reviews: 384,
    number_of_reviews_ltm: 27,
    number_of_reviews_l30d: 4,
    first_review: '2011-03-23',
    last_review: '2023-12-14',
    review_scores_rating: 4.75,
    review_scores_accuracy: 4.81,
    review_scores_cleanliness: 4.65,
    review_scores_checkin: 4.91,
    review_scores_communication: 4.94,
    review_scores_location: 4.77,
    review_scores_value: 4.7,
    license: '',
    instant_bookable: 't',
    calculated_host_listings_count: 3,
    calculated_host_listings_count_entire_homes: 3,
    calculated_host_listings_count_private_rooms: 0,
    calculated_host_listings_count_shared_rooms: 0,
    reviews_per_month: 2.48
  },
  {
    _id: ObjectId('660dbb6fb6515eb20577bba5'),
    id: 51287,
    listing_url: 'https://www.airbnb.com/rooms/51287',
    scrape_id: Long('20231215032838'),
    last_scraped: '2023-12-15',
    source: 'city scrape',
    name: 'Rental Unit In Vienna · ★4.66 · Studio · 2 Beds · 1 Bath',
    description: '',
    neighborhood_overview: 'The neighbourhood has a lot of very nice little pubs and restaurants. 200 meters away you have the karmelitermarket, which is especially great on saturday morning. Aswell I like the Augarten, which is one of the biggist gardens in Vienna and just 5 minutes away! Beautiful old buildings are around and nearby is the modern Noveltower, including a skybar at the Sofitel (Praterstraße 1) which has a terrific view above the city!',
    picture_url: 'https://a0.muscache.com/pictures/25163038/1c4e1334_original.jpg',
    host_id: 166283,
    host_url: 'https://www.airbnb.com/users/show/166283',
    host_name: 'Hannes',
    host_since: '2010-07-14',
    host_location: 'Vienna, Austria',
    host_about: 'I am open minded and like travelling myself. I have spent many months in Latinamerica and Asia, where I got  in touch with Indian philosophie and meditation...\n' +
      'Now I mostly work in the field of contemporary art and I do my best to offer you a nice apartment next to the citycenter...!\n' +
      '\n' +
      '\n',
    host_response_time: 'within an hour',
    host_response_rate: '100%',
    host_acceptance_rate: '100%',
    host_is_superhost: 'f',
    host_thumbnail_url: 'https://a0.muscache.com/im/users/166283/profile_pic/1435040494/original.jpg?aki_policy=profile_small',
    host_picture_url: 'https://a0.muscache.com/im/users/166283/profile_pic/1435040494/original.jpg?aki_policy=profile_x_medium',
    host_neighbourhood: 'Leopoldstadt',
    host_listings_count: 3,
    host_total_listings_count: 3,
    host_verifications: "['email', 'phone']",
    host_has_profile_pic: 't',
    host_identity_verified: 't',
    neighbourhood: 'Vienna, Austria',
    neighbourhood_cleansed: 'Leopoldstadt',
    neighbourhood_group_cleansed: '',
    latitude: 48.21778,
    longitude: 16.37847,
    property_type: 'Entire rental unit',
    room_type: 'Entire home/apt',
    accommodates: 3,
    bathrooms: '',
    bathrooms_text: '1 bath',
    bedrooms: '',
    beds: 2,
    amenities: '[]',
    price: '$73.0',
    minimum_nights: 5,
    maximum_nights: 90,
    minimum_minimum_nights: 3,
    maximum_minimum_nights: 14,
    minimum_maximum_nights: 1125,
    maximum_maximum_nights: 1125,
    minimum_nights_avg_ntm: 8.4,
    maximum_nights_avg_ntm: 1125,
    calendar_updated: '',
    has_availability: 't',
    availability_30: 12,
    availability_60: 42,
    availability_90: 72,
    availability_365: 72,
    calendar_last_scraped: '2023-12-15',
    number_of_reviews: 370,
    number_of_reviews_ltm: 14,
    number_of_reviews_l30d: 1,
    first_review: '2011-01-27',
    last_review: '2023-12-09',
    review_scores_rating: 4.66,
    review_scores_accuracy: 4.78,
    review_scores_cleanliness: 4.52,
    review_scores_checkin: 4.92,
    review_scores_communication: 4.95,
    review_scores_location: 4.86,
    review_scores_value: 4.59,
    license: '',
    instant_bookable: 'f',
    calculated_host_listings_count: 3,
    calculated_host_listings_count_entire_homes: 3,
    calculated_host_listings_count_private_rooms: 0,
    calculated_host_listings_count_shared_rooms: 0,
    reviews_per_month: 2.36
  },
  {
    _id: ObjectId('660dbb6fb6515eb20577bba6'),
    id: 70637,
    listing_url: 'https://www.airbnb.com/rooms/70637',
    scrape_id: Long('20231215032838'),
    last_scraped: '2023-12-15',
    source: 'city scrape',
    name: 'Rental Unit In Vienna · ★4.77 · 1 Bedroom · 2 Beds · 2 Shared Baths',
    description: '',
    neighborhood_overview: '',
    picture_url: 'https://a0.muscache.com/pictures/925691/c8c1bdd6_original.jpg',
    host_id: 358842,
    host_url: 'https://www.airbnb.com/users/show/358842',
    host_name: 'Elxe',
    host_since: '2011-01-23',
    host_location: 'Vienna, Austria',
    host_about: 'Ich lebe in der Stadt und am Land, ich liebe es, meine Freund*innen zu treffen, zu tanzen, kochen, essen gehen, kulturell was unternehmen und ich liebe es auch, in der Natur zu sein, den Schmetterlingen lauschen, zu gärtnern, im Chor zu singen, mal im Dirndl, mal im Cocktailkleid auszugehen, Zeit mit meiner Familie zu verbringen und mit meinem Freund zu lachen und ihn necken.  * )',
    host_response_time: 'within an hour',
    host_response_rate: '100%',
    host_acceptance_rate: '94%',
    host_is_superhost: 't',
    host_thumbnail_url: 'https://a0.muscache.com/im/pictures/user/User-358842/original/7d3fe8db-d311-496e-8430-b9bb55f8e77a.jpeg?aki_policy=profile_small',
    host_picture_url: 'https://a0.muscache.com/im/pictures/user/User-358842/original/7d3fe8db-d311-496e-8430-b9bb55f8e77a.jpeg?aki_policy=profile_x_medium',
    host_neighbourhood: 'Leopoldstadt',
    host_listings_count: 4,
    host_total_listings_count: 4,
    host_verifications: "['email', 'phone']",
    host_has_profile_pic: 't',
    host_identity_verified: 't',
    neighbourhood: '',
    neighbourhood_cleansed: 'Leopoldstadt',
    neighbourhood_group_cleansed: '',
    latitude: 48.2176,
    longitude: 16.38018,
    property_type: 'Private room in rental unit',
    room_type: 'Private room',
    accommodates: 2,
    bathrooms: '',
    bathrooms_text: '2 shared baths',
    bedrooms: '',
    beds: 2,
    amenities: '[]',
    price: '$50.0',
    minimum_nights: 2,
    maximum_nights: 1000,
    minimum_minimum_nights: 2,
    maximum_minimum_nights: 2,
    minimum_maximum_nights: 1000,
    maximum_maximum_nights: 1000,
    minimum_nights_avg_ntm: 2,
    maximum_nights_avg_ntm: 1000,
    calendar_updated: '',
    has_availability: 't',
    availability_30: 1,
    availability_60: 1,
    availability_90: 1,
    availability_365: 111,
    calendar_last_scraped: '2023-12-15',
    number_of_reviews: 116,
    number_of_reviews_ltm: 1,
    number_of_reviews_l30d: 0,
    first_review: '2011-03-28',
    last_review: '2023-01-18',
    review_scores_rating: 4.77,
    review_scores_accuracy: 4.74,
    review_scores_cleanliness: 4.68,
    review_scores_checkin: 4.8,
    review_scores_communication: 4.76,
    review_scores_location: 4.81,
    review_scores_value: 4.72,
    license: '',
    instant_bookable: 'f',
    calculated_host_listings_count: 3,
    calculated_host_listings_count_entire_homes: 1,
    calculated_host_listings_count_private_rooms: 2,
    calculated_host_listings_count_shared_rooms: 0,
    reviews_per_month: 0.75
  },
  {
    _id: ObjectId('660dbb6fb6515eb20577bba7'),
    id: 40625,
    listing_url: 'https://www.airbnb.com/rooms/40625',
    scrape_id: Long('20231215032838'),
    last_scraped: '2023-12-15',
    source: 'city scrape',
    name: 'Rental Unit In Vienna · ★4.85 · 2 Bedrooms · 4 Beds · 1 Bath',
    description: '',
    neighborhood_overview: 'The neighbourhood offers plenty of restaurants and grocery shops. In the apartment you will find an area map marked with the different restaurants and shops in the area, including opening hours for your ease of reference.',
    picture_url: 'https://a0.muscache.com/pictures/11509144/d55c2742_original.jpg',
    host_id: 175131,
    host_url: 'https://www.airbnb.com/users/show/175131',
    host_name: 'Ingela',
    host_since: '2010-07-20',
    host_location: 'Vienna, Austria',
    host_about: 'I´m originally from Sweden but have been living in Vienna for many years. I love this city and I love meeting guests from different parts of the world :-) During my travel, both privately and on duty, I have learned the importance of safe, clean and comfortable accommodation in a central location with good infrastructure. This is what I offer you with my apartments.\n' +
      ' \n' +
      'Most of my apartments are located in the same building right on the underground U4 Meidling Hauptstrase that connects to the city center in less than 10min, and at the same time walking distance to Palace Schönbrunn - Austria´s biggest tourist attraction. \n' +
      '\n' +
      'My city centre apartment is located next to Hofburg Palace with walking distance to all the inner city attractions.\n' +
      '\n' +
      'As the majority of my apartments are located in the same building it is very convenient for groups as well to stay with me. My offer spans from studio apartments of 30m2 to 3 bedroom apartments of 100m2 sleeping up to 14 persons.\n' +
      '\n' +
      'Since 1 January 2015 I have been an Airbnb Super Host. This is such an honour and I will do everything I can to make YOUR stay perfect as well!!\n' +
      '\n' +
      'Kind regards, \n' +
      'Ingela Johansson :-)',
    host_response_time: 'within an hour',
    host_response_rate: '98%',
    host_acceptance_rate: '85%',
    host_is_superhost: 't',
    host_thumbnail_url: 'https://a0.muscache.com/im/users/175131/profile_pic/1279660518/original.jpg?aki_policy=profile_small',
    host_picture_url: 'https://a0.muscache.com/im/users/175131/profile_pic/1279660518/original.jpg?aki_policy=profile_x_medium',
    host_neighbourhood: 'Rudolfsheim-Fünfhaus',
    host_listings_count: 17,
    host_total_listings_count: 19,
    host_verifications: "['email', 'phone']",
    host_has_profile_pic: 't',
    host_identity_verified: 't',
    neighbourhood: 'Vienna, Austria',
    neighbourhood_cleansed: 'Rudolfsheim-Fünfhaus',
    neighbourhood_group_cleansed: '',
    latitude: 48.18434,
    longitude: 16.32701,
    property_type: 'Entire rental unit',
    room_type: 'Entire home/apt',
    accommodates: 6,
    bathrooms: '',
    bathrooms_text: '1 bath',
    bedrooms: '',
    beds: 4,
    amenities: '[]',
    price: '$150.0',
    minimum_nights: 1,
    maximum_nights: 180,
    minimum_minimum_nights: 1,
    maximum_minimum_nights: 3,
    minimum_maximum_nights: 180,
    maximum_maximum_nights: 180,
    minimum_nights_avg_ntm: 1,
    maximum_nights_avg_ntm: 180,
    calendar_updated: '',
    has_availability: 't',
    availability_30: 19,
    availability_60: 49,
    availability_90: 79,
    availability_365: 350,
    calendar_last_scraped: '2023-12-15',
    number_of_reviews: 202,
    number_of_reviews_ltm: 17,
    number_of_reviews_l30d: 1,
    first_review: '2010-08-04',
    last_review: '2023-11-19',
    review_scores_rating: 4.85,
    review_scores_accuracy: 4.91,
    review_scores_cleanliness: 4.88,
    review_scores_checkin: 4.89,
    review_scores_communication: 4.94,
    review_scores_location: 4.59,
    review_scores_value: 4.72,
    license: '',
    instant_bookable: 't',
    calculated_host_listings_count: 15,
    calculated_host_listings_count_entire_homes: 14,
    calculated_host_listings_count_private_rooms: 1,
    calculated_host_listings_count_shared_rooms: 0,
    reviews_per_month: 1.24
  },
  {
    _id: ObjectId('660dbb6fb6515eb20577bba8'),
    id: 75500,
    listing_url: 'https://www.airbnb.com/rooms/75500',
    scrape_id: Long('20231215032838'),
    last_scraped: '2023-12-15',
    source: 'city scrape',
    name: 'Rental Unit In Vienna · ★4.45 · 2 Bedrooms · 2 Beds · 1 Bath',
    description: '',
    neighborhood_overview: '',
    picture_url: 'https://a0.muscache.com/pictures/549090/b51ce46d_original.jpg',
    host_id: 400857,
    host_url: 'https://www.airbnb.com/users/show/400857',
    host_name: 'Sabine',
    host_since: '2011-02-20',
    host_location: 'Geneva, Switzerland',
    host_about: 'I am Austrian, from Salzburg, but I spent 5 years in Vienna to study. Currently I am living in Switzerland and therefore my flat is very often available for guests.',
    host_response_time: 'within a day',
    host_response_rate: '100%',
    host_acceptance_rate: '75%',
    host_is_superhost: 'f',
    host_thumbnail_url: 'https://a0.muscache.com/im/pictures/user/5d5abab3-922c-45c4-add2-dda022e5c4ab.jpg?aki_policy=profile_small',
    host_picture_url: 'https://a0.muscache.com/im/pictures/user/5d5abab3-922c-45c4-add2-dda022e5c4ab.jpg?aki_policy=profile_x_medium',
    host_neighbourhood: '',
    host_listings_count: 1,
    host_total_listings_count: 1,
    host_verifications: "['email', 'phone']",
    host_has_profile_pic: 't',
    host_identity_verified: 't',
    neighbourhood: '',
    neighbourhood_cleansed: 'Brigittenau',
    neighbourhood_group_cleansed: '',
    latitude: 48.23493,
    longitude: 16.36752,
    property_type: 'Entire rental unit',
    room_type: 'Entire home/apt',
    accommodates: 4,
    bathrooms: '',
    bathrooms_text: '1 bath',
    bedrooms: '',
    beds: 2,
    amenities: '[]',
    price: '$85.0',
    minimum_nights: 4,
    maximum_nights: 90,
    minimum_minimum_nights: 4,
    maximum_minimum_nights: 4,
    minimum_maximum_nights: 90,
    maximum_maximum_nights: 90,
    minimum_nights_avg_ntm: 4,
    maximum_nights_avg_ntm: 90,
    calendar_updated: '',
    has_availability: 't',
    availability_30: 9,
    availability_60: 39,
    availability_90: 69,
    availability_365: 327,
    calendar_last_scraped: '2023-12-15',
    number_of_reviews: 12,
    number_of_reviews_ltm: 0,
    number_of_reviews_l30d: 0,
    first_review: '2011-07-20',
    last_review: '2019-12-01',
    review_scores_rating: 4.45,
    review_scores_accuracy: 4.67,
    review_scores_cleanliness: 4.67,
    review_scores_checkin: 4.67,
    review_scores_communication: 4.67,
    review_scores_location: 4.08,
    review_scores_value: 4.42,
    license: '',
    instant_bookable: 'f',
    calculated_host_listings_count: 1,
    calculated_host_listings_count_entire_homes: 1,
    calculated_host_listings_count_private_rooms: 0,
    calculated_host_listings_count_shared_rooms: 0,
    reviews_per_month: 0.08
  },
  {
    _id: ObjectId('660dbb6fb6515eb20577bba9'),
    id: 90247,
    listing_url: 'https://www.airbnb.com/rooms/90247',
    scrape_id: Long('20231215032838'),
    last_scraped: '2023-12-15',
    source: 'city scrape',
    name: 'Rental Unit In Vienna · ★4.85 · 1 Bedroom · 2 Beds · 1 Bath',
    description: '',
    neighborhood_overview: '',
    picture_url: 'https://a0.muscache.com/pictures/miso/Hosting-90247/original/d53fcd96-c015-4821-966c-863a1b0e533d.jpeg',
    host_id: 489611,
    host_url: 'https://www.airbnb.com/users/show/489611',
    host_name: 'Diana',
    host_since: '2011-04-06',
    host_location: 'Vienna, Austria',
    host_about: 'Born in Romania and living in Vienna. I love to host international guests and to travel abroad being hosted as well.\n' +
      'The eternal student I am always involved in learning something new. I speak Romanian, English, Spanish and German.\n' +
      'I love good food, especially Asian cuisine and Spanish tapas.',
    host_response_time: 'within an hour',
    host_response_rate: '100%',
    host_acceptance_rate: '100%',
    host_is_superhost: 't',
    host_thumbnail_url: 'https://a0.muscache.com/im/users/489611/profile_pic/1302126965/original.jpg?aki_policy=profile_small',
    host_picture_url: 'https://a0.muscache.com/im/users/489611/profile_pic/1302126965/original.jpg?aki_policy=profile_x_medium',
    host_neighbourhood: 'Neubau',
    host_listings_count: 3,
    host_total_listings_count: 3,
    host_verifications: "['email', 'phone']",
    host_has_profile_pic: 't',
    host_identity_verified: 't',
    neighbourhood: '',
    neighbourhood_cleansed: 'Neubau',
    neighbourhood_group_cleansed: '',
    latitude: 48.20599,
    longitude: 16.3489,
    property_type: 'Entire rental unit',
    room_type: 'Entire home/apt',
    accommodates: 4,
    bathrooms: '',
    bathrooms_text: '1 bath',
    bedrooms: '',
    beds: 2,
    amenities: '[]',
    price: '$128.0',
    minimum_nights: 1,
    maximum_nights: 1125,
    minimum_minimum_nights: 1,
    maximum_minimum_nights: 1,
    minimum_maximum_nights: 1125,
    maximum_maximum_nights: 1125,
    minimum_nights_avg_ntm: 1,
    maximum_nights_avg_ntm: 1125,
    calendar_updated: '',
    has_availability: 't',
    availability_30: 11,
    availability_60: 41,
    availability_90: 57,
    availability_365: 268,
    calendar_last_scraped: '2023-12-15',
    number_of_reviews: 743,
    number_of_reviews_ltm: 54,
    number_of_reviews_l30d: 3,
    first_review: '2011-04-21',
    last_review: '2023-11-29',
    review_scores_rating: 4.85,
    review_scores_accuracy: 4.92,
    review_scores_cleanliness: 4.93,
    review_scores_checkin: 4.91,
    review_scores_communication: 4.87,
    review_scores_location: 4.82,
    review_scores_value: 4.81,
    license: '',
    instant_bookable: 't',
    calculated_host_listings_count: 2,
    calculated_host_listings_count_entire_homes: 2,
    calculated_host_listings_count_private_rooms: 0,
    calculated_host_listings_count_shared_rooms: 0,
    reviews_per_month: 4.82
  },
  {
    _id: ObjectId('660dbb6fb6515eb20577bbaa'),
    id: 98210,
    listing_url: 'https://www.airbnb.com/rooms/98210',
    scrape_id: Long('20231215032838'),
    last_scraped: '2023-12-15',
    source: 'city scrape',
    name: 'Rental Unit In Vienna · ★4.55 · 1 Bedroom · 1 Bed · Shared Half-Bath',
    description: '',
    neighborhood_overview: '2 minutes to the old city with the subway from our street. The Naschmarkt and State Opera area is the place to be in Vienna, with many trendy restaurants, bars and galleries.<br /><br />It is ery easy to get here from the airport and train and bus stations. No taxi is needed.',
    picture_url: 'https://a0.muscache.com/pictures/1757461/3938b800_original.jpg',
    host_id: 518644,
    host_url: 'https://www.airbnb.com/users/show/518644',
    host_name: 'Michael',
    host_since: '2011-04-18',
    host_location: 'Vienna, Austria',
    host_about: 'I studied Musicology, German Literature and singing as a counter tenor, mainly Renaissance and Baroque music.\n' +
      '\n' +
      'Two of my passions are cooking (Vegan, Macrobiotic, also viennese kitchen) and the city of Vienna and what it has to offer. I do yoga, jogging, walking and biking tours.\n' +
      '\n' +
      "It's nice to meet all those people from all over the world and helping them through their way in Vienna. Vienna is not as famous as Paris or Londen, but has so much to offer, so many hidden interessting corners, full of history and art.",
    host_response_time: 'within an hour',
    host_response_rate: '90%',
    host_acceptance_rate: '75%',
    host_is_superhost: 'f',
    host_thumbnail_url: 'https://a0.muscache.com/im/pictures/user/f5d057ee-4f72-44f1-a01a-54b7c1712dd0.jpg?aki_policy=profile_small',
    host_picture_url: 'https://a0.muscache.com/im/pictures/user/f5d057ee-4f72-44f1-a01a-54b7c1712dd0.jpg?aki_policy=profile_x_medium',
    host_neighbourhood: 'Margareten',
    host_listings_count: 34,
    host_total_listings_count: 74,
    host_verifications: "['email', 'phone']",
    host_has_profile_pic: 't',
    host_identity_verified: 't',
    neighbourhood: 'Vienna, Austria',
    neighbourhood_cleansed: 'Margareten',
    neighbourhood_group_cleansed: '',
    latitude: 48.19409,
    longitude: 16.35857,
    property_type: 'Private room in rental unit',
    room_type: 'Private room',
    accommodates: 2,
    bathrooms: '',
    bathrooms_text: 'Shared half-bath',
    bedrooms: '',
    beds: 1,
    amenities: '[]',
    price: '$50.0',
    minimum_nights: 1,
    maximum_nights: 180,
    minimum_minimum_nights: 1,
    maximum_minimum_nights: 6,
    minimum_maximum_nights: 1125,
    maximum_maximum_nights: 1125,
    minimum_nights_avg_ntm: 1.1,
    maximum_nights_avg_ntm: 1125,
    calendar_updated: '',
    has_availability: 't',
    availability_30: 14,
    availability_60: 44,
    availability_90: 74,
    availability_365: 164,
    calendar_last_scraped: '2023-12-15',
    number_of_reviews: 139,
    number_of_reviews_ltm: 15,
    number_of_reviews_l30d: 0,
    first_review: '2011-05-08',
    last_review: '2023-09-17',
    review_scores_rating: 4.55,
    review_scores_accuracy: 4.62,
    review_scores_cleanliness: 4.73,
    review_scores_checkin: 4.76,
    review_scores_communication: 4.79,
    review_scores_location: 4.81,
    review_scores_value: 4.57,
    license: '',
    instant_bookable: 'f',
    calculated_host_listings_count: 34,
    calculated_host_listings_count_entire_homes: 17,
    calculated_host_listings_count_private_rooms: 17,
    calculated_host_listings_count_shared_rooms: 0,
    reviews_per_month: 0.91
  },
  {
    _id: ObjectId('660dbb6fb6515eb20577bbab'),
    id: 109679,
    listing_url: 'https://www.airbnb.com/rooms/109679',
    scrape_id: Long('20231215032838'),
    last_scraped: '2023-12-15',
    source: 'city scrape',
    name: 'Rental Unit In Vienna · ★4.87 · Studio · 4 Beds · 1 Bath',
    description: '',
    neighborhood_overview: 'The neighbourhood offers plenty of restaurants and grocery shops. In the apartment you will find an area map marked with the different restaurants and shops in the area, including opening hours for your ease of reference.',
    picture_url: 'https://a0.muscache.com/pictures/1982234/1fc346f2_original.jpg',
    host_id: 175131,
    host_url: 'https://www.airbnb.com/users/show/175131',
    host_name: 'Ingela',
    host_since: '2010-07-20',
    host_location: 'Vienna, Austria',
    host_about: 'I´m originally from Sweden but have been living in Vienna for many years. I love this city and I love meeting guests from different parts of the world :-) During my travel, both privately and on duty, I have learned the importance of safe, clean and comfortable accommodation in a central location with good infrastructure. This is what I offer you with my apartments.\n' +
      ' \n' +
      'Most of my apartments are located in the same building right on the underground U4 Meidling Hauptstrase that connects to the city center in less than 10min, and at the same time walking distance to Palace Schönbrunn - Austria´s biggest tourist attraction. \n' +
      '\n' +
      'My city centre apartment is located next to Hofburg Palace with walking distance to all the inner city attractions.\n' +
      '\n' +
      'As the majority of my apartments are located in the same building it is very convenient for groups as well to stay with me. My offer spans from studio apartments of 30m2 to 3 bedroom apartments of 100m2 sleeping up to 14 persons.\n' +
      '\n' +
      'Since 1 January 2015 I have been an Airbnb Super Host. This is such an honour and I will do everything I can to make YOUR stay perfect as well!!\n' +
      '\n' +
      'Kind regards, \n' +
      'Ingela Johansson :-)',
    host_response_time: 'within an hour',
    host_response_rate: '98%',
    host_acceptance_rate: '85%',
    host_is_superhost: 't',
    host_thumbnail_url: 'https://a0.muscache.com/im/users/175131/profile_pic/1279660518/original.jpg?aki_policy=profile_small',
    host_picture_url: 'https://a0.muscache.com/im/users/175131/profile_pic/1279660518/original.jpg?aki_policy=profile_x_medium',
    host_neighbourhood: 'Rudolfsheim-Fünfhaus',
    host_listings_count: 17,
    host_total_listings_count: 19,
    host_verifications: "['email', 'phone']",
    host_has_profile_pic: 't',
    host_identity_verified: 't',
    neighbourhood: 'Vienna, Austria',
    neighbourhood_cleansed: 'Rudolfsheim-Fünfhaus',
    neighbourhood_group_cleansed: '',
    latitude: 48.18467,
    longitude: 16.32795,
    property_type: 'Entire rental unit',
    room_type: 'Entire home/apt',
    accommodates: 5,
    bathrooms: '',
    bathrooms_text: '1 bath',
    bedrooms: '',
    beds: 4,
    amenities: '[]',
    price: '$130.0',
    minimum_nights: 1,
    maximum_nights: 180,
    minimum_minimum_nights: 1,
    maximum_minimum_nights: 3,
    minimum_maximum_nights: 180,
    maximum_maximum_nights: 180,
    minimum_nights_avg_ntm: 1,
    maximum_nights_avg_ntm: 180,
    calendar_updated: '',
    has_availability: 't',
    availability_30: 0,
    availability_60: 27,
    availability_90: 57,
    availability_365: 325,
    calendar_last_scraped: '2023-12-15',
    number_of_reviews: 135,
    number_of_reviews_ltm: 6,
    number_of_reviews_l30d: 0,
    first_review: '2012-04-02',
    last_review: '2023-09-23',
    review_scores_rating: 4.87,
    review_scores_accuracy: 4.87,
    review_scores_cleanliness: 4.91,
    review_scores_checkin: 4.91,
    review_scores_communication: 4.92,
    review_scores_location: 4.64,
    review_scores_value: 4.81,
    license: '',
    instant_bookable: 't',
    calculated_host_listings_count: 15,
    calculated_host_listings_count_entire_homes: 14,
    calculated_host_listings_count_private_rooms: 1,
    calculated_host_listings_count_shared_rooms: 0,
    reviews_per_month: 0.95
  },
  {
    _id: ObjectId('660dbb6fb6515eb20577bbac'),
    id: 111059,
    listing_url: 'https://www.airbnb.com/rooms/111059',
    scrape_id: Long('20231215032838'),
    last_scraped: '2023-12-15',
    source: 'city scrape',
    name: 'Rental Unit In Vienna · ★4.91 · 1 Bedroom · 1 Bed · 1 Bath',
    description: '',
    neighborhood_overview: "The apartment is located in a quiet one-way side street in the centre of Vienna's 17th district, Hernals. Small shopping center with supermarket, restaurants, pharmacy, and bakery is about 50 m away; several shops, cafes, tobacco shop, banks and restaurants are located nearby.<br />In the neighbourhood there three parking garages (Dornerplatz, Parhameplatz, Interspar Garage Hernals) available for a long term parking (90-115 €/month), further in 20 min away with public transport there are two Park-and-Ride parkings for cheaper week (around 20€) or monthly (around 70€) parking.",
    picture_url: 'https://a0.muscache.com/pictures/11308805/d0d7e800_original.jpg',
    host_id: 569644,
    host_url: 'https://www.airbnb.com/users/show/569644',
    host_name: 'Kateryna',
    host_since: '2011-05-09',
    host_location: 'Vienna, Austria',
    host_about: 'I am Kateryna and I am a Biologist. I am a real family person. In my spare time I enjoy reading, travelling, cooking - or just watching "Friends" (guess, I am a big fan) - Long story short: I am a Optimistic Realist.',
    host_response_time: 'within an hour',
    host_response_rate: '100%',
    host_acceptance_rate: '88%',
    host_is_superhost: 'f',
    host_thumbnail_url: 'https://a0.muscache.com/im/users/569644/profile_pic/1342560325/original.jpg?aki_policy=profile_small',
    host_picture_url: 'https://a0.muscache.com/im/users/569644/profile_pic/1342560325/original.jpg?aki_policy=profile_x_medium',
    host_neighbourhood: 'Hernals',
    host_listings_count: 2,
    host_total_listings_count: 2,
    host_verifications: "['email', 'phone']",
    host_has_profile_pic: 't',
    host_identity_verified: 't',
    neighbourhood: 'Vienna, Austria',
    neighbourhood_cleansed: 'Hernals',
    neighbourhood_group_cleansed: '',
    latitude: 48.22042,
    longitude: 16.33377,
    property_type: 'Entire rental unit',
    room_type: 'Entire home/apt',
    accommodates: 4,
    bathrooms: '',
    bathrooms_text: '1 bath',
    bedrooms: '',
    beds: 1,
    amenities: '[]',
    price: '$71.0',
    minimum_nights: 5,
    maximum_nights: 365,
    minimum_minimum_nights: 5,
    maximum_minimum_nights: 5,
    minimum_maximum_nights: 365,
    maximum_maximum_nights: 365,
    minimum_nights_avg_ntm: 5,
    maximum_nights_avg_ntm: 365,
    calendar_updated: '',
    has_availability: 't',
    availability_30: 0,
    availability_60: 0,
    availability_90: 0,
    availability_365: 0,
    calendar_last_scraped: '2023-12-15',
    number_of_reviews: 167,
    number_of_reviews_ltm: 4,
    number_of_reviews_l30d: 0,
    first_review: '2011-06-26',
    last_review: '2023-04-01',
    review_scores_rating: 4.91,
    review_scores_accuracy: 4.95,
    review_scores_cleanliness: 4.96,
    review_scores_checkin: 4.97,
    review_scores_communication: 4.98,
    review_scores_location: 4.67,
    review_scores_value: 4.89,
    license: '',
    instant_bookable: 'f',
    calculated_host_listings_count: 2,
    calculated_host_listings_count_entire_homes: 2,
    calculated_host_listings_count_private_rooms: 0,
    calculated_host_listings_count_shared_rooms: 0,
    reviews_per_month: 1.1
  },
  {
    _id: ObjectId('660dbb6fb6515eb20577bbad'),
    id: 114505,
    listing_url: 'https://www.airbnb.com/rooms/114505',
    scrape_id: Long('20231215032838'),
    last_scraped: '2023-12-15',
    source: 'city scrape',
    name: 'Rental Unit In Vienna · ★4.88 · Studio · 4 Beds · 1 Bath',
    description: '',
    neighborhood_overview: 'The neighbourhood offers plenty of restaurants and grocery shops. In the apartment you will find an area map marked with the different restaurants and shops in the area, including opening hours for your ease of reference.',
    picture_url: 'https://a0.muscache.com/pictures/11536257/906555e0_original.jpg',
    host_id: 175131,
    host_url: 'https://www.airbnb.com/users/show/175131',
    host_name: 'Ingela',
    host_since: '2010-07-20',
    host_location: 'Vienna, Austria',
    host_about: 'I´m originally from Sweden but have been living in Vienna for many years. I love this city and I love meeting guests from different parts of the world :-) During my travel, both privately and on duty, I have learned the importance of safe, clean and comfortable accommodation in a central location with good infrastructure. This is what I offer you with my apartments.\n' +
      ' \n' +
      'Most of my apartments are located in the same building right on the underground U4 Meidling Hauptstrase that connects to the city center in less than 10min, and at the same time walking distance to Palace Schönbrunn - Austria´s biggest tourist attraction. \n' +
      '\n' +
      'My city centre apartment is located next to Hofburg Palace with walking distance to all the inner city attractions.\n' +
      '\n' +
      'As the majority of my apartments are located in the same building it is very convenient for groups as well to stay with me. My offer spans from studio apartments of 30m2 to 3 bedroom apartments of 100m2 sleeping up to 14 persons.\n' +
      '\n' +
      'Since 1 January 2015 I have been an Airbnb Super Host. This is such an honour and I will do everything I can to make YOUR stay perfect as well!!\n' +
      '\n' +
      'Kind regards, \n' +
      'Ingela Johansson :-)',
    host_response_time: 'within an hour',
    host_response_rate: '98%',
    host_acceptance_rate: '85%',
    host_is_superhost: 't',
    host_thumbnail_url: 'https://a0.muscache.com/im/users/175131/profile_pic/1279660518/original.jpg?aki_policy=profile_small',
    host_picture_url: 'https://a0.muscache.com/im/users/175131/profile_pic/1279660518/original.jpg?aki_policy=profile_x_medium',
    host_neighbourhood: 'Rudolfsheim-Fünfhaus',
    host_listings_count: 17,
    host_total_listings_count: 19,
    host_verifications: "['email', 'phone']",
    host_has_profile_pic: 't',
    host_identity_verified: 't',
    neighbourhood: 'Vienna, Austria',
    neighbourhood_cleansed: 'Rudolfsheim-Fünfhaus',
    neighbourhood_group_cleansed: '',
    latitude: 48.18445,
    longitude: 16.32722,
    property_type: 'Entire rental unit',
    room_type: 'Entire home/apt',
    accommodates: 5,
    bathrooms: '',
    bathrooms_text: '1 bath',
    bedrooms: '',
    beds: 4,
    amenities: '[]',
    price: '$130.0',
    minimum_nights: 1,
    maximum_nights: 180,
    minimum_minimum_nights: 1,
    maximum_minimum_nights: 3,
    minimum_maximum_nights: 180,
    maximum_maximum_nights: 180,
    minimum_nights_avg_ntm: 1,
    maximum_nights_avg_ntm: 180,
    calendar_updated: '',
    has_availability: 't',
    availability_30: 3,
    availability_60: 33,
    availability_90: 63,
    availability_365: 335,
    calendar_last_scraped: '2023-12-15',
    number_of_reviews: 125,
    number_of_reviews_ltm: 2,
    number_of_reviews_l30d: 0,
    first_review: '2011-06-07',
    last_review: '2022-12-30',
    review_scores_rating: 4.88,
    review_scores_accuracy: 4.9,
    review_scores_cleanliness: 4.89,
    review_scores_checkin: 4.96,
    review_scores_communication: 4.96,
    review_scores_location: 4.71,
    review_scores_value: 4.8,
    license: '',
    instant_bookable: 'f',
    calculated_host_listings_count: 15,
    calculated_host_listings_count_entire_homes: 14,
    calculated_host_listings_count_private_rooms: 1,
    calculated_host_listings_count_shared_rooms: 0,
    reviews_per_month: 0.82
  }
]
```

This might allow us to look closer at the data than just someone looking at the table allowing us to come to better conclusions

### Choose two hosts (by reffering to their host_id values) who are superhosts (available in the host_is_superhost field), and show all of the listings offered by both of the two hosts


```javascript
   db.listings.find(
  { "host_id": { "$in": [175131, 675182] } },
  { "name": 1, "price": 1, "neighbourhood": 1, "host_name": 1, "host_is_superhost": 1 }
)
```

The result we get is

```javascript
[
  {
    _id: ObjectId('660dbb6fb6515eb20577bba7'),
    name: 'Rental Unit In Vienna · ★4.85 · 2 Bedrooms · 4 Beds · 1 Bath',
    host_name: 'Ingela',
    host_is_superhost: 't',
    neighbourhood: 'Vienna, Austria',
    price: '$150.0'
  },
  {
    _id: ObjectId('660dbb6fb6515eb20577bbab'),
    name: 'Rental Unit In Vienna · ★4.87 · Studio · 4 Beds · 1 Bath',
    host_name: 'Ingela',
    host_is_superhost: 't',
    neighbourhood: 'Vienna, Austria',
    price: '$130.0'
  },
  {
    _id: ObjectId('660dbb6fb6515eb20577bbad'),
    name: 'Rental Unit In Vienna · ★4.88 · Studio · 4 Beds · 1 Bath',
    host_name: 'Ingela',
    host_is_superhost: 't',
    neighbourhood: 'Vienna, Austria',
    price: '$130.0'
  },
  {
    _id: ObjectId('660dbb6fb6515eb20577bbb1'),
    name: 'Condo In Vienna · ★5.0 · 1 Bedroom · 2 Beds · 1 Bath',
    host_name: 'Stephanie',
    host_is_superhost: 't',
    neighbourhood: 'Vienna, Austria',
    price: '$154.0'
  },
  {
    _id: ObjectId('660dbb6fb6515eb20577bbb7'),
    name: 'Rental Unit In Vienna · ★4.87 · Studio · 3 Beds · 1 Bath',
    host_name: 'Ingela',
    host_is_superhost: 't',
    neighbourhood: 'Vienna, Austria',
    price: '$99.0'
  },
  {
    _id: ObjectId('660dbb6fb6515eb20577bbc9'),
    name: 'Condo In Vienna · 1 Bedroom · 2 Beds · 1 Bath',
    host_name: 'Stephanie',
    host_is_superhost: 't',
    neighbourhood: 'Vienna, Austria',
    price: '$100.0'
  },
  {
    _id: ObjectId('660dbb6fb6515eb20577bbcc'),
    name: 'Condo In Vienna · 1 Bedroom · 2 Beds · 1 Bath',
    host_name: 'Stephanie',
    host_is_superhost: 't',
    neighbourhood: 'Vienna, Austria',
    price: '$121.0'
  },
  {
    _id: ObjectId('660dbb6fb6515eb20577bbcd'),
    name: 'Condo In Vienna · ★5.0 · Studio · 1 Bed · 1 Bath',
    host_name: 'Stephanie',
    host_is_superhost: 't',
    neighbourhood: 'Vienna, Austria',
    price: '$89.0'
  },
  {
    _id: ObjectId('660dbb6fb6515eb20577bbce'),
    name: 'Condo In Vienna · 1 Bedroom · 2 Beds · 1 Bath',
    host_name: 'Stephanie',
    host_is_superhost: 't',
    neighbourhood: 'Vienna, Austria',
    price: '$95.0'
  },
  {
    _id: ObjectId('660dbb6fb6515eb20577bbcf'),
    name: 'Condo In Vienna · 2 Bedrooms · 4 Beds · 1 Bath',
    host_name: 'Stephanie',
    host_is_superhost: 't',
    neighbourhood: 'Vienna, Austria',
    price: '$149.0'
  },
  {
    _id: ObjectId('660dbb6fb6515eb20577bbd0'),
    name: 'Condo In Vienna · 1 Bedroom · 2 Beds · 1 Bath',
    host_name: 'Stephanie',
    host_is_superhost: 't',
    neighbourhood: 'Vienna, Austria',
    price: '$85.0'
  },
  {
    _id: ObjectId('660dbb6fb6515eb20577bbd1'),
    name: 'Condo In Vienna · ★4.67 · 1 Bedroom · 2 Beds · 1 Bath',
    host_name: 'Stephanie',
    host_is_superhost: 't',
    neighbourhood: 'Vienna, Austria',
    price: '$146.0'
  },
  {
    _id: ObjectId('660dbb6fb6515eb20577bbd2'),
    name: 'Condo In Vienna · Studio · 1 Bed · 1 Bath',
    host_name: 'Stephanie',
    host_is_superhost: 't',
    neighbourhood: 'Vienna, Austria',
    price: '$95.0'
  },
  {
    _id: ObjectId('660dbb6fb6515eb20577bbd5'),
    name: 'Rental Unit In Vienna · ★4.84 · 2 Bedrooms · 5 Beds · 1.5 Baths',
    host_name: 'Ingela',
    host_is_superhost: 't',
    neighbourhood: 'Vienna, Austria',
    price: '$272.0'
  },
  {
    _id: ObjectId('660dbb6fb6515eb20577bbd7'),
    name: 'Condo In Vienna · ★5.0 · Studio · 1 Bed · 1 Bath',
    host_name: 'Stephanie',
    host_is_superhost: 't',
    neighbourhood: 'Vienna, Austria',
    price: '$95.0'
  },
  {
    _id: ObjectId('660dbb6fb6515eb20577bbd8'),
    name: 'Condo In Vienna · ★5.0 · Studio · 1 Bed · 1 Bath',
    host_name: 'Stephanie',
    host_is_superhost: 't',
    neighbourhood: 'Vienna, Austria',
    price: '$94.0'
  },
  {
    _id: ObjectId('660dbb6fb6515eb20577bbd9'),
    name: 'Condo In Vienna · 2 Bedrooms · 5 Beds · 1 Bath',
    host_name: 'Stephanie',
    host_is_superhost: 't',
    neighbourhood: 'Vienna, Austria',
    price: '$209.0'
  },
  {
    _id: ObjectId('660dbb6fb6515eb20577bbda'),
    name: 'Serviced Apartment In Vienna · 2 Bedrooms · 5 Beds · 1 Bath',
    host_name: 'Stephanie',
    host_is_superhost: 't',
    neighbourhood: 'Vienna, Austria',
    price: '$211.0'
  },
  {
    _id: ObjectId('660dbb6fb6515eb20577bc06'),
    name: 'Rental Unit In Vienna · ★4.89 · 2 Bedrooms · 3 Beds · 1 Bath',
    host_name: 'Ingela',
    host_is_superhost: 't',
    neighbourhood: 'Vienna, Austria',
    price: '$156.0'
  },
  {
    _id: ObjectId('660dbb6fb6515eb20577bc54'),
    name: 'Rental Unit In Vienna · ★4.87 · 3 Bedrooms · 8 Beds · 1.5 Baths',
    host_name: 'Ingela',
    host_is_superhost: 't',
    neighbourhood: 'Vienna, Austria',
    price: '$263.0'
  }
]
```

This allows us to gain additional insight as it allows us to see all the units a certain person has, you would be unable to do this just looking at a CSV table. So we can see that Ingela has a lot of properties across vienna.

### Find all the unique `host_name` values:

The code we would use is

```javascript
db.listings.distinct("host_name")
```

This gives the results of

```javascript
[
  '',
  '4beds&More',
  'A',
  'ADO Apartments',
  'Aaron',
  'Aashima',
  'AbaiApartments',
  'Abdelrahman',
  'Abdullah',
  'Abieshomes',
  'Abigail',
  'Abraham',
  'AdInfinitum Philip Bea Sophia',
  'Ada',
  'Adam',
  'Adele',
  'Adelheid',
  'Adelin',
  'Adelina',
  'Adem',
  'Adesina',
  'Adi',
  'Adiam',
  'Adin',
  'Adina',
  'Adis',
  'Adisa',
  'Adnan',
  'Ado',
  'Adoniran',
  'Adrian',
  'Adriana',
  'Adriano',
  'Adrien Adnan',
  'Adrijana',
  'Adrián',
  'Aelia',
  'Agata',
  'Aglaë',
  'Agnes',
  'Agnese',
  'Agnieszka',
  'Ahmad',
  'Ahmed',
  'Ahmet',
  'Aida',
  'Aifuwa',
  'Aisha',
  'Ajla',
  'Akram',
  'Al',
  'Alaa',
  'Alan',
  'Albena',
  'Albert',
  'Albi',
  'Albino',
  'Aldin',
  'Aleks',
  'Aleksandar',
  'Aleksander',
  'Aleksandra',
  'Alen',
  'Alena',
  'Alessa',
  'Alessandra',
  'Alex',
  'Alexa',
  'Alexander',
  'Alexandra',
  'Alexis',
  'Alfred',
  'Alfred Und Christina',
  'Alfredo',
  'Ali',
  'Alice',
  'Alin',
  'Alina',
  'Alina-Zoe',
  'Aline',
  'Alireza',
  'Aliz',
  'Allesgute',
  'Alma',
  'Almina',
  'Almuthana',
  'Alois',
  'Alon',
  'Alp',
  'Alpheus',
  'Altstadt',
  'Alvina',
  'Amadeus',
  'Amal',
  'Amanda',
  'Ambi',
  'Amel',
  'Amelie',
  'Amets',
  'Amila',
  ... 2157 more items
]
```

### Find all of the places that have more than 2 beds in a neighborhood of your choice (referred to as either the neighborhood or neighbourhood_group_cleansed fields in the data file), ordered by review_scores_rating descending

```javascript
   db.listings.find({
     neighbourhood_cleansed: "Leopoldstadt",
     beds: { $gt: 2 }
   }, {
     name: 1, beds: 1, review_scores_rating: 1, price: 1
   }).sort({ review_scores_rating: -1 })
```
Results -

```javascript
[
  {
    _id: ObjectId('660dbb6fb6515eb20577be87'),
    name: 'Condo In Vienna · 2 Bedrooms · 5 Beds · 1 Bath',
    beds: 5,
    price: '$130.0',
    review_scores_rating: 5
  },
  {
    _id: ObjectId('660dbb6fb6515eb20577c0a1'),
    name: 'Rental Unit In Vienna · ★5.0 · 3 Bedrooms · 7 Beds · 2 Baths',
    beds: 7,
    price: '$600.0',
    review_scores_rating: 5
  },
  {
    _id: ObjectId('660dbb6fb6515eb20577c0a5'),
    name: 'Rental Unit In Vienna · ★5.0 · 2 Bedrooms · 3 Beds · 1 Bath',
    beds: 3,
    price: '$690.0',
    review_scores_rating: 5
  },
```

### Show the number of listings per host

```javascript
   db.listings.aggregate([
     { $group: { _id: "$host_id", total_listings: { $sum: 1 } } }
   ])
```

Results -

```javascript
[
  { _id: 44586496, total_listings: 1 },
  { _id: 181573153, total_listings: 1 },
  { _id: 235177184, total_listings: 2 },
  { _id: 543488122, total_listings: 1 },
  { _id: 79783186, total_listings: 1 },
  { _id: 84640349, total_listings: 3 },
  { _id: 286154252, total_listings: 1 },
  { _id: 200729542, total_listings: 1 },
  { _id: 547234192, total_listings: 1 },
  { _id: 547210496, total_listings: 1 },
  { _id: 449662778, total_listings: 1 },
  { _id: 453229602, total_listings: 1 },
  { _id: 9836276, total_listings: 1 },
  { _id: 8521814, total_listings: 1 },
  { _id: 550537818, total_listings: 1 },
  { _id: 12414611, total_listings: 1 },
  { _id: 550368379, total_listings: 1 },
  { _id: 64972585, total_listings: 1 },
  { _id: 545179285, total_listings: 1 },
  { _id: 79417889, total_listings: 1 }
]
Type "it" for more
```

### Find the average review_scores_rating per neighborhood, and only show those that are 4 or above, sorted in descending order of rating

```javascript
db.listings.aggregate([
...      { $group: { _id: "$neighbourhood_cleansed", average_rating: { $avg: "$review_scores_rating" } } },
...      { $match: { average_rating: { $gte: 4 } } },
...      { $sort: { average_rating: -1 } }
...    ])
```


```javascript
[
  { _id: 'Liesing', average_rating: 4.7939905134427985 },
  { _id: 'Döbling', average_rating: 4.768722591771372 },
  { _id: 'Josefstadt', average_rating: 4.754121286349162 },
  { _id: 'Wieden', average_rating: 4.750768406628369 },
  { _id: 'Neubau', average_rating: 4.747602269021976 },
  { _id: 'Innere Stadt', average_rating: 4.736504100641129 },
  { _id: 'Penzing', average_rating: 4.732053903842683 },
  { _id: 'Mariahilf', average_rating: 4.731167375536374 },
  { _id: 'Alsergrund', average_rating: 4.728490823363518 },
  { _id: 'Landstraße', average_rating: 4.72527020052918 },
  { _id: 'Donaustadt', average_rating: 4.712564657537411 },
  { _id: 'Simmering', average_rating: 4.712401569676746 },
  { _id: 'Brigittenau', average_rating: 4.699766026258683 },
  { _id: 'Meidling', average_rating: 4.6866687918875245 },
  { _id: 'Hernals', average_rating: 4.683787267338725 },
  { _id: 'Rudolfsheim-Fünfhaus', average_rating: 4.682146265520776 },
  { _id: 'Floridsdorf', average_rating: 4.675555609513288 },
  { _id: 'Währing', average_rating: 4.669469768779703 },
  { _id: 'Leopoldstadt', average_rating: 4.665109423964703 },
  { _id: 'Ottakring', average_rating: 4.656255943039626 }
]
Type "it" for more
```
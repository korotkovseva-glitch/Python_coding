/// Assignment Stata part, Hotels in Vienna clean data analysis ///

cd "C:\Users\Korotkov_Seva\Documents\Coding\Assignment" // Setting a working folder

import delimited "Clean_data\hotelbookingdata-vienna_clean.csv", clear // uploading a clean data from Python iteration

/// Creating labels for all variables

label variable rating_reviewcount "The number of reviews"
label variable center1distance "Distance from city centre in miles"
label variable center1label "City centre by default"
label variable center2distance "Distance from the center2label"
label variable center2label "Alternative point of calculation distance for hotels"
label variable neighbourhood "The name of Vienna's neighbourhoods"
label variable price "Price per room per night in USD"
label variable starrating "Number of stars of the hotel"
label variable accommodationtype "Type of accomodation (apartment, hotel, hostel, etc)"
label variable guestreviewsrating "Score of the hotel based on guest reviews (5 max)"
label variable hotel_id "ID of the hotel"

/// Creating additional variablles

generate center1distance_km=round(center1distance*1.60934,0.1) // creating variable with distance from city center in km
label variable center1distance_km "Distance from city centre in km"
describe center1distance_km // checking the type of variable

generate price_EUR=round(price*0.87,1)
// creating variable with price in EUR
label variable price_EUR "Price per room per night in EUR"
describe price_EUR // checking the type of variable
recast int price_EUR // because we have no demicals it's better to convert to int type
describe price_EUR // checking conversion

save"C:\Users\Korotkov_Seva\Documents\Coding\Assignment\Clean_data\hotelbookingdata-vienna_clean_stata.dta", replace // saveing an updated clean version in dta. format for further analysis


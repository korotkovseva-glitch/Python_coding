cd "C:\Users\Korotkov_Seva\Documents\Coding\Assignment" // Setting a working folder

use "Clean_data\hotelbookingdata-vienna_clean_stata.dta", clear // uploading a clean data from stata iteration

describe // data review

keep if accommodationtype=="Hotel" // considering only hotels in Vienna

by starrating, sort: summarize price_EUR // review of price by stars

keep if starrating == 3 | starrating == 4 | starrating == 5

/// Considering observatoins and results, it was maded a decision to look at 3, 4 and 5 stars hotels for analysis

by starrating, sort: summarize price_EUR // it was notices that price that max price for 3 and 5 stars hotels are quite high. So, it was made a decision eliminate it

drop if starrating == 3 & price_EUR>137 // excluding anomalies
drop if starrating ==5 & price_EUR>473 // excluding anomalies

by starrating, sort: summarize price_EUR, detail // check

by starrating, sort: summarize center1distance_km, detail // there is a huge step between 95% and 99% percentile. It was maded decision to eliminate the 3* hotels with distance exceeds 8.5 km

drop if starrating==3 & center1distance_km>8.5 // excluding anomaly

by starrating, sort: summarize center1distance_km, detail // checking

destring guestreviewsrating, replace //changing to numeric

/// Creating graphs

generate distance_cat="1km and below" if center1distance_km<=1
replace distance_cat="above 1 km" if center1distance_km>1

graph bar, over(distance_cat) over(starrating) stack asyvar percentage title("Distibution of hotels from city centre depending on stars")
graph export hotels_stars_distr_distance.pdf, replace

hist price_EUR if distance_cat=="1km and below", bin (20) percent title("Price (EUR per night) for located in 1 km and below")
graph export hotels_price_1km_and_below.pdf, replace


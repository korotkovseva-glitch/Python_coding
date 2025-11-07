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

by starrating, sort: summarize price_EUR, detail
by starrating, sort: summarize center1distance_km, detail
by starrating, sort: summarize guestreviewsrating, detail // it was noticed that guestreviewsrating is a string

destring guestreviewsrating, replace //changing to numeric

by starrating, sort: summarize guestreviewsrating, detail  // updated version

// Saving observations in word file with summary statistics
ssc install asdoc, replace
asdoc tabstat center1distance_km, by(starrating) ///
 statistics(N mean sd min max p5 p10 p50 p90 p95) ///
 save(hotels_distance_summary.doc) ///
 title(Summary statistics table depending on distance from city centre by hotel star) dec(2) replace
  
 asdoc tabstat price_EUR, by(starrating) ///
 statistics(N mean sd min max p5 p10 p50 p90 p95) ///
 save(hotels_price_summary.doc) ///
 title(Summary statistics table depending on price [EUR per night] by hotel star) dec(2) replace
  
 asdoc tabstat guestreviewsrating, by(starrating) ///
 statistics(N mean sd min max p5 p10 p50 p90 p95) ///
 save(hotels_guestreview_summary.doc) ///
 title(Summary statistics table depending on guest review rating [5 max] by hotel star) dec(2) replace
  

 
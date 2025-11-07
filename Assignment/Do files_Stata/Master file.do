/// It's master file for home assigment. The analysed data is 3,4,5 star hotels in Vienna. It's included 3 do files. Working with data file consider the following filtering and naming veriables as well as converting csv file in dta. Analysos of data includes summary statistics tables with following option of creating outputs in doc format. Graphs considers creation charts in pdf format for price and stars variable depending on distance

version 19
clear all
set more off

do "C:\Users\Korotkov_Seva\Documents\Coding\Assignment\Do files_Stata\Working with data.do"
do "C:\Users\Korotkov_Seva\Documents\Coding\Assignment\Do files_Stata\Analysis of data.do"
do "C:\Users\Korotkov_Seva\Documents\Coding\Assignment\Do files_Stata\Graphs.do"

display as text "All done."

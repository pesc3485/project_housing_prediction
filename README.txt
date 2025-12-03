# AUTHOR: PETER SCOTT - PESC3485
# PURPOSE: Can we predict the heat of US housing market based off of pending sales, price drops, and supply?
# USE: All graphs and algorithms are defined within queryspace.ipynb markdown file
# TECH USED: Pandas, DuckDB, Python, SQL
# Database -> City_market_tracker with 5.9 million line items : all files are ignored in this repo to save on median_sale_price
Repo can be found here: https://www.kaggle.com/datasets/vincentvaseghi/us-cities-housing-market-data
 

Database Notes:
The dataset has the following columns:

period_begin
period_end
period_duration
region_type
region_type_id
table_id
is_seasonally_adjusted. (indicates if prices are seasonally adjusted; f represents False)
region
city
state
state_code
property_type
property_type_id
median_sale_price
median_sale_price_mom (median sale price changes month over month)
median_sale_price_yoy (median sale price changes year over year)
median_list_price
median_list_price_mom (median list price changes month over month)
median_list_price_yoy (median list price changes year over year)
median_ppsf (median sale price per square foot)
median_ppsf_mom (median sale price per square foot changes month over month)
median_ppsf_yoy (median sale price per square foot changes year over year)
median_list_ppsf (median list price per square foot)
median_list_ppsf_mom (median list price per square foot changes month over month)
median_list_ppsf_yoy. (median list price per square foot changes year over year)
homes_sold (number of homes sold)
homes_sold_mom (number of homes sold month over month)
homes_sold_yoy (number of homes sold year over year)
pending_sales
pending_sales_mom
pending_sales_yoy
new_listings
new_listings_mom
new_listings_yoy
inventory
inventory_mom
inventory_yoy
months_of_supply
months_of_supply_mom
months_of_supply_yoy
median_dom (median days on market until property is sold)
median_dom_mom (median days on market changes month over month)
median_dom_yoy (median days on market changes year over year)
avg_sale_to_list (average sale price to list price ratio)
avg_sale_to_list_mom (average sale price to list price ratio changes month over month)
avg_sale_to_list_yoy (average sale price to list price ratio changes year over year)
sold_above_list
sold_above_list_mom
sold_above_list_yoy
price_drops
price_drops_mom
price_drops_yoy
off_market_in_two_weeks (number of properties that will be taken off the market within 2 weeks)
off_market_in_two_weeks_mom (changes in number of properties that will be taken off the market within 2 weeks, month over month)
off_market_in_two_weeks_yoy (changes in number of properties that will be taken off the market within 2 weeks, year over year)
parent_metro_region
parent_metro_region_metro_code
last_updated
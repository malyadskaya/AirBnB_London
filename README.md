# AirBnB_London

Let's imagin that there is no corona viruce and eople are travelling as usual to many different locations..

So I've decided to take the data from kaggle, it is Airbnb London Data analysis.
https://www.kaggle.com/ahmedatta/airbnb-london

Let's say one of the nephews of Roman Abramovich decided to buy few apartments for rent.
So we want to help to poor guy by analysing the areas.
So out question is - what housing type and where to buy?

There we have 5 yearly csv files starting from 2017 and pretend that we have full 2021.
So we're loading all the files to one df (like years are the batches) with additional yr column,
cleaning the data a bit, and saving to another files (also csv, not realistic but its imaginary etl, so..):
union data and some outliers for additional analysis.
Then we're uploading the files to databricks where we can create kinda db with not only union and outliers tables
but also smaller tables showing neighbourhoods statistics or tables for other needs - for hosts analysis for example.

https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/1960148774256339/289242420014320/7117132185040703/latest.html

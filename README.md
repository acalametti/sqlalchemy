# sqlalchemy

Contributor: Alex Calametti 

Overview: 

The main goal of this project is to analyze a climate database to visualize precipitation and temperature data collected from different weather stations in Hawaii before a planned vacation. This activity works to help gain more practice using SQLAlchemy and ORM queries as well as a website powered by FLask. The name of files used, programs needed, steps taken to create the vizualizations, and Flask set up are included below. 

What you need: 

-   Databases: hawaii.sqlite, hawaii_measurements.csv, hawaii_stations.csv

-   Libraries/Programs: Pandas, Matplotlib, SQLAlchemy, Flask

-   Starter Code: climate_starter.ipynb and app.py


Project Steps: 

-  Start by creating engine to hawaii.sqlite in the climate_starter code and reflect the database and tables using automap base
-  Save references for each table and create the session
-  Find the most recent data point in the database and use this to pull the last 12 months of data
-  Query the database to finde the precipitation score data, save as a pd.DataFrame and plot with Matplotlib
  

![Screen Shot 2023-10-28 at 12 56 53 PM](https://github.com/acalametti/sqlalchemy/assets/136642574/d9cba686-bf85-42f0-ba80-1381eb0e1336)

- Next query the database to find the active station to calculate the average, max, and min temperature
- Plot the last year of temperature observations from the most active station identified

   ![Screen Shot 2023-10-28 at 12 59 27 PM](https://github.com/acalametti/sqlalchemy/assets/136642574/99ba107f-ac00-463f-9819-255e62b9e3fc)


-  In the app.py set up the database similar to in the climate_starter by creating the engine, adding the tables, saving references to classes, and creating the engine
- Copy the code for finding the last 12 months of data into the Database Setup section
- Set up Flask Routes on the home page of the webpage to the precipitation, station, and tobs JSONs as well as a page that returns the avg, min, and max temp of a specified data
- Run flask in the terminal and follow the link to the homepage created

![Screen Shot 2023-10-28 at 1 12 17 PM](https://github.com/acalametti/sqlalchemy/assets/136642574/7e3c2deb-424f-449b-91f2-f541d61b4ca7)


Outside Contributors: 

Big thank you to Geronimo Perez for all of his help setting up the Flask routes! 

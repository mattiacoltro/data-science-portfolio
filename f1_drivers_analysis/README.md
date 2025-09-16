# Formula 1 Drivers Analysis

F1 Analytics specializes in analyzing the performance of drivers and teams in the world of Formula 1. The goal of this project is to analyze the results of the 2008 Formula 1 World Championship season using the data contained in the formula1_data.csv file.

This file contains detailed information about drivers, manufacturers, cities, and countries of Grand Prix races, as well as the finishing order of each driver. Based on this data, various functions will be implemented to provide an in-depth analysis of points, wins, and podium finishes at both the individual and manufacturer levels.

## Dataset

The dataset formula1_data.csv (downloadable from here: https://proai-datasets.s3.eu-west-3.amazonaws.com/formula1_data.csv) contains the following columns:
1. **Driver**: Name of the driver.
2. **Team**: Name of the manufacturer for which the driver competes.
3. **Race**: City where the Grand Prix took place.
4. **Country**: Country where the Grand Prix took place.
5. **Position**: Number between 0 and 8 indicating the driver's finishing order (0 means that the driver did not finish in the top 8 and did not score any points).

## Scoring system

At the end of each Grand Prix, points are awarded to drivers based on their finishing order as follows: 
- 1st place: 10 points 
- 2nd place: 8 points 
- 3rd place: 6 points 
- 4th place: 5 points 
- 5th place: 4 points 
- 6th place: 3 points 
- 7th place: 2 points 
- 8th place: 1 point 
- 9th place or lower: 0 points

## Project objectives

The project involves the implementation of the following features:

1. Function for analyzing **individual driver performance**

    The first function receives a driver's name as input and returns a list containing three key pieces of information:
    - The total points accumulated by the driver during the championship.
    - The number of wins, i.e., how many times the driver finished first in a Grand Prix. 
    - The number of podium finishes, i.e., how many times the driver finished in the top three. This function will be useful for analyzing the individual performance of drivers and providing a clear overview of their positions throughout the season.

2. Function for creating the **final driver standings**

    The second function generates a dictionary containing the names of the drivers as keys and their total scores as values. The dictionary is then used to create an overall driver standings.
    Finally, the standings will be saved in a text file (Drivers_Standings_2008.txt) with the
    following format:

    Drivers Standings 2008 Formula 1
    DriverName1: TotalPoints
    DriverName2: TotalPoints

3. Function for the **constructors' standings**

    The third function creates a dictionary with the names of the teams/constructors as keys and their total scores as values. Each team's score is the sum of the points obtained by the drivers who competed for that constructor.
    This function uses the data previously generated for the drivers and calculates the constructors' standings. This information is also essential for gaining a clear picture of the teams' performance throughout the year.


## Technologies
Python 

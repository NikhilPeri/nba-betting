#uOEC 2018 Programming Challenge

## Overview
Todays companies are sitting on mountains of data, and are increasingly looking for cleaver engineers
to structure this data and produce useful insights.

Since the rise of bitcoin people are more comfortable with gambling their money away online.
This years challenge is to channel you inner addictive gambler and marry that with your
dank coding skills to design an algorithm to make you rich (or entirely broke)

## Problem Statement
You are developing an algorithm to predict the outcomes of tonights NBA games based on any pre-grame data.
Your application must be able to read a csv file with the following schema

```
Month,Day,Year,Start (ET),Visitor,Home
```

And output computed predictions in the csv format

```
Month,Day,Year,Start (ET),Visitor,Home,Outcome,Confidence
```

| Outcome    | a value of either 'home' or 'away' representing the winning team          |
|------------|---------------------------------------------------------------------------|
| Confidence | an associated confidence score (0 to 1) of the prediction (bonus points)  |

At the end of the competition you will be required to predict tonights games only using any data sources you wish.
You may also use any programming language of choice, but a [jupyter notebook enviorment](http://jupyter.org/install.html) is recommended.

## Provided Data
The following two datasets are provided along with the scrapper that generated them which can be
found in `data/scrape_standings.py`. You are not limited to these datasets and are extremely encouraged to
construct your own based on the provided scrapper for things such as injuries, local vs visitor weather, player stats etc,.

#### data/2017schedule.csv
This file contains a list of all games in the 2017 regular season along with the points for completed games.

```
Month,Day,Year,Start (ET),Visitor,Visitor PTS,Home,Home PTS,Score,,Notes
```
For games which are yet to be completed the points value is empty along with the Score

#### data/nba.db
This [sqlite](https://docs.python.org/2/library/sqlite3.html) database contains team standings for various dates throught the 2017 regular season
The following values are included:
- date
- team_name text
- games integer
- minutes integer
- field_goals integer
- field_goal_attempts integer
- field_goal_percentage decimal
- three_points integer
- three_point_attempts integer
- three_point_percentage decimal
- two_points integer
- two_point_attempts integer
- two_point_percentage decimal
- free_throws integer
- free_throw_attempts integer
- free_throw_percentage integer
- offensive_rebounds integer
- defensive_rebounds integer
- total_rebounds integer
- assists integer
- steals integer
- turn_overs integer
- personal_fouls integer
- points integer

## Evaluation
The following is the grid for evaluation, the team with the most points after evaluation wins
| Criteria                           | Max Points | Description                                                                                                                                                                                                               |
|:------------------------------------|:------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code Quality                       | 30         |  <ul><li>Readability of the code</li><li>Functionality of the code</li><li>This score is based entirely on judges</li></ul>                                                                                                                        |
| Additional Data Sources            | 20         |  <ul><li>The use of additional relevant data sources</li><li>no points given for using irrelevant data sources regardless of how correlated (ex. babies born before game day)</li><li>5 points per data source</ul>                            |
| Prediction Algorithm               | 40         |  <ul><li>The understanding and ability to explain the Prediction Algorithm used  </li><li>The quality of features selected for algorithm  </li><li>Presentation of feature research in the form of graphs and charts to identify key features</ul> |
| Predicting the games for the night | 10         |  `score = sum(confidence * outcome)` where outcome is +1 for correct geuss and -1 for incorrect geuss                                                                                                                     |

## Submissions
In order to create a submission you must fork this repositiory by clicking the `Fork` button on the main page
As soon as you have forked the repository please submit the link to the competition organizer,
your repository must be public to be graded
you can then push commits to your forked version.  

# Go Get IT
![Go Get IT](https://giphy.com/gifs/lebron-james-nba-finals-super-saiyan-3oEdv2qNBprY4gDxMk?utm_source=media-link&utm_medium=landing&utm_campaign=Media%20Links&utm_term=https://www.google.ca/)

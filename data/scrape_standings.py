import csv
import sqlite3
import urllib2
import urllib
import pdb
from bs4 import BeautifulSoup, Comment

def standings(day, month, year, database):
    url = "https://www.basketball-reference.com/friv/standings.fcgi?" + urllib.urlencode({'day': day, 'month': month, 'year': year})
    print 'request -> ' + url
    page = urllib2.urlopen(url).read()
    doc = BeautifulSoup(page)

    for comment in doc.findAll(text=lambda text:isinstance(text, Comment)):
        soup = BeautifulSoup(str(comment))
        table = soup.find('table', {'id' : 'team'})
        if table == None:
            continue

        for row in table.find_all('tr')[1:31]:
            rank = int(row.find('th', {'data-stat': 'ranker'}).getText())
            team_name =  str(row.find('td', {'data-stat': 'team_name'}).find('a').getText())
            games = int(row.find('td', {'data-stat': 'g'}).getText())
            minutes = int(row.find('td', {'data-stat': 'mp'}).getText())

            field_goals = int(row.find('td', {'data-stat': 'fg'}).getText())
            field_goal_attempts = int(row.find('td', {'data-stat': 'fga'}).getText())
            field_goal_percentage = float(row.find('td', {'data-stat': 'fg_pct'}).getText())

            three_points = int(row.find('td', {'data-stat': 'fg3'}).getText())
            three_point_attempts = int(row.find('td', {'data-stat': 'fg3a'}).getText())
            three_point_percentage = float(row.find('td', {'data-stat': 'fg3_pct'}).getText())

            two_points = int(row.find('td', {'data-stat': 'fg2'}).getText())
            two_point_attempts = int(row.find('td', {'data-stat': 'fg2a'}).getText())
            two_point_percentage = float(row.find('td', {'data-stat': 'fg2_pct'}).getText())

            free_throws = int(row.find('td', {'data-stat': 'ft'}).getText())
            free_throw_attempts = int(row.find('td', {'data-stat': 'fta'}).getText())
            free_throw_percentage = float(row.find('td', {'data-stat': 'ft_pct'}).getText())

            offensive_rebounds = int(row.find('td', {'data-stat': 'orb'}).getText())
            defensive_rebounds = int(row.find('td', {'data-stat': 'drb'}).getText())
            total_rebounds = int(row.find('td', {'data-stat': 'trb'}).getText())

            assists = int(row.find('td', {'data-stat': 'ast'}).getText())
            steals = int(row.find('td', {'data-stat': 'stl'}).getText())
            blocks = int(row.find('td', {'data-stat': 'blk'}).getText())
            turn_overs = int(row.find('td', {'data-stat': 'tov'}).getText())
            personal_fouls = int(row.find('td', {'data-stat': 'pf'}).getText())
            points = int(row.find('td', {'data-stat': 'pts'}).getText())

            date = str(year) + '-' + str(month) + '-' + str(day)
            try:
                database.execute("INSERT INTO standings VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                  [date, team_name, games, minutes,
                  field_goals, field_goal_attempts, field_goal_percentage,
                  three_points, three_point_attempts, three_point_percentage,
                  two_points, two_point_attempts, two_point_percentage,
                  free_throws, free_throw_attempts, free_throw_percentage,
                  offensive_rebounds, defensive_rebounds, total_rebounds,
                  assists, steals, turn_overs, personal_fouls, points])
                database.commit()
                print date + ' | team: ' + team_name
            except:
                print 'FAILED ' + date + ' | team: ' + team_name

create_table_query = '''
CREATE TABLE IF NOT EXISTS standings (
 date text NOT NULL,
 team_name text NOT NULL,
 games integer NOT NULL,
 minutes integer NOT NULL,
 field_goals integer NOT NULL,
 field_goal_attempts integer NOT NULL,
 field_goal_percentage decimal NOT NULL,
 three_points integer NOT NULL,
 three_point_attempts integer NOT NULL,
 three_point_percentage decimal NOT NULL,
 two_points integer NOT NULL,
 two_point_attempts integer NOT NULL,
 two_point_percentage decimal NOT NULL,
 free_throws integer NOT NULL,
 free_throw_attempts integer NOT NULL,
 free_throw_percentage integer NOT NULL,
 offensive_rebounds integer NOT NULL,
 defensive_rebounds integer NOT NULL,
 total_rebounds integer NOT NULL,
 assists integer NOT NULL,
 steals integer NOT NULL,
 turn_overs integer NOT NULL,
 personal_fouls integer NOT NULL,
 points integer NOT NULL
);
'''
create_index_query= '''
CREATE UNIQUE INDEX IF NOT EXISTS index_id
ON standings (date, team_name);
'''

database = sqlite3.connect('nba.db')
database.execute(create_table_query)
database.commit()
database.execute(create_index_query)
database.commit()

for month  in [1, 2, 3, 4, 5]:
    for day in range(1, 31):
        try:
            standings(day, month, 2018, database)
        except:
            print 'FAILED DAY ' + str(day) + '-' + str(month) + '-' + str(2017)

database.close()

#!/usr/bin/env python

""" mlbApp.py: small script to grab today's score for a given MLB team 
    and display in the command line.
    
    This project is for scraping MLB data from mlb.com's gd2 backend.
	Please follow the fair use guidelines at http://gdx.mlb.com/components/copyright.txt
"""

import sys
import datetime
import urllib2
import xml.etree.ElementTree as ET

__author__ = "Nathan Bryans"
__version__ = "1.0"

def parseArguments(team="Mariners", action="score"):
    return [team, action]

def generateQuery(offset):
    dt = getDate(offset)
    q_str = "http://gd2.mlb.com/components/game/mlb/year_%s/month_%s/day_%s/master_scoreboard.xml"  \
            % (str(dt.year), str(dt.month).zfill(2), str(dt.day).zfill(2))
    return q_str
    
def queryData(counter):
    query = generateQuery(counter)
    xmlData = urllib2.urlopen(query)
    tree = ET.parse(xmlData)
    return tree.getroot()
    
def getDate(offset):
    return datetime.date.fromordinal(datetime.datetime.today().toordinal()+offset)
    
def getGameState(game_xml, homeTeam, awayTeam):
    status = ""
    home_score = "-"
    away_score = "-"
    for child in game_xml:
        if "status" in child.tag:
            status = child.attrib['status']
        elif "linescore" in child.tag:
            for inner_child in child:
                if "r" == inner_child.tag:
                    home_score = inner_child.attrib['home']
                    away_score = inner_child.attrib['away']
    str1 = "%s:%s\t%s:%s\t%s" % (awayTeam, away_score, homeTeam, home_score, status)
    
    if "Preview" in status:
        str1 += "\t%s %s"  % (game_xml.attrib['time'], game_xml.attrib['time_zone'])
    else:
        str1 += "\t%s" % (game_xml.attrib['original_date'])
    return str1
    
def getTeamSchedule(game_xml, homeTeam, awayTeam):
    return "%s\t%s @ %s\t%s %s" % (game_xml.attrib['original_date'], awayTeam, homeTeam, game_xml.attrib['time'], game_xml.attrib['time_zone'])
    
# Main Script
numDaysLookAhead = 3
found = 0
counter = 0

# Parse and format arguments
if len(sys.argv) > 3:
    print "Too many arguments, exiting."
    exit()

team, action = parseArguments(*sys.argv[1:])
team = team.replace('_', ' ')



if "score" in action:
    while True:
        games = queryData(-counter)

        for game in games:
            if team in [game.attrib['home_team_name'] , game.attrib['away_team_name']]:
                homeTeam = game.attrib['home_team_name']
                awayTeam = game.attrib['away_team_name']
                print getGameState(game, homeTeam, awayTeam)
                exit(0)      

        counter += 1
        if counter > 2:
            print "No games within 3 days. Check spelling of team name"
            print "Represent spaces with an underscore (i.e. \"Blue_Jays\")"
            exit(-1)

elif "schedule" in action:
    print "Upcoming games for %s in next %s days." % (team, str(numDaysLookAhead))
    for i in range(0, numDaysLookAhead):
        games = queryData(i+1)

        for game in games:
            if team in [game.attrib['home_team_name'] , game.attrib['away_team_name']]:
                homeTeam = game.attrib['home_team_name']
                awayTeam = game.attrib['away_team_name']
                print getTeamSchedule(game, homeTeam, awayTeam)

exit(0)



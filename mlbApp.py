#!/usr/bin/env python

""" mlbApp.py: small script to grab score or schedule for a given MLB team.

    Using MLB data from http://gd2.mlb.com/components/game/mlb/
    Please review the terms of copyright before forking/using
    to verify you are in agreement with their terms. 
"""

import sys
import datetime
import urllib2
import xml.etree.ElementTree as ET

__author__ = "Nathan Bryans"
__version__ = "1.1"

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
                    if (int(home_score) > int(away_score)):
                        home_score += '*'
                    else:
                        away_score += '*'   

    str1 = "{0: <12}:{1: <3}  {2: <12}:{3: <3}\t{4: <10}".format(awayTeam, away_score, homeTeam, home_score, status)
    
    if "Preview" in status:
        str1 += "{0} {1}".format(game_xml.attrib['time'], game_xml.attrib['time_zone'])
    else:
        str1 += "{0}".format(game_xml.attrib['original_date'])   
    return str1
    
def getTeamSchedule(game_xml, homeTeam, awayTeam):
    return "%s\t%s @ %s\t%s %s" % (game_xml.attrib['original_date'], awayTeam, homeTeam, game_xml.attrib['time'], game_xml.attrib['time_zone'])

def printHelp():
    print("mlbApp.py: small script to grab score or schedule for a given MLB team.")
    print("\nUsage:\n")
    print("./mlbApp.py score Mariners")
    print("./mlbApp.py schedule Tigers")
    print("\n")
    print("Non-Obvious Team Names:\nBlue_Jays\nD-backs\nAngels\nWhite_Sox\nRed_Sox")



actions = ['score', 'schedule']
numDaysLookAhead = 3
numDaysLookBehind = 3

if __name__ == "__main__":
    if len(sys.argv) > 3:
        print("Too many arguments, exiting.")
        exit()
        
    team, action = parseArguments(*sys.argv[1:])

    if team == '-h' or team == '-help':
        printHelp()
        exit(0)

    if (team.lower() in actions): #If user gave opposite order
        team, action = action, team

    team = team.replace('_', ' ')

    found = 0
    counter = 0

    if "score" in action:
        foundGame = 0
        while True:
            games = queryData(-counter)
               
            for game in games:
                if team in [game.attrib['home_team_name'] , game.attrib['away_team_name']]:
                    homeTeam = game.attrib['home_team_name']
                    awayTeam = game.attrib['away_team_name']
                    print(getGameState(game, homeTeam, awayTeam))
                    foundGame = 1
                    
            counter += 1
            if counter > numDaysLookBehind: 
                if not foundGame:
                    print("No games within 3 days. Check spelling of team name (use -h for help)")
                    print("Represent spaces with an underscore (i.e. \"Blue_Jays\")")
                    exit(-1)
                else:
                    exit(0)
                
    elif "schedule" in action:
        print("Upcoming games for %s in next %s days:" % (team, str(numDaysLookAhead)))
        for i in range(0, numDaysLookAhead):
            games = queryData(i+1)
            
            for game in games:
                if team in [game.attrib['home_team_name'] , game.attrib['away_team_name']]:
                    homeTeam = game.attrib['home_team_name']
                    awayTeam = game.attrib['away_team_name']
                    print(getTeamSchedule(game, homeTeam, awayTeam))
                    
        exit(0)
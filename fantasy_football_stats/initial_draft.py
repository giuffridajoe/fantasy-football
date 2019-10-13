import requests
from FantasyFootballPlayer import FantasyFootballPlayer

def getPlaceFinished(placeFinished):
	placeAndOrdinal = ""
	if placeFinished == 1:
		placeAndOrdinal = placeFinished + "st place"
	elif placeFinished == 2:
		placeAndOrdinal = placeFinished + "nd place"
	elif placeFinished == 3:
		placeAndOrdinal = placeFinished + "rd place"
	else:
		placeAndOrdinal = placeFinished + "th place"
	return placeAndOrdinal
	
	
def playerFinishedInMoney(placeFinished):
	return placeFinished == 1 or placeFinished == 2 or placeFinished == 3
	
def playerFinishedInFirst(placeFinished):
	return placeFinished == 1
	
def playerFinishedInLast(placeFinished):
	return placeFinished == 10
	
def getPlayerName(guid)
	playerName = ""
	
	if guid == "{CA683308-66E8-4172-9891-D8C2A8A09FE4}":
		playerName = 'Bob'
	elif guid = "{797A0B2F-9B4F-4231-9264-5EAB154EEC2C}":
		playerName = 'Steve'
	elif guid = "{FED936E0-0A6F-43DB-87B5-ABE7B0A65799}":
		playerName = "Me"
	elif guid = "{66B8630F-0CBE-4B4E-BFD5-192B09C489DE}":
		playerName = 'Joe Viti'
	elif guid = "{6B60B179-6FD4-44EA-BEEB-5452F6B1180B}":
		playerName = 'Shannon' 	
	elif guid = "{3963B88C-28F7-45C1-8781-FB276E18AA17}":
		playerName = "Joe Vaccaro"
	elif guid = "{1B97B44B-B739-4670-8518-895EB6B80B36}":
		playerName = "Eric"
	elif guid = "{C6F97B7E-6150-4797-9CB5-F932C1958463}":
		playerName = "Sean"
	elif guid = "{1892C10F-CD14-4EAF-A701-47870982F254}":
		playerName = "Ed"
	elif guid = "{A31A37BD-0B9F-4C8C-B6E2-5878858F9C3D}":
		playerName = "Little"
		
	return playerName
	

#url = "https://fantasy.espn.com/[insert base url here]/[league id here]?view=kona_history_standings"

result = requests.get(url,
                 cookies={"swid": "",
                          "espn_s2": ""})
data = result.json()
ffTeams = data[0]['teams']
yearsInMoney = []
yearsInFirst = []
yearsInLast = []

for season in data:
	print "\nFor the %s" % season['seasonId'] + " season: "
	
	for team in ffTeams:
		print "\t" + team['location'] + ' ' +team['nickname'] + " finished in %s" % getPlaceFinished(team['rankCalculatedFinal'])
		
		if playerFinishedInMoney(team['rankCalculatedFinal']):
			yearsInMoney = season['seasonId']
			
		if playerFinishedInFirst(team['rankCalculatedFinal']):
			yearsInFirst = season['seasonId']
			
		if playerFinishedInLast(team['rankCalculatedFinal']):
			yearsInLast = season['seasonId']
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
		
import requests
from fantasy-football import FantasyFootballPlayer

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
'''
#url = "https://fantasy.espn.com/[insert base url here]/[league id here]?view=kona_history_standings"
url = https://fantasy.espn.com/apis/v3/games/ffl/leagueHistory/335710?view=kona_history_standings

result = requests.get(url,
                 cookies={"swid": "{FED936E0-0A6F-43DB-87B5-ABE7B0A65799}",
                          "espn_s2": "AEBhXr8Qs6HGmsmcyO3TQuM3AAmuHY0025XShVp9lvxL4rgf524Yf2my9HR9sOoHaqMtJvu2fG0UnlB28IVKAIliTwoJ"})
data = result.json()
ffTeams = data[0]['teams']

for season in data:
	print "\nFor the %s" % season['seasonId'] + " season: "
	for team in ffTeams:
		print "\t" + team['location'] + ' ' +team['nickname'] + " finished in %s" % getPlaceFinished(team['rankCalculatedFinal'])'''

ffPlayer = FantasyFootballPlayer("Bob")

ffPlayer.printName() 
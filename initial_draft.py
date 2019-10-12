import requests

def correctOrdinal(placeFinished):
	ordinal = ""
	if placeFinished == 1:
		ordinal = "st place"
	elif placeFinished == 2:
		ordinal = "nd place"
	elif placeFinished == 3:
		ordinal = "rd place"
	else:
		ordinal = "th place"
	return ordinal

url = "https://fantasy.espn.com/[insert base url here]/[league id here]?view=kona_history_standings"

r = requests.get(url,
                 cookies={"swid": "put cookie here",
                          "espn_s2": "put cookie here"})
d = r.json()
ffTeams = d[0]['teams']

for season in d:
	print "\nFor the %s" % season['seasonId'] + " season: "
	for team in ffTeams:
		print "\t" + team['location'] + ' ' +team['nickname'] + " finished in %s" % team['rankCalculatedFinal'] + correctOrdinal(team['rankCalculatedFinal']) 


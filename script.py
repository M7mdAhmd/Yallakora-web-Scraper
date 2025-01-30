import requests
from bs4 import BeautifulSoup
import lxml
import csv

date = input("Enter the date at the format of MM/DD/YYYY : ")
pageURL = f"https://www.yallakora.com/match-center/%d9%85%d8%b1%d9%83%d8%b2-%d8%a7%d9%84%d9%85%d8%a8%d8%a7%d8%b1%d9%8a%d8%a7%d8%aa?date={date}#matchesclipNext"

def main(URL):
    rawData = requests.get(URL).content
    data = BeautifulSoup(rawData, "lxml")
    champions = data.find_all("div", {"class":"matchCard"})
    def campionData(championsList):
        championsData = []
        for champion in championsList:
            ChampionTitle = champion.contents[1].find("h2").text.strip() # == champion.find("div", {"class":"title"}).find("h2").text.strip()
            championMatches = champion.contents[3].find_all("div", {"class":"item"})
            for match in championMatches:
                championTitle = ChampionTitle
                week = match.find("div", {"class":"allData"}).find("div", {"class":"date"}).text.strip()
                status = match.find("div", {"class":"allData"}).find("div", {"class":"matchStatus"}).text.strip()
                teamA = match.find("div", {"class":"allData"}).find("div", {"class":"teamsData"}).find("div", {"class":"teamA"}).text.strip()
                teamB = match.find("div", {"class":"allData"}).find("div", {"class":"teamsData"}).find("div", {"class":"teamB"}).text.strip()
                result = match.find("div", {"class":"allData"}).find("div", {"class":"teamsData"}).find("div", {"class":"MResult"}).find_all("span", {"class":"score"})
                time= match.find("div", {"class":"allData"}).find("div", {"class":"teamsData"}).find("div", {"class":"MResult"}).find("span", {"class":"time"}).text.strip()
                matchResult = f"{result[0].text.strip()}-{result[1].text.strip()}"
                matchData = {"Champion":championTitle, "Week":week, "Status":status, "First Team":teamA, "Second Team":teamB, "Result":matchResult, "Time":time}
                championsData.append(matchData)
        return championsData
    return campionData(champions)
outputData = main(pageURL)
keys = ["Champion", "Week", "Status", "First Team", "Second Team", "Result", "Time"]
with open("Scraped-Data.csv", "w", encoding='utf-8') as file:  # encoding here is vital as the scraping is on Arabic data.
    o = csv.DictWriter(file, keys)
    o.writeheader()
    o.writerows(outputData)
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
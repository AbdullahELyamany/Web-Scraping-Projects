
"""
 Find out day's matches from the Yallakora website, enter day's date to find out all the matches on this day

 Created by *Abdullah EL-Yamany*


 YouTube Channel => *Codezilla*
 Video Link => https://youtu.be/taL3r_JpwBg


 Note => An error can occur if the site has been modified
      => After running the code, you can go to the csv file.  to see the results

"""

import requests
from bs4 import BeautifulSoup
import csv


date = input("Please Enyrt a Date DD/MM/YYYY: ")
date1 = date.strip().split("/")
date2 = f"{date1[1]}/{date1[0]}/{date1[2]}"

page = requests.get(f"https://www.yallakora.com/Match-Center/?date={date2}")



def main(page):

    src = page.content  # Content of Page (Page code)

    soup = BeautifulSoup(src, "lxml") # Show The Content from Beautiful Look


    matches_details = []

    championaships = soup.find_all("div", {'class': 'matchCard'}) # return list of all in class="matchCard"

    number_of_championaships = len(championaships)



    def get_match_info(championaships): 

        championaship_title = championaships.contents[1].find('h2').text.strip() # return text within h2 => cham..title
        print(f"## {championaship_title} ##=>>")

        all_matches = championaships.contents[3].find_all('li') # List of all Items in <li>

        number_of_matches = len(all_matches)


        for i in range(number_of_matches):
                # get team names
            team1 = all_matches[i].find('div', {'class': 'teamA'}).text.strip()
            team2 = all_matches[i].find('div', {'class': 'teamB'}).text.strip()
            
                # get score
            match_result = all_matches[i].find('div', {'class': 'MResult'}).find_all('span', {'class', 'score'})
            score = f"{match_result[0].text.strip()} - {match_result[1].text.strip()}"
            
                # get match time
            match_time = all_matches[i].find('div', {'class': 'MResult'}).find('span', {'class', 'time'}).text.strip()

            matches_details.append({"Name Of Championaships": championaship_title,
                                    "First Team": team1,
                                    "Second Team": team2,
                                    "Match Time": match_time,
                                    "Match Result": score
                                   })

            print(f"{team1}  {score}  {team2} -time->({match_time})")
            

    for n in range(number_of_championaships):
        
        get_match_info(championaships[n]) # return first Items in list of class="matchCard"



    keys = matches_details[0].keys()

    with open('matches_details.csv', 'w') as csv_file :

        dict_writer = csv.DictWriter(csv_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(matches_details)
        print("All Done!")


main(page)


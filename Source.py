from bs4 import BeautifulSoup
import requests
def get_data(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.text,'lxml')
    new_testss=soup.select('tr:has(td)')
    data=[]
    for new_test in new_testss:
        player_namessss = new_test.find('a', class_='playerName').text.strip()
        total_bigchances_missed = new_test.find('td',class_='mainStat text-centre').text.strip()
        ranks = new_test.find('td', class_='rank').text.strip()
        
        data.append({'player_names':player_namessss,
        'total_bigchances_missed':total_bigchances_missed,
        'ranks':ranks})
    return data
    


get_data('https://www.premierleague.com/stats/top/players/big_chance_missed')
import pandas as pd
def export_data(data):
    df=pd.DataFrame(data)
    df.to_csv("name of players with most big chances missed.csv")

if __name__ == '__main__':
    data=get_data('https://www.premierleague.com/stats/top/players/big_chance_missed')
    export_data(data)
    print('Done')




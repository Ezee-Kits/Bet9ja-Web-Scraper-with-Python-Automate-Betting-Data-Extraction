from func import selenium_init,scrolling,requesting_init,saving_files,drop_duplicate,saving_path_csv
from bs4 import BeautifulSoup



def bet9ja_func():
    path = f'{saving_path_csv}/BET9JA.csv'
    driver,wait,EC,By = selenium_init()
    url = 'https://sports.bet9ja.com/mobile/dailyBundle/soccer/1-1000'

    driver.get(url)

    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wrapper"]/main/div/div[6]')))
    except:
        pass

    scrolling(driver=driver)

    source = driver.page_source
    soup = BeautifulSoup(source,'html.parser')


    match_time = [ x.text.split('●')[0] for x in soup.find_all('div',class_='match-content__row--info')]

    teams = [ x.text for x in soup.find_all('div',class_='match-content__row--team')]
    home_team = [teams[x] for x in range(len(teams)) if x%2 == 0]
    away_team = [teams[x] for x in range(len(teams)) if x%2 == 1]

    odds = [ x.text for x in soup.find_all('div',class_='bets__item')]
    home_odd = [ odds[x] for x in range(0,len(odds),3)]
    draw_odd = [ odds[x]  for x in range(1,len(odds),3)]
    away_odd = [ odds[x]  for x in range(2,len(odds),3)]
    bookmaker = ['BET9JA']*len(away_odd)


    data = {
        'TIME':match_time,
        'HOME TEAM':home_team,
        'AWAY TEAM':away_team,

        'HOME ODD': home_odd,
        'DRAW ODD':draw_odd,
        'AWAY ODD':away_odd,
        'BOOKMAKER':bookmaker
    }

    saving_files(data=data,path=path)
    drop_duplicate(path=path)

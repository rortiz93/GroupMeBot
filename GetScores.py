
import bs4
import re
import requests


def get_matchup_score(full_text, league_id, season_id, league_size):
    leagueId = league_id # insert your ESPN leagueId
    seasonId = season_id  # insert season year
    scoreboardUrl = 'http://games.espn.com/ffl/scoreboard?leagueId=%s&seasonId=%s' % (leagueId, seasonId)
    res = requests.get(scoreboardUrl)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    scores_tag = soup.find_all(class_='score')
    names_tag = soup.find_all(class_='name')
    owners_tag = soup.find_all(class_='owners')

    for i in range(0, league_size):
        score_content_line1 = names_tag[i].get_text() + ': ' + scores_tag[i].get_text()
        if i in range(1, league_size, 2):
            score_content_line2 = names_tag[i - 1].get_text() + ': ' + scores_tag[i - 1].get_text()
        else:
            score_content_line2 = names_tag[i + 1].get_text() + ': ' + scores_tag[i + 1].get_text()

            full_text += (score_content_line1 + ' vs ' + score_content_line2 + '\n')


        i += 1
    return full_text

# not working right now because ESPN is asking for log in unlike the football URL
def get_baseball_matchup_score(full_text, league_id, season_id, league_size):
    leagueId = league_id # insert your ESPN leagueId
    seasonId = season_id  # insert season year
    scoreboardUrl = 'http://games.espn.com/flb/scoreboard?leagueId=%s&seasonId=%s' % (leagueId, seasonId)
    res = requests.get(scoreboardUrl)
    print(res.text)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    #scores_tag = soup.find_all(class_='teamScore')
    names_tag = soup.find_all('td', class_='teamName')
    #owners_tag = soup.find_all(class_='owners')
    for i in names_tag:
        print(i.get_text())
    '''
    for i in range(0, league_size):
        score_content_line1 = names_tag[i].get_text() + ': ' + scores_tag[i].get_text()
        if i in range(1, league_size, 2):
            score_content_line2 = names_tag[i - 1].get_text() + ': ' + scores_tag[i - 1].get_text()
        else:
            score_content_line2 = names_tag[i + 1].get_text() + ': ' + scores_tag[i + 1].get_text()

            full_text += (score_content_line1 + ' vs ' + score_content_line2 + '\n')


        i += 1
        '''
    print(names_tag)
    return full_text

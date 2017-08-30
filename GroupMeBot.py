import GetScores
from groupy import Group, Bot


# list of my GroupMe groups
groups = Group.list()

botId = 'c3ff35c4f554a9fa8525878d15'
groupId = '33275265'
full_text = ''
league_id = '458388'
season_id = '2017'
league_size = 16

# loop through GroupMe Groups and find desired group based off the group id.
for g in groups:
    if g.group_id == groupId:
        group = g

# assign the bot to the correct bot ID from the bot list
for bot in Bot.list():
    if bot.bot_id == botId:
        testBot = bot


# bot setup to print what is desired within the groupme

#testBot.post("test")

def send_message(full_text):
    full_text = GetScores.get_matchup_score(full_text, league_id, season_id, league_size)
    testBot.post(full_text)


full_text = GetScores.get_matchup_score(full_text, league_id, season_id, league_size)
testBot.post(full_text)



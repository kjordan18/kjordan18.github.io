from pybaseball import statcast_single_game, statcast
import pandas as pd
import numpy as np

firstGameID = 529406
lastGameID = 531060
bullpenGames = [530171, 530252, 530342, 530409, 530463, 530487, 
                530535, 530616, 530644, 530729, 530775, 530852, 
                530881, 530938, 530982, 531017, 531051, 530090, 530105, 530156, 530186, 530266]
# data = pd.DataFrame(statcast_single_game(531000))
# data = pd.read_csv('firstGameData.csv')
# data1 = statcast('2018-04-01', '2018-04-06')
# pd.set_option('display.max_columns', None)
# data.to_csv('lastGameData.csv')
# print(data)

firstGameID2017 = 490106
games1 = 3
games = 1654
games2017 = 2406
game_list = []
counter = 0
for i in range(games2017):
    nextGame = firstGameID2017 + counter
    game_list.append(nextGame)
    counter = counter + 1

gamesSkipped = 0
counter = 0
gameList = []


for i in game_list:
    print(i)
    try:
        data = statcast_single_game(i)
        eventsData = data['events'].dropna()
        pitchData = data['pitch_type']
        inning = data['inning_topbot']
        current_pitcher = data['pitcher'][0]
        home_score = data['home_score'][0]
        road_score = data['away_score'][0]
        home_team = data['home_team'][0]
        road_team = data['away_team'][0]
        home_pitcher_id = []
        road_pitcher_id = []
        home_pitcher = True
        away_pitcher = False
        bullpenGameHome = 0
        bullpenGameRoad = 0
        out_count = 0
        home_win = 0
        road_win = 0
        fastballVeloHome = 0
        breakingballVeloHome = 0
        changeupVeloHome = 0
        fastballSpinHome = 0
        breakingballSpinHome = 0
        changeupSpinHome = 0
        fastballCounterHome = 0
        breakingballCounterHome = 0
        changeupCounterHome = 0
        fastballVeloRoad = 0
        breakingballVeloRoad = 0
        changeupVeloRoad = 0
        fastballSpinRoad = 0
        breakingballSpinRoad = 0
        changeupSpinRoad = 0
        fastballCounterRoad = 0
        breakingballCounterRoad = 0
        changeupCounterRoad = 0
        homeWOBA = 0
        roadWOBA = 0
        homeISO = 0
        roadISO = 0
        homeCount = 0
        roadCount = 0

        for v in bullpenGames:
            if (v == i and home_team == "TB"):
                bullpenGameHome = 1
            elif (v == i and road_team == "TB"):
                bullpenGameRoad = 1
            else:
                continue
        
        for i,v in inning.items():
            if v == 'Top':
                home_pitcher = True
                road_pitcher = False
                home_pitcher_id.append(data['pitcher'][0])
                # print("Inning Loop Home Current Pitcher")
                # print(data['pitcher'][0])
                
            elif v == 'Bot':
                home_pitcher = False
                road_pitcher = True
                road_pitcher_id.append(data['pitcher'][0])
                # print("Inning Loop Road Current Pitcher")
                # print(data['pitcher'][0])

        for i,v in eventsData.items():

            if v == 'field_out':
                out_count = out_count + 1
                current_pitcher = data['pitcher'][i]
                if home_pitcher == True:
                    homeWOBA += data['woba_value'][i]
                    homeISO += data['iso_value'][i]
                    homeCount += 1
                else:
                    roadWOBA += data['woba_value'][i]
                    roadISO += data['iso_value'][i]
                    roadCount += 1
            elif v == 'force_out':
                out_count = out_count + 1
                current_pitcher = data['pitcher'][i]
                if home_pitcher == True:
                    homeWOBA += data['woba_value'][i]
                    homeISO += data['iso_value'][i]
                    homeCount += 1
                else:
                    roadWOBA += data['woba_value'][i]
                    roadISO += data['iso_value'][i]
                    roadCount += 1
            elif v == 'strikeout':
                out_count = out_count + 1
                current_pitcher = data['pitcher'][i]
            elif v == 'caught_stealing_2b':
                out_count = out_count + 1
                current_pitcher = data['pitcher'][i]
            elif v == 'caught_stealing_3b':
                out_count = out_count + 1 
                current_pitcher = data['pitcher'][i]
            elif v == 'caught_stealing_1b':
                out_count = out_count + 1   
                current_pitcher = data['pitcher'][i]
            elif v == 'grounded_into_double_play':
                out_count = out_count + 2
                current_pitcher = data['pitcher'][i]
                if home_pitcher == True:
                    homeWOBA += data['woba_value'][i]
                    homeISO += data['iso_value'][i]
                    homeCount += 1
                else:
                    roadWOBA += data['woba_value'][i]
                    roadISO += data['iso_value'][i]
                    roadCount += 1
            elif v == 'double_play':
                out_count = out_count + 2
                current_pitcher = data['pitcher'][i]
                if home_pitcher == True:
                    homeWOBA += data['woba_value'][i]
                    homeISO += data['iso_value'][i]
                    homeCount += 1
                else:
                    roadWOBA += data['woba_value'][i]
                    roadISO += data['iso_value'][i]
                    roadCount += 1
            elif v == 'grounded_into_triple_play':
                out_count = out_count + 3
                current_pitcher = data['pitcher'][i]
                if home_pitcher == True:
                    homeWOBA += data['woba_value'][i]
                    homeISO += data['iso_value'][i]
                    homeCount += 1
                else:
                    roadWOBA += data['woba_value'][i]
                    roadISO += data['iso_value'][i]
                    roadCount += 1
            elif v == 'triple_play':
                out_count = out_count + 3
                current_pitcher = data['pitcher'][i]
                if home_pitcher == True:
                    homeWOBA += data['woba_value'][i]
                    homeISO += data['iso_value'][i]
                    homeCount += 1
                else:
                    roadWOBA += data['woba_value'][i]
                    roadISO += data['iso_value'][i]
                    roadCount += 1

            elif v == 'walk':
                current_pitcher = data['pitcher'][i]
                if home_pitcher == True:
                    homeWOBA += data['woba_value'][i]
                    homeISO += data['iso_value'][i]
                    homeCount += 1
                else:
                    roadWOBA += data['woba_value'][i]
                    roadISO += data['iso_value'][i]
                    roadCount += 1
            elif v == 'catcher_interf':
                current_pitcher = data['pitcher'][i]
            elif v == 'single':
                current_pitcher = data['pitcher'][i]
                if home_pitcher == True:
                    homeWOBA += data['woba_value'][i]
                    homeISO += data['iso_value'][i]
                    homeCount += 1
                else:
                    roadWOBA += data['woba_value'][i]
                    roadISO += data['iso_value'][i]
                    roadCount += 1
            elif v == 'double':
                current_pitcher = data['pitcher'][i]
                if home_pitcher == True:
                    homeWOBA += data['woba_value'][i]
                    homeISO += data['iso_value'][i]
                    homeCount += 1
                else:
                    roadWOBA += data['woba_value'][i]
                    roadISO += data['iso_value'][i]
                    roadCount += 1
            elif v == 'triple':
                current_pitcher = data['pitcher'][i]
                if home_pitcher == True:
                    homeWOBA += data['woba_value'][i]
                    homeISO += data['iso_value'][i]
                    homeCount += 1
                else:
                    roadWOBA += data['woba_value'][i]
                    roadISO += data['iso_value'][i]
                    roadCount += 1
            elif v == 'home_run':
                current_pitcher = data['pitcher'][i]
                if home_pitcher == True:
                    homeWOBA += data['woba_value'][i]
                    homeISO += data['iso_value'][i]
                    homeCount += 1
                else:
                    roadWOBA += data['woba_value'][i]
                    roadISO += data['iso_value'][i]
                    roadCount += 1
            elif v == 'hit_by_pitch':
                current_pitcher = data['pitcher'][i]
                if home_pitcher == True:
                    homeWOBA += data['woba_value'][i]
                    homeISO += data['iso_value'][i]
                    homeCount += 1
                else:
                    roadWOBA += data['woba_value'][i]
                    roadISO += data['iso_value'][i]
                    roadCount += 1

            

            if (out_count == 3 and home_pitcher == True):        
                home_pitcher_id.append(current_pitcher)
                # print('home current pitcher out count ')
                # print(current_pitcher)
                home_pitcher = False
                road_pitcher = True
                out_count = 0
                
            if (out_count == 3 and road_pitcher == True):
                road_pitcher_id.append(current_pitcher)
                # print('road current pitcher out count ')
                # print(current_pitcher)
                home_pitcher = True
                road_pitcher = False
                out_count = 0
                
            if (data['pitcher'][i] != current_pitcher and home_pitcher == True):
                current_pitcher = data['pitcher'][i]
                home_pitcher_id.append(current_pitcher)
                # print('Home current pitcher middle inning ')
                # print(current_pitcher)

            if (data['pitcher'][i] != current_pitcher and road_pitcher == True):
                current_pitcher = data['pitcher'][i]
                road_pitcher_id.append(current_pitcher)
                # print('Road current pitcher middle inning ')
                # print(current_pitcher)

            for i,v in pitchData.items():

                if data['release_spin_rate'][i] > 1000:

                    if data['inning_topbot'][i] == "Top":

                        if v == 'FF' or v == 'SI' or v == 'FT' :
                            fastballVeloHome += data['release_speed'][i]
                            fastballSpinHome += data['release_spin_rate'][i]
                            fastballCounterHome += 1
                        elif v == 'SL' or v == 'CU' or v == 'KC':
                            breakingballVeloHome += data['release_speed'][i]
                            breakingballSpinHome += data['release_spin_rate'][i]
                            breakingballCounterHome += 1
                        else:
                            changeupVeloHome += data['release_speed'][i]
                            changeupSpinHome += data['release_spin_rate'][i]
                            changeupCounterHome += 1
                    else:
                        if v == 'FF' or v == 'SI' or v == 'FT' :
                            fastballVeloRoad += data['release_speed'][i]
                            fastballSpinRoad += data['release_spin_rate'][i]
                            fastballCounterRoad += 1
                        elif v == 'SL' or v == 'CU' or v == 'KC':
                            breakingballVeloRoad += data['release_speed'][i]
                            breakingballSpinRoad += data['release_spin_rate'][i]
                            breakingballCounterRoad += 1
                        else:
                            changeupVeloRoad += data['release_speed'][i]
                            changeupSpinRoad += data['release_spin_rate'][i]
                            changeupCounterRoad += 1

        fastballVeloHomeMean = fastballVeloHome / fastballCounterHome
        breakingballVeloHomeMean = breakingballVeloHome / breakingballCounterHome
        changeupVeloHomeMean = changeupVeloHome / changeupCounterHome
        fastballSpinHomeMean = fastballSpinHome / fastballCounterHome
        breakingballSpinHomeMean = breakingballSpinHome / breakingballCounterHome
        changeupSpinHomeMean = changeupSpinHome / changeupCounterHome

        fastballVeloRoadMean = fastballVeloRoad / fastballCounterRoad
        breakingballVeloRoadMean = breakingballVeloRoad / breakingballCounterRoad
        changeupVeloRoadMean = changeupVeloRoad / changeupCounterRoad
        fastballSpinRoadMean = fastballSpinRoad / fastballCounterRoad
        breakingballSpinRoadMean = breakingballSpinRoad / breakingballCounterRoad
        changeupSpinRoadMean = changeupSpinRoad / changeupCounterRoad

        home_pitcher_id = set(home_pitcher_id)
        road_pitcher_id = set(road_pitcher_id)
        home_pitcher_count = len(home_pitcher_id)
        road_pitcher_count = len(road_pitcher_id)
        print(home_pitcher_id)
        print(road_pitcher_id)

        homeWOBAMean = homeWOBA / homeCount
        homeISOMean = homeISO / homeCount
        roadWOBAMean = roadWOBA / roadCount
        roadISOMean = roadISO / roadCount
        print(homeISOMean)

        if home_score > road_score:
            home_win = 1
        else:
            road_win = 1

        homeDict = {
            'pitcher_count': home_pitcher_count,
            'winning_team': home_win,
            'fastballVelo': fastballVeloHomeMean,
            'breakingballVelo': breakingballVeloHomeMean,
            'changeupVelo': changeupVeloHomeMean,
            'fastballSpin': fastballSpinHomeMean,
            'breakingballSpin': breakingballSpinHomeMean,
            'changeupSpin': changeupSpinHomeMean,
            'runs_scored': home_score,
            'runs_allowed': road_score,
            'WOBA_against': roadWOBAMean,
            'ISO_against': roadISOMean,
            'bullpen_game': bullpenGameHome,
            'team': home_team
        }
        roadDict = {
            'pitcher_count': road_pitcher_count,
            'winning_team': road_win,
            'fastballVelo': fastballVeloRoadMean,
            'breakingballVelo': breakingballVeloRoadMean,
            'changeupVelo': changeupVeloRoadMean,
            'fastballSpin': fastballSpinRoadMean,
            'breakingballSpin': breakingballSpinRoadMean,
            'changeupSpin': changeupSpinRoadMean,
            'runs_scored': road_score,
            'runs_allowed': home_score,
            'WOBA_against': homeWOBAMean,
            'ISO_against': homeISOMean,
            'bullpen_game': bullpenGameRoad,
            'team': road_team
        }

        # print(homeDict)
        gameList.append(homeDict)
        # print(roadDict)
        gameList.append(roadDict)
        # print(gameList)

    except:
        gamesSkipped += 1
        # print(gamesSkipped)
        continue

# print(gameList)
print(gamesSkipped)
gameList = pd.DataFrame(gameList)
gameList.to_csv('gameList2017.csv')

# if home_pitcher == True:
                #     homeWOBA += data['woba_value'][i]
                #     homeISO += data['iso_value'][i]
                #     homeCount += 1
                # else:
                #     roadWOBA += data['woba_value'][i]
                #     roadISO += data['iso_value'][i]
                #     roadCount += 1
# if home_pitcher == True:
                #     homeWOBA += data['woba_value'][i]
                #     homeISO += data['iso_value'][i]
                #     homeCount += 1
                # else:
                #     roadWOBA += data['woba_value'][i]
                #     roadISO += data['iso_value'][i]
                #     roadCount += 1
# if home_pitcher == True:
                #     homeWOBA += data['woba_value'][i]
                #     homeISO += data['iso_value'][i]
                #     homeCount += 1
                # else:
                #     roadWOBA += data['woba_value'][i]
                #     roadISO += data['iso_value'][i]
                #     roadCount += 1
# if home_pitcher == True:
                #     homeWOBA += data['woba_value'][i]
                #     homeISO += data['iso_value'][i]
                #     homeCount += 1
                # else:
                #     roadWOBA += data['woba_value'][i]
                #     roadISO += data['iso_value'][i]
                #     roadCount += 1
# if home_pitcher == True:
                #     homeWOBA += data['woba_value'][i]
                #     homeISO += data['iso_value'][i]
                #     homeCount += 1
                # else:
                #     roadWOBA += data['woba_value'][i]
                #     roadISO += data['iso_value'][i]
                #     roadCount += 1
# if home_pitcher == True:
                #     homeWOBA += data['woba_value'][i]
                #     homeISO += data['iso_value'][i]
                #     homeCount += 1
                # else:
                #     roadWOBA += data['woba_value'][i]
                #     roadISO += data['iso_value'][i]
                #     roadCount += 1
# if home_pitcher == True:
                #     homeWOBA += data['woba_value'][i]
                #     homeISO += data['iso_value'][i]
                #     homeCount += 1
                # else:
                #     roadWOBA += data['woba_value'][i]
                #     roadISO += data['iso_value'][i]
                #     roadCount += 1
# if home_pitcher == True:
                #     homeWOBA += data['woba_value'][i]
                #     homeISO += data['iso_value'][i]
                #     homeCount += 1
                # else:
                #     roadWOBA += data['woba_value'][i]
                #     roadISO += data['iso_value'][i]
                #     roadCount += 1
# if home_pitcher == True:
                #     homeWOBA += data['woba_value'][i]
                #     homeISO += data['iso_value'][i]
                #     homeCount += 1
                # else:
                #     roadWOBA += data['woba_value'][i]
                #     roadISO += data['iso_value'][i]
                #     roadCount += 1
# if home_pitcher == True:
                #     homeWOBA += data['woba_value'][i]
                #     homeISO += data['iso_value'][i]
                #     homeCount += 1
                # else:
                #     roadWOBA += data['woba_value'][i]
                #     roadISO += data['iso_value'][i]
                #     roadCount += 1
# if home_pitcher == True:
                #     homeWOBA += data['woba_value'][i]
                #     homeISO += data['iso_value'][i]
                #     homeCount += 1
                # else:
                #     roadWOBA += data['woba_value'][i]
                #     roadISO += data['iso_value'][i]
                #     roadCount += 1
    

# loop through some list with number of games between first and last
#      add one to the game_id and assign it to variable nextGame
#      append list with nextGame

#      final list should have all game ids for each game in 2018

# loop through game_id list
#     feed into statcast_single_game module and get each days game data
#     append pitcher_id to home_pitcher_id list
#     count 'out' events to 3 OR when outs_when_up is 0, 
#     switch count to road_pitcher_id 
#     repeat out count until game is over
#     count number of pitchers for each team and append them to correct bin based on number of pitcehrs

#      final product: should have lists of number of pitchers in games (1, 2, 3, 4, 5, 6+)

# loop through each list of each number of pitchers
#     compare home_score to road_score (first entry is last event of game)
#     assign win to correct pitcher_id list
#     calculate ERA based on number of runs per 9 innings
#     bin based on pitch type
#     find avg release_speed, release_spin_rate for each pitch
#     
#     find W/L record for each group

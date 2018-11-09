# Bullpenning 

<li>link: https://public.tableau.com/profile/kevin.jordan1362#!/vizhome/Bullpenning_Dashboard_Update/Dashboard1</li>

<h2>Contents</h2>
<li>What is 'Bullpenning'?

Bullpenning is a new trend in baseball where teams are using more pitcehrs per game than ever before. There are a multitude of reasons for this, including the relief pitchers in Major League Baseball are better and are throwing harder than ever before. Furthermore, studies have shown that hitters have a significant advantage against pitcher after facing them multpile times, especially the third time. Teams are no longer relying on one pitcher to get them through an entire game, and are looking to avoid these inadvantageous situations. The Tampa Bay Rays have taken it a step further and begun using 'bullpen games' instead of a fourth or fifth starting pitcher

Data Collection / Limitations

I used a module called "PyBaseball" which calls on an API called Statcast, which gathers data from high powered, extra-sensitive cameras that capture the movement of players and the ball for every pitch of every MLB game. Some of the stats I used from Statcast were spin rate, velocity, pitch frequency, weighted on base average (wOBA) and isolated power (ISO). Spin rate calculates the number of rotations the baseball makes in a pitch. Pitch frequency shows the percentage of how often a team's pitching staff throws each type of pitch. Weighted on base average is an advanced metric that uses linear weights designed to measure a player's overall offensive contributions per plate appearance. These weights are reassigned annually, and reflect the impact of each way to get on base. Isolated power identifies the frequency in which a player hits for extra bases (double, triple, home run) per at bat. It is calculated by the difference between a batter's slugging percntage and batting average. Some limitations I had with the data was a small sample size for the bullpen games. 

Another metric I used is "Bauer Units," which is the ratio of a pitch's spin rate to velocity. According to an article from FiveThirtyEight (clickable below), this essentially measures how "unhittable" the pitch is. To understand why this metric is so reliable, consider two 95 MPH fastballs, one with a spin rate of 2300 rpm and the other with 2400 rpm. The higher spin rate will give the effect of "rising" or "late life," common old-school baseball terms referring to how pitches move. The higher this ratio, the more unhittable the pitch.

Some of the limitations I faced were due to the module not gathering data perfectly. The API call gathers game-by-game data, and each entry is in reverse order of how the game is played (the first row is the last pitch of the game). Using loops to gather and compute data was difficult, but I was able to get a fairly accurate dataset. I was able to get data for 2400 games (4800  total entries, 2 entries per game, one for each team) from the 2018 season, but my code couldn't get the data for 60 of the games, so some of the data isn't perfect. Of the 4800 entries, 53 of them were bullpen games, so the conclusions I draw may not be concrete, due to a relatively small sample size, but we can certainly still seek out trends in the data.

What is a 'bullpen game'?

A bullpen game is where a team uses a traditional bullpen pitcher to start the game, and play the entire game based on matchups. The theory behind it's use is that if you are in the most advantageous position to succeed for every play, then you will have a better chance of winning. The majority of these games saw an "opener" begin the game and throw one or two innings, followed by the next pitcher who may throw 3-5. However, despite the team's flexbile plan of how the game would ideally be structured, most of the decisions made are based on matchups. The Rays have started implimenting bullpen games at the start of the 2018 MLB season, so I used data from an API called Statcast to look into this trend.

What is the purpose of this project?

I wanted to look into these trends and use both performance statistics along with physics data (spin rate, velocity)  gathered from Statcast to answer the following quesitons: Are teams performing better when they use more pitchers? Have these bullpen games been successful and will this become a more evident trend throughout the game?</li>

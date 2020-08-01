# Rocket League Stats API
##### Get your Rocket League stats

#### Usage:

```
GET localhost:4996/rocket-league/playlist/{platform}/{username}
```

#### Response:

```Json
{
  "games": [
    {
    "rankImgUrl": "https://rocketleague.tracker.network/Images/RL/ranked/s4-19.png",
    "gameType": "Ranked Duel 1v1",
    "divDown": "~538",
    "divUp": null,
    "rank": "Grand Champion Division I",
    "rating": "1,759",
    "topPercent": " (Top 0.1%)",
    "gamesPlayed": "847"
    },
    {
    "rankImgUrl": "https://rocketleague.tracker.network/Images/RL/ranked/s4-19.png",
    "gameType": "Ranked Doubles 2v2",
    "divDown": "~520",
    "divUp": null,
    "rank": "Grand Champion Division I",
    "rating": " 2,020",
    "topPercent": " (Top 0.1%)",
    "gamesPlayed": "1,095"
    }
  ]
}
```

#### Available Platforms:
 
  - ps (PlayStation 4)
  - steam
  - xbox
 
--- 

#### Installation (without docker):

```
pip3 install -r requirements.txt
```

```
python3 rocket_league.py
```
---

#### Installation (with docker):

```
docker build -t rocket-league .
```

```
docker run -d --name rl -p 4996:4996 rocket-league
```

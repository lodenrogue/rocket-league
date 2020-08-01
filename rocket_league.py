from flask import Flask, request, Response
from flask_cors import CORS
from bs4 import BeautifulSoup
import requests
import json

BASE_URL = 'https://rocketleague.tracker.network'
PROFILE_URL = BASE_URL + '/profile/{platform}/{username}'

app = Flask(__name__)
CORS(app)


@app.route('/rocket-league/playlist/<platform>/<username>')
def get_playlist(platform, username):
	url = PROFILE_URL.replace('{platform}', platform).replace('{username}', username)

	req = requests.get(url)
	soup = BeautifulSoup(req.content, 'html.parser')

	playlist = {'games': []}
	rows = get_rows(soup)

	for row in rows[1:]:
		rank_img_url = get_rank_img_url(row)
		game_type = get_game_type(row)

		div_down = get_div_down(row)
		div_up = get_div_up(row)

		rank = get_rank(row)
		rating = get_rating(row)
		top_percent = get_top_percent(row)
		games_played = get_games_played(row)

		playlist['games'].append({
			'rankImgUrl' : rank_img_url,
			'gameType' : game_type,
			'divDown' : div_down,
			'divUp' : div_up,
			'rank' : rank,
			'rating' : rating,
			'topPercent': top_percent,
			'gamesPlayed' : games_played
		})

	js = json.dumps(playlist)
	return Response(js, status=200, mimetype='application/json')


def get_rank_img_url(row):
	data = row.find_all('td')[0]
	image = data.find('img')
	return BASE_URL + image['src']


def get_game_type(row):
	data = row.find_all('td')[1]
	split = data.getText().split('\n')
	return split[1]


def get_div_down(row):
	return get_div_movement(row, 2)


def get_div_up(row):
	return get_div_movement(row, 4)


def get_div_movement(row, index):
	data = row.find_all('td')[index]
	span = data.find('span')

	if span is None:
		return None
	else:
		return span.text


def get_rank(row):
	data = row.find_all('td')[1]
	split = data.getText().split('\n')
	return split[3] + " " + split[4]


def get_rating(row):
	data = row.find_all('td')[3]
	split = data.getText().split('\n')
	return split[1]


def get_top_percent(row):
	data = row.find_all('td')[3]
	split = data.getText().split('\n')
	return split[3]


def get_games_played(row):
	data = row.find_all('td')[5]
	split = data.getText().split('\n')
	return split[1]


def get_rows(soup):
	season_table = soup.find_all(class_='season-table')[0]
	playlist_table = season_table.find_all('table')[1]
	table_body = playlist_table.find('tbody')
	return table_body.find_all('tr')


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=4996)

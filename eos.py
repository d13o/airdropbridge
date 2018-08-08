import requests


def fetch_eos_actions(page=0):
	URL = 'https://explorer.eoseco.com/api/accountTraces'
	r = requests.get(URL, params={'name': 'enueosfriend', 'page': page}, timeout=10)		
	return r.json()

fetch_eos_actions()

import dateutil.parser
from eos import fetch_eos_actions


def validate_eos_transfer(action):
	assert(action['account_name'] == 'enueosfriend') 
	assert(len(action['transaction_id']) == 64) 
	assert(len(action['contract_actions']) == 1)
	assert(action['pending'] == False)

	cact = action['contract_actions'][0]
	assert(cact['contract'] == 'eosio.token')
	assert(cact['action'] == 'transfer')
	assert(cact['data']['to'] == 'enueosfriend')
	assert(cact['data']['quantity'] == '0.0001 EOS')
	assert(len(cact['data']['memo']) > 0)


def encode_airdrop_data(action):
	dt = dateutil.parser.parse(action['timestamp'])
	ts_ms = int(dt.timestamp() * 1000)
	txid = action['transaction_id']
	eos_account = action['contract_actions'][0]['data']['from']
	enu_account = action['contract_actions'][0]['data']['memo']
	return ':'.join([eos_account, enu_account, str(ts_ms), txid])


def test():
	acts = fetch_eos_actions()
	for act in acts:
		try:
			validate_eos_transfer(act)
		except AssertionError as e:
			continue
		print(encode_airdrop_data(act))


if __name__ == '__main__':
	test()

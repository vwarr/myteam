import cfbd, os, record

config = cfbd.Configuration()
config.api_key['Authorization'] = os.getenv('CFBD_API_KEY')
config.api_key_prefix['Authorization'] = 'Bearer'

team = 'VMI'

api_instance = cfbd.GamesApi(cfbd.ApiClient(configuration=config))

record.get_wins_losses(api_instance, team, 2024)


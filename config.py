import os

#configuration
CONFIG = {
    'district': '서울특별시',
    'countries': [('중국', 112), ('일본', 130), ('미국', 275)],
    'common': {
        'start_year': 2017,
        'end_year': 2017,
        'fetch': False,
        'result_directory': '__results__/crawling',
        'service_key': 'QdHkfm%2BbbCxyXKtLDwC%2FetAD3OkxlNmThephKw96FxPLhxNJbWdcp6NIJ0EJZSHVdjzaSa8fEMHlMlZ9rxJF5w%3D%3D'
    }
}

if not os.path.exists(CONFIG['common']['result_directory']):
    os.makedirs(CONFIG['common']['result_directory'])

if not os.path.exists(CONFIG['common']['result_directory']):
    os.makedirs(**CONFIG['common']['result_directory'])
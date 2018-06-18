import os

#configuration
CONFIG={
    'district=':'서울특별시',
    'countries':[('중국', 112), ('일본', 130), ('미국', 275)],
    'common':{ #공통되는 부분 서비스키, year,
        'start_year':2017,  # CONFIG['common']['start_year']
        'end_year':2017,
        'fetch' : True,
        'result_directory':'__results__/crawling',
        'service_key':'QdHkfm%2BbbCxyXKtLDwC%2FetAD3OkxlNmThephKw96FxPLhxNJbWdcp6NIJ0EJZSHVdjzaSa8fEMHlMlZ9rxJF5w%3D%3D%2FH55iva04jaZEtA%3D%3D'
    }
}

if not os.path.exists(CONFIG['common']['result_directory']):
    os.makedirs(**CONFIG['common'])
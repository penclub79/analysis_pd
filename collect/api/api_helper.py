
#공공data 서울특별시 관광 정보 크롤링

#test for pd_gen_url

from urllib.parse import urlencode
from .web_request import json_request

END_POINT = "http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService"
SERVICE_KEY = "QdHkfm%2BbbCxyXKtLDwC%2FetAD3OkxlNmThephKw96FxPLhxNJbWdcp6NIJ0EJZSHVdjzaSa8fEMHlMlZ9rxJF5w%3D%3D"


def pb_gen_url(endpoint = END_POINT, service_key = SERVICE_KEY, **params):

    url = '%s?serviceKey=%s&%s' % (endpoint, service_key, urlencode(params))

    return url

def pb_fetch_tourspot_visitor(district="", year=0, month=0):
    url = pb_gen_url(
        'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList',
    YM='{0:04d}{1:02d}'.format(year, month),
    SIDO='',
    GUNGU='',
    RES_NM='',
    numOfRows=10,
    _type='json',
    for pageNo in totalCount:
        pageNo+=totalCoun
    )
    json_result=json_request(url=url)
    return json_result

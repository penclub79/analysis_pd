
#공공data 서울특별시 관광 정보 크롤링

#test for pd_gen_url

from urllib.parse import urlencode
from .web_request import json_request
import datetime

END_POINT = "http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService"
SERVICE_KEY = "QdHkfm%2BbbCxyXKtLDwC%2FetAD3OkxlNmThephKw96FxPLhxNJbWdcp6NIJ0EJZSHVdjzaSa8fEMHlMlZ9rxJF5w%3D%3D"


def pb_gen_url(endpoint = END_POINT, service_key = SERVICE_KEY, **params):

    url = '%s?serviceKey=%s&%s' % (endpoint, service_key, urlencode(params))

    return url

def pb_fetch_foreign_visitor(country_code, year, month):
    endpoint = 'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'
    url = pb_gen_url(endpoint,
                     YM='{0:04d}{1:02d}'.format(year, month),
                     NAT_CD=country_code,
                     ED_CE='E',
                     _type='json')
    json_result = json_request(url=url)

    json_response= json_result.get('response')
    json_header = json_response.get('header')
    result_message = json_header.get('resultMsg')
    if 'OK' != result_message:
        print('%s Error[%s] for request %s' % (datetime.now(), result_message, url))
        return None

    json_body = json_response.get('body')
    json_items = json_body.get('items')

    return json_items.get('item') if isinstance(json_items, dict) else None

def pb_fetch_tourspot_visitor(district="", year=0, month=0):
    url = pb_gen_url(
        'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList',
    YM='{0:04d}{1:02d}'.format(year, month),
    SIDO='',
    GUNGU='',
    RES_NM='',
    numOfRows=10,
    _type='json',
    pageNo=1)

    # isnext = True   #true냐 false에 따라서 달라고하기
    # while isnext is True: # isnext가 true면 루프돌기
    #     json_result = json_request(url=url)
    #     #페이징 정보 가져오기 왜? json result가 null일수 있어서
    #     pageNo = None
    #     if json_result is None:
    #         pageNo =  None
    #     else:
    #         pageNo = json_result.get('pageNo')


    isnext=True
    while isnext is True:
        json_result=json_request(url=url)
        pageNo = None if json_result is None else json_result.get('response').json_result.get('body').json_result.get('pageNo')
        items = None if json_result is None else json_result.get('response').json_result.get('body').json_result.get('items').json_result.get('item')
        url = None if pageNo is None else pageNo.get("pageNo")

        isnext = url is not None

        yield items


#공공data 서울특별시 관광 정보 크롤링

#test for pd_gen_url

from urllib.parse import urlencode
from .web_request import json_request
from datetime import datetime
import math

END_POINT = "http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList"
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

def pb_fetch_tourspot_visitor(district='', year=0, month=0, service_key=''):

    pageno = 1
    hasnext = True

    while hasnext:
        url = pb_gen_url(
            endpoint=END_POINT,
            service_key,
            YM='{0:04d}{1:02d}'.format(year, month),
            SIDO=district,
            GUNGU='',
            RES_NM='',
            numOfRows=20,
            _type='json',
            pageNo=pageno
        )
        json_result = json_request(url=url)

        json_response = json_result.get('response')
        json_header = json_response.get('header')
        result_message = json_header.get('resultMsg')

        if 'OK' != result_message:
            print('%s Error[%s] for request %s' % (datetime.now(), result_message, url))
            return None

        json_body = json_response.get('body')
        numofrows = json_body.get('numOfRows')
        totalcount = json_body.get('totalCount')
        json_items = json_body.get('items')

        if totalcount == 0:
            break

        last_page = math.ceil(totalcount/numofrows)
        if pageno == last_page:
            hasnext = False
        else:
            pageno += 1


        yield json_items.get('item')

        # items = None if json_result is None else json_result.get('response').json_result.get('body').json_result.get('items')
        # url = None if pageNo is None else pageNo.get("pageNo")

        # hasnext = url is not None

        # yield items

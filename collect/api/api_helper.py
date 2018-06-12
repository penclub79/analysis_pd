
#공공data 서울특별시 관광 정보 크롤링

#test for pd_gen_url

from urllib.parse import urlencode
# from .web_request import json_request

END_POINT = "http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService"
SERVICE_KEY = "10wfesCEKZKTWb9IhpFWutS0D6Z6p2M1j9BlDf0VCuhfzvsI74IuQND3AgnhxdIpSyI9lER%2FH55iva04jaZEtA%3D%3D"


def pd_gen_url(endpoint = END_POINT, service_key = SERVICE_KEY, **params):

    url = '%s?serviceKey=%s&%s' % (endpoint, service_key, urlencode(params))

    return url


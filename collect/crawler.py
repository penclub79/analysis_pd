import json
from .api import api

def preprocess_tourspot_visitor(item):
    # addrCd
    del item['addrCd']

    # rnum
    del item['rnum']

    # gungu
    del item['gungu']

    # 내국인수
    if 'csNatCnt' not in item:
        item['count_locals'] = 0
    else:
        item['count_locals'] = item['csNatCnt']
    del item['csNatCnt']

    # 외국인 수
    if 'csForCnt' not in item:
        item['count_foreigner'] = 0
    else:
        item['count_foreigner'] = item['csForCnt']
    del item['csForCnt']

    # 관광지 이름
    if 'resNm' not in item:
        item['tourist_spot'] = 0
    else:
        item['tourist_spot'] = item['resNm']
    del item['resNm']

    # 년월
    if 'ym' not in item:
        item['date'] = 0
    else:
        item['date'] = item['ym']
        del item['ym']

    # 시도
    if 'sido' not in item:
        item['district'] = 0
    else:
        item['district'] = item['sido']
        del item['sido']

def preprocess_foreign_visitor(data):       #저장해서 전처리로넣기
    #ed
    del data['ed']

    #edCd
    del data['edCd']

    #rnum
    del data['rnum']

    #나라 코드
    data['country_code'] = data['natCd']
    del data['natCd']

    #나라 이름
    data['country_name'] = data['natKorNm'].replace(' ','')
    del data['natKorNm']

    #방문자 수
    data['visit_count'] = data['num']
    del data['num']

    # 년 월
    if 'ym' not in data:
        data['date'] = ''
    else:
        data['date'] = data['ym']
        del data['ym']



def crawling_tourspot_visitor(
        district,
        start_year,
        end_year,
        fetch=True,
        result_directory='',
        service_key=''):

    results = []
    filename = '%s/%s_tourspot_%s_%s.json' % (
        result_directory,
        district,
        start_year,
        end_year)

    if fetch:
        for year in range(start_year, end_year+1):
            for month in range(1, 13):
                for items in api.pb_fetch_tourspot_visitor(
                        district1=district,
                        year=year,
                        month=month,
                        service_key=service_key):
                    for item in items:
                        preprocess_tourspot_visitor(item)

                    results += items

        # save data to file
        with open(filename, 'w', encoding='utf-8') as outfile:
            json_string = json.dumps(results, indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(json_string)

    return filename




# def crawling_foreign_visitor(country, start_year, end_year, fetch=True, result_directory='', service_key=''):
#     results = []
#     for year in range(start_year, end_year+1):  #년도 루프
#         for month in range(1, 13):      #개월 루프
#             # print(country[0] + ":" + str(year)+"-"+str(month))
#             data = api.pb_fetch_foreign_visitor(
#                 country[1],
#                 year,
#                 month,
#                 service_key)
#             # print(data)
#             if data is None:    #data를 실수로 넣엇을때 처리하는 과정
#                 continue
#
#             preprocess_foreign_visitor(data)
#             # results += data  배열로 처리하기때문에 이렇게 적으면 안됌
#             results.append(data)
#
#
#     #루프 다 빠져나오고 저장해야할 위치 save data
#     # print(results)
#     filename = '%s/%s(%s)_foreignvisitor_%s_%s.json' % (result_directory, country[0], country[1], start_year, end_year)
#     with open(filename, 'w', encoding='utf-8') as outfile:
#         json_string = json.dumps(results, indent=4, sort_keys=True, ensure_ascii=False)
#         outfile.write(json_string)
#         #with open은 클로즈 안해줘도 된다.
#
# # if not os.path.exists(RESULT_DIRECTORY):
# #     os.makedirs(RESULT_DIRECTORY)
def crawling_foreign_visitor(
        country,
        start_year,
        end_year,
        fetch=True,
        result_directory='',
        service_key=''):

    results = []
    filename = '%s/%s(%s)_foreignvisitor_%s_%s.json' % (result_directory, country[0], country[1], start_year, end_year)

    if fetch:
        for year in range(start_year, end_year+1):
            for month in range(1, 13):
                data = api.pb_fetch_foreign_visitor(
                    country[1],
                    year,
                    month,
                    service_key)
                if data is None:
                    continue

                preprocess_foreign_visitor(data)
                results.append(data)

        # save data to file

        with open(filename, 'w', encoding='utf-8') as outfile:
            json_string = json.dumps(results, indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(json_string)

    return filename
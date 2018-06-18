import json
from .api import api

def preprocess_foreign_visitor(item):       #저장해서 전처리로넣기
    #ed
    del item['ed']

    #edCd
    del item['edCd']

    #rnum
    del item['rnum']

    #나라 코드
    item['country_code'] = item['natCd']
    del item['natCd']

    #나라 이름
    item['country_name'] = item['natKorNm'].replace(' ','')
    del item['natKorNm']

    #방문자 수
    item['visit_count'] = item['num']
    del item['num']

    # 년 월
    if 'ym' not in item:
        item['date'] = ''
    else:
        item['date'] = item['ym']
        del item['ym']
def preprocess_tourspot_visitor(item):

    #csNatCnt -> count_locals
    if 'csNatCnt' not in item:
        item['count_locals'] = 0
    else:
        item['count_locals'] = item['csNatCnt']
    del item['csNatCnt']

    #csForCnt->count_forigner
    if 'csForCnt' not in item:
        item['count_locals'] = 0
    else:
        item['count_locals'] = item['csForCnt']
    del item['csForCnt']

    #resNm -> tourist_spot
    if 'resNm' not in item:
        item['tourist_spot'] = 0
    else:
        item['tourist_spot'] = item['resNm']
    del item['resNm']

    #ym -> date
    if 'ym' not in item:
        item['date'] = 0
    else:
        item['date'] = item['ym']
    del item['ym']

    #sido->restrict1
    if 'ym' not in item:
        item['restrict1'] = 0
    else:
        item['restrict1'] = item['sido']
    del item['sido']

    # gungu->restrict2
    if 'ym' not in item:
        item['restrict2'] = 0
    else:
        item['restrict2'] = item['gungu']
    del item['gungu']

    # addrCd
    del item['addrCd']
    # rnum
    del item['rnum']


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
                for items in api.pd_fetch_tourspot_visitor(
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

    if fetch:
        for year in range(start_year, end_year+1):
            for month in range(1, 13):
                data = api.pd_fetch_foreign_visitor(
                    country[1],
                    year,
                    month,
                    service_key)
                if data is None:
                    continue

                preprocess_foreign_visitor(data)
                results.append(data)

        # save data to file
        filename = '%s/%s(%s)_foreignvisitor_%s_%s.json' % (result_directory, country[0], country[1], start_year, end_year)
        with open(filename, 'w', encoding='utf-8') as outfile:
            json_string = json.dumps(results, indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(json_string)

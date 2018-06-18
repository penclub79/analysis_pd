import json
from .api import api
import json
from .api import api
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
def preprocess_tourspot_visitor(data):

    #csNatCnt -> count_locals
    if 'csNatCnt' not in data:
        data['count_locals'] = 0
    else:
        data['count_locals'] = data['csNatCnt']
    del data['csNatCnt']

    #csForCnt->count_forigner
    if 'csForCnt' not in data:
        data['count_locals'] = 0
    else:
        data['count_locals'] = data['csForCnt']
    del data['csForCnt']

    #resNm -> tourist_spot
    if 'resNm' not in data:
        data['tourist_spot'] = 0
    else:
        data['tourist_spot'] = data['resNm']
    del data['resNm']

    #ym -> date
    if 'ym' not in data:
        data['date'] = 0
    else:
        data['date'] = data['ym']
    del data['ym']

    #sido->restrict1
    if 'ym' not in data:
        data['restrict1'] = 0
    else:
        data['restrict1'] = data['sido']
    del data['sido']

    # gungu->restrict2
    if 'ym' not in data:
        data['restrict2'] = 0
    else:
        data['restrict2'] = data['gungu']
    del data['gungu']

    # addrCd
    del data['addrCd']
    # rnum
    del data['rnum']


def crawling_tourspot_visitor(district, start_year, end_year, fetch=True, result_directory=''):
    results = []
    for year in range(start_year, end_year+1):
        for month in range(1,13):
            datas = api.pb_fetch_tourspot_visitor(
                district,
                year,
                month,
                service_key)

            for dataa in datas:
                for data in dataa:
                    preprocess_tourspot_visitor(data)
                results += dataa

    filename = '%s/%s_tourspot_%s_%s.json' % (RESULT_DIRECTORY, district, start_year, end_year)
    with open(filename, 'w', encoding='utf-8') as outfile:
        json_string = json.dumps(results, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(json_string)


def crawling_foreign_visitor(country, start_year, end_year, fetch=True, service_key=''):
    results = []
    for year in range(start_year, end_year+1):  #년도 루프
        for month in range(1, 13):      #개월 루프
            # print(country[0] + ":" + str(year)+"-"+str(month))
            data = api.pb_fetch_foreign_visitor(country[1], year, month)
            # print(data)
            if data is None:    #data를 실수로 넣엇을때 처리하는 과정
                continue

            preprocess_foreign_visitor(data)
            # results += data  배열로 처리하기때문에 이렇게 적으면 안됌
            results.append(data)


    #루프 다 빠져나오고 저장해야할 위치 save data
    # print(results)
    filename = '%s/%s(%s)_foreignvisitor_%s_%s.json' % (RESULT_DIRECTORY, country[0], country[1], start_year, end_year)
    with open(filename, 'w', encoding='utf-8') as outfile:
        json_string = json.dumps(results, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(json_string)
        #with open은 클로즈 안해줘도 된다.

# if not os.path.exists(RESULT_DIRECTORY):
#     os.makedirs(RESULT_DIRECTORY)
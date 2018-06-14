import os
import json
from .api import api



RESULT_DIRECTORY = '__results__/crawling'

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

def crawling_tourspot_visitor():
    pass

def crawling_foreign_visitor(country, start_year, end_year):
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

if not os.path.exists(RESULT_DIRECTORY):
    os.makedirs(RESULT_DIRECTORY)
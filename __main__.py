import collect
from config import CONFIG
# if __name__ == '__main__':
#     collect.crawlling_tourspot_visitor(district='서울특별시', start_year=2017, end_year=2017)

#collect데이터 수집
'''
collect.crawling_tourspot_visitor(district='서울특별시',
                                  start_year=2017,
                                  end_year=2017)
'''
# for country in [('중국', 112), ('일본', 130), ('미국', 275)]:
# #테스트 코드를 메인에 바로 만들어줌
#     collect.crawling_foreign_visitor(country, 2017, 2017)

if __name__ == '__main__':
    collect.crawling_tourspot_visitor(
        district=CONFIG['district'],    #config에 잇는 함수 들고옴
        # start_year=CONFIG['common']['start_year'],
        # end_year=['common']['end_year']
        **CONFIG['common']
    )

    for country in CONFIG['countries']:
        collect.crawling_foreign_visitor(
            country,
            **CONFIG['common'])

#analysis데이터분석

#visualize데이터 시각화
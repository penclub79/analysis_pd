import collect
import analyze
import visualize
from config import CONFIG
import pandas as pd
import matplotlib.pyplot as plt
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

# if __name__ == '__main__':
#     collect.crawling_tourspot_visitor(
#         district=CONFIG['district'],    #config에 잇는 함수 들고옴
#         # start_year=CONFIG['common']['start_year'],
#         # end_year=['common']['end_year']
#         **CONFIG['common']
#     )
#
#     for country in CONFIG['countries']:
#         collect.crawling_foreign_visitor(
#             country,
#             **CONFIG['common'])
if __name__ == '__main__':
    resultfiles = dict()

    #collect
    resultfiles['tourspot_visitor'] = collect.crawling_tourspot_visitor(
        district=CONFIG['district'], **CONFIG['common'])

    resultfiles['foreign_visitor'] = []
    for country in CONFIG['countries']:
        rf = collect.crawling_foreign_visitor(country, **CONFIG['common'])
        resultfiles['foreign_visitor'].append(rf)

#1. analysis and visualize데이터분석
    #result_analysis = analyze.analysis_correlation(resultfiles)
        #result_analysis 는 막대그래프
    # visualize.graph_scatter(result_analysis)
    #위는 산점형태
    #위에는 장소 다합친거

#2. visualize데이터 시각화
    result_analysis = analyze.analysis_correlation_by_tourspot(resultfiles)  #장소별로 나오게하기
    # grapth_table = pd.DataFrame(result_analysis, colums=['tourspot', "r_중국", "r_일본", "r_미국" ])
    # grapth_table = grapth_table.set_index('tourspot')
    # #
    # grapth_table.plot(kind='bar')
    # plt.show()
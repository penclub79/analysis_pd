import analysis_pd.collect.api.api as pdapi
    #테스트코드를 먼저 만들기
url = pdapi.pb_gen_url(
    'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList',
    YM='{0:04d}{1:02d}'.format(2017, 1),
    SIDO='서울특별시',
    GUNGU='',
    RES_NM='',
    numOfRows=10,
    _type='json',
    pageNo=1)

print(url)



# # # pb_fetch_tourspot_visitor(district='서울특별시', year=2012, month=7)
# for items in pdapi.pb_fetch_tourspot_visitor(district="서울특별시", year=2012, month=7):
#     print(items)

#test for pb_fetch_foreign_visitor
item = pdapi.pb_fetch_foreign_visitor(112, 2012, 7)
print(item)
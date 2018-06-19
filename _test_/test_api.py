import analysis_pd.collect.api.api as pdapi
#     #테스트코드를 먼저 만들기
# url = pdapi.pb_gen_url(
#     'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList',
#     service_key='QdHkfm%2BbbCxyXKtLDwC%2FetAD3OkxlNmThephKw96FxPLhxNJbWdcp6NIJ0EJZSHVdjzaSa8fEMHlMlZ9rxJF5w%3D%3D',
#     YM='{0:04d}{1:02d}'.format(2017, 1),
#     SIDO='서울특별시',
#     GUNGU='',
#     RES_NM='',
#     numOfRows=10,
#     _type='json',
#     pageNo=1
#     )
# print(url)

service_key='QdHkfm%2BbbCxyXKtLDwC%2FetAD3OkxlNmThephKw96FxPLhxNJbWdcp6NIJ0EJZSHVdjzaSa8fEMHlMlZ9rxJF5w%3D%3D'

# pb_fetch_tourspot_visitor(district='서울특별시', year=2012, month=7)
# for items in pdapi.pb_fetch_tourspot_visitor(district1="서울특별시", year=2012, month=7, service_key=service_key):
#     print(items)

#test for pb_fetch_foreign_visitor
item = pdapi.pb_fetch_foreign_visitor(112, 2012, 7, service_key)
print(item)
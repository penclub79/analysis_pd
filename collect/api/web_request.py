import sys
from urllib.request import Request, urlopen  #모듈 가져오기
from datetime import *
import json

def html_request(
        url = '',
        encoding = 'utf-8',
        success = None,
        error = lambda e: print('%s %s' % (e, datetime.now()), file=sys.stderr)):
              # standard err
              # 함수 한줄로 만들기
    # success = function(함수명)
    try:
        Request(url)  # request객체 생성
        request = Request(url)
        resp = urlopen(request)

        # 응답내용을 다 읽는다.
        html = resp.read().decode(encoding)

        if callable(success) is False:  # 함수인지 아닌지를 판별
            return html  # return값을 주는 의미는 바깥에서 처리해라 뜻

        print(html)

    except Exception as e:
        if callable(error) is True:
            error(e)

# def print_error(error):
#     print('%s %s' % (e, datetime.now()), file=sys.stderr)

def json_request(
                url = '',
                encoding='utf-8',
                success = None,
                error = lambda e: print('%s %s' % (e, datetime.now()), file=sys.stderr)):
                #[ success = None ] : callBack하는 비동기식의 함수
    try:
        request = Request(url)  #객체생성
        resp = urlopen(request)  # 응답 받기

        json_req = resp.read().decode(encoding)  # 응답 읽기 (바디 내용)  - 바이트로 통신    인코딩 했으면 디코딩도 해야함
        json_result = json.loads(json_req)
        print('%s : success for request[%s]' % (datetime.now(), url)) #성공 로그를 남김

        if callable(success) is False: #이까지온다면 성공이고 success는 성공함수다
            return json_result

        success(json_result)

    except Exception as e :
        if callable(error) is True:
            error(e)

    # print(html)  # 네이버 바디(코드)를 가져옴
    # except Exception as e:
    #     print('%s %s' % (e, datetime.now()), file=sys.stderr)

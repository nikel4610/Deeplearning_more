import json
import requests
import openpyxl
import apikeys

"""
{
    "lastBuildDate": "Sat, 22 Jun 2019 14:57:13 +0900",
    "total": 634151,
    "start": 1,
    "display": 10,
    "items": [
        {
            "title": "MHL 케이블 (아이폰, <b>안드로이드</b> 스마트폰 HDMI TV연결)",
            "link": "https://search.shopping.naver.com/gate.nhn?id=10782444869",
            "image": "https://shopping-phinf.pstatic.net/main_1078244/10782444869.5.jpg",
            "lprice": "16500",
            "hprice": "0",
            "mallName": "투데이샵",
            "productId": "10782444869",
            "productType": "2"
        },
        {
            "title": "파인디지털 파인드라이브 Q300",
            "link": "https://search.shopping.naver.com/gate.nhn?id=19490416717",
            "image": "https://shopping-phinf.pstatic.net/main_1949041/19490416717.20190527115824.jpg",
            "lprice": "227050",
            "hprice": "359000",
            "mallName": "네이버",
            "productId": "19490416717",
            "productType": "1"
        },
        {
            "title": "주파집 USB NEW 마그네틱 5핀 <b>안드로이드</b> 자석 고속충전케이블",
            "link": "https://search.shopping.naver.com/gate.nhn?id=16222651410",
            "image": "https://shopping-phinf.pstatic.net/main_1622265/16222651410.20181120154423.jpg",
            "lprice": "6500",
            "hprice": "11900",
            "mallName": "네이버",
            "productId": "16222651410",
            "productType": "1"
        },
        {
            "title": "MHL 케이블 아이폰 <b>안드로이드</b> HDMI 미러링",
            "link": "https://search.shopping.naver.com/gate.nhn?id=11859583359",
            "image": "https://shopping-phinf.pstatic.net/main_1185958/11859583359.1.jpg",
            "lprice": "12500",
            "hprice": "0",
            "mallName": "가가넷",
            "productId": "11859583359",
            "productType": "2"
        },
        {
            "title": "아이폰삼각대 / ios&amp;<b>Android</b> 호환 가능",
            "link": "https://search.shopping.naver.com/gate.nhn?id=16341221561",
            "image": "https://shopping-phinf.pstatic.net/main_1634122/16341221561.4.jpg",
            "lprice": "31900",
            "hprice": "0",
            "mallName": "포시즌몰",
            "productId": "16341221561",
            "productType": "2"
        },
        {
            "title": "뷰잉 (viewing)",
            "link": "https://search.shopping.naver.com/gate.nhn?id=13030462232",
            "image": "https://shopping-phinf.pstatic.net/main_1303046/13030462232.20190306144248.jpg",
            "lprice": "87110",
            "hprice": "180000",
            "mallName": "네이버",
            "productId": "13030462232",
            "productType": "1"
        },
        {
            "title": "샤오미 Mi Box (TELEBEE)",
            "link": "https://search.shopping.naver.com/gate.nhn?id=12302122742",
            "image": "https://shopping-phinf.pstatic.net/main_1230212/12302122742.20170920112004.jpg",
            "lprice": "54900",
            "hprice": "99000",
            "mallName": "네이버",
            "productId": "12302122742",
            "productType": "1"
        },
        {
            "title": "MHL 케이블 아이폰 <b>안드로이드</b> HDMI 미러링 TV연결",
            "link": "https://search.shopping.naver.com/gate.nhn?id=8678305242",
            "image": "https://shopping-phinf.pstatic.net/main_8678305/8678305242.5.jpg",
            "lprice": "5500",
            "hprice": "0",
            "mallName": "글로벌텐교",
            "productId": "8678305242",
            "productType": "2"
        },
        {
            "title": "파인디지털 파인드라이브 Q30",
            "link": "https://search.shopping.naver.com/gate.nhn?id=18711239261",
            "image": "https://shopping-phinf.pstatic.net/main_1871123/18711239261.20190415105108.jpg",
            "lprice": "199000",
            "hprice": "315640",
            "mallName": "네이버",
            "productId": "18711239261",
            "productType": "1"
        },
        {
            "title": "이노아이오 스마트빔 3",
            "link": "https://search.shopping.naver.com/gate.nhn?id=14032821135",
            "image": "https://shopping-phinf.pstatic.net/main_1403282/14032821135.20180413144450.jpg",
            "lprice": "259870",
            "hprice": "387000",
            "mallName": "네이버",
            "productId": "14032821135",
            "productType": "1"
        }
    ]
}
"""

client_id = apikeys.client_id
client_secret = apikeys.client_secret
naver_open_api = 'https://openapi.naver.com/v1/search/shop.json?query=무선충전기'
header_params = {"X-Naver-Client-Id":client_id, "X-Naver-Client-Secret":client_secret}
res = requests.get(naver_open_api, headers=header_params)
if res.status_code == 200:
    data = res.json()
    for index, item in enumerate(data['items']):
        print (index + 1, item['title'], item['link'])
else:
    print ("Error Code:", res.status_code)

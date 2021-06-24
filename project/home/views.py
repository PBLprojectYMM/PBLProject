from os import name
from django import http
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import vaccine_pincode
import requests
import json

# Create your views here.



def index(request):
    context = {
        'variable': 'I will do it'
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


# def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name= name, email=email, desc=desc, date=datetime.today())
        contact.save()

    return render(request, 'contact.html')


def updates(request):
    api = 'https://disease.sh/v3/covid-19/all'
    json_data = requests.get(api).json()
    content = {
    "updated_at" : json_data['updated'],
    # "date" : datetime.fromtimestamp["updated_at"/1e3],
    "total_cases" : str(json_data['cases']),
    "today_cases" : str(json_data['todayCases']),
    "deaths" : str(json_data['deaths']),
    "today_deaths" : str(json_data['todayDeaths']),
    "recovered" : str(json_data['recovered']),
    "today_recovered" : str(json_data['todayRecovered']),
    "active" : str(json_data['active']),
    "test" : str(json_data['tests']),
    "affected_countries" : str(json_data['affectedCountries']) }
    
    return render(request, 'index.html', content)

def vaccine_pin(request):
    if request.method == 'POST':
        pincode = request.POST.get('pincode')
        date = request.POST.get('date')
        da_ta = vaccine_pincode(pincode= pincode, date= date)
        da_ta.save()
    return render(request, 'vaccine.html')

def vaccine_print(request):
# if request.method == 'POST':
    # obj = vaccine_pincode.objects.get(id=24)

    pincode = request.POST.get('pincode')
    date = request.POST.get('date')
    date = datetime.strptime(str(date), '%Y-%m-%d').strftime('%d-%m-%Y')
    params = {
        'pincode': pincode,
        'date': date
        }

    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
        }

    URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin'

    response = requests.get(url=URL, params=params, headers=headers)
    # response.headers.get("Content-Type")

    data = response.json()
    data1 = (json.dumps(data, indent=4))

    data2 = json.loads(data1)
    ses = {}

    for session in data2["sessions"]:
        ses= {
            "center_id": session["center_id"],
            "name": session["name"],
            "address": session['address'],
            'state_name': session['state_name'],
            'district_name': session['district_name'],
            'block_name': session['block_name'],
            'pincode': session['pincode'],
            'from': session['from'],
            'to': session['to'],
            'fee_type': session['fee_type'],
            'session_id': session['session_id'],
            'date': session['date'],
            'fee': session['fee'],
            'min_age_limit': session['min_age_limit'],
            'vaccine': session['vaccine'],
            'slots': session['slots']
            }
    
    context = {
            "center_id": ses["center_id"],
            "name": ses["name"],
            "address": ses['address'],
            'state_name': ses['state_name'],
            'district_name': ses['district_name'],
            'block_name': ses['block_name'],
            'pincode': ses['pincode'],
            'from': ses['from'],
            'to': ses['to'],
            'fee_type': ses['fee_type'],
            'session_id': ses['session_id'],
            'date': ses['date'],
            'fee': ses['fee'],
            'min_age_limit': ses['min_age_limit'],
            'vaccine': ses['vaccine'],
            'slots': ses['slots']
            }

    return render(request, "vaccine.html", context)


# def get_covid_datd(request):
#     api = 'https://disease.sh/v3/covid-19/all'
#     json_data = requests.get(api).json()
#     updated_at = json_data['updated']
#     date = datetime.datetime.fromtimestamp(updated_at/1e3)
#     total_cases = str(json_data['cases'])
#     today_cases = str(json_data['todayCases'])
#     deaths = str(json_data['deaths'])
#     today_deaths = str(json_data['todayDeaths'])
#     recovered = str(json_data['recovered'])
#     today_recovered = str(json_data['todayRecovered'])
#     active = str(json_data['active'])
#     test = str(json_data['tests'])
#     affected_countries = str(json_data['affectedCountries'])
#     print("updated at=",date,'\n',"\n","Total Cases=",total_cases,"\t","Today Cases=",today_cases,"\n"
#           "  Deaths=",deaths,"\t","\t","\t","Today Deaths=",today_deaths,"\n","Recovered=",recovered,"\t",
#           "Today Recovered=",today_recovered,"\n","\n","Active=",active,"\n","Test=",test,"\n",
#           "Affected Countries=",affected_countries )
#     values = ["updated at=",date,'\n',"\n","Total Cases=",total_cases,"\t","Today Cases=",today_cases,"\n"
#           "  Deaths=",deaths,"\t","\t","\t","Today Deaths=",today_deaths,"\n","Recovered=",recovered,"\t",
#           "Today Recovered=",today_recovered,"\n","\n","Active=",active,"\n","Test=",test,"\n",
#           "Affected Countries=",affected_countries]
#     # values = {
#     #     "updated at": datetime.datetime.fromtimestamp(updated_at/1e3),"Total Cases=": total_cases,"Today Cases": today_cases,
#     #       "Deaths": deaths,"Today Deaths": today_deaths,"Recovered": recovered,
#     #       "Today Recovered": today_recovered, "Active": active,"Test": test,
#     #       "Affected Countries": affected_countries}

#     # ["updated at",date,
#     # total_cases,
#     # today_cases,
#     # deaths,
#     # today_deaths,
#     # recovered,
#     # today_recovered,
#     # active,
#     # test,
#     # affected_countries]

#     return render(request, 'covid_update.html')
def get_news(request):
    api = 'https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=f04b2319954b4416aff255504f617789'
    respones = requests.get(api)
    data = respones.json()
    data1 = (json.dumps(data, indent=4))
    data2 = json.loads(data1)
    content = {}
    
    for article in data2["articles"][0:1]:
       content= {
            "title" : article['title'],
            "url" : article['url'],
            "urlToImage" : article['urlToImage'],
            "published_on" : article['publishedAt'][:10] }

    for article in data2["articles"][1:2]:
       content1= {
            "title1" : article['title'],
            "url1" : article['url'],
            "urlToImage1" : article['urlToImage'],
            "published_on1" : article['publishedAt'][:10] }
    # print(content)

    for article in data2["articles"][2:3]:
       content2= {
            "title2" : article['title'],
            "url2" : article['url'],
            "urlToImage2" : article['urlToImage'],
            "published_on2" : article['publishedAt'][:10] }
    
    for article in data2["articles"][3:4]:
       content3= {
            "title3" : article['title'],
            "url3" : article['url'],
            "urlToImage3" : article['urlToImage'],
            "published_on3" : article['publishedAt'][:10] }
    
    for article in data2["articles"][4:5]:
       content4= {
            "title4" : article['title'],
            "url4" : article['url'],
            "urlToImage4" : article['urlToImage'],
            "published_on4" : article['publishedAt'][:10] }
    
    for article in data2["articles"][5:6]:
       content5= {
            "title5" : article['title'],
            "url5" : article['url'],
            "urlToImage5" : article['urlToImage'],
            "published_on5" : article['publishedAt'][:10] }
    
    for article in data2["articles"][6:7]:
       content6= {
            "title6" : article['title'],
            "url6" : article['url'],
            "urlToImage6" : article['urlToImage'],
            "published_on6" : article['publishedAt'][:10] }
    
    for article in data2["articles"][7:8]:
       content7= {
            "title7" : article['title'],
            "url7" : article['url'],
            "urlToImage7" : article['urlToImage'],
            "published_on7" : article['publishedAt'][:10] }

    for article in data2["articles"][8:9]:
       content8= {
            "title8" : article['title'],
            "url8" : article['url'],
            "urlToImage8" : article['urlToImage'],
            "published_on8" : article['publishedAt'][:10] }
    

    context = {
        "content_title": content["title"],
        "content_url": content["url"], 
        "content_urlToImage": content["urlToImage"], 
        "content_published_on": content["published_on"], 
        "content1_title1": content1["title1"], 
        "content1_url1": content1["url1"], 
        "content1_urlToImage1": content1["urlToImage1"], 
        "content1_published_on1": content1["published_on1"], 
        "content2_title2": content2["title2"],
        "content2_url2": content2["url2"], 
        "content2_urlToImage2": content2["urlToImage2"], 
        "content2_published_on2": content2["published_on2"],
        "content3_title3": content3["title3"],
        "content3_url3": content3["url3"], 
        "content3_urlToImage3": content3["urlToImage3"], 
        "content3_published_on3": content3["published_on3"],
        "content4_title4": content4["title4"],
        "content4_url4": content4["url4"], 
        "content4_urlToImage4": content4["urlToImage4"], 
        "content4_published_on4": content4["published_on4"],
        "content5_title5": content5["title5"],
        "content5_url5": content5["url5"], 
        "content5_urlToImage5": content5["urlToImage5"], 
        "content5_published_on5": content5["published_on5"],
        "content6_title6": content6["title6"],
        "content6_url6": content6["url6"], 
        "content6_urlToImage6": content6["urlToImage6"], 
        "content6_published_on6": content6["published_on6"],
        "content7_title7": content7["title7"],
        "content7_url7": content7["url7"], 
        "content7_urlToImage7": content7["urlToImage7"], 
        "content7_published_on7": content7["published_on7"],
        "content8_title8": content8["title8"],
        "content8_url8": content8["url8"], 
        "content8_urlToImage8": content8["urlToImage8"], 
        "content8_published_on8": content8["published_on8"]
    }

    return render(request, 'news.html', context)
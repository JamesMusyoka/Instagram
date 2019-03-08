from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt

def  index(request):
    date = dt.date.today()

    
    html = f'''
        <html>
            <body>
                <h1> {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return render(request, 'index.html',{'date':date})


def convert_dates(dates):

    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    day = days[day_number]
    return day

def profile(request,profile):
    return HttpResponse(html)

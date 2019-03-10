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
     date = dt.date.today()
     return render(request, 'profile.html', {"date": date,})

def search_results(request,search_results):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)

        message = "{search_term}"
        return render(request, 'search_results.html', {"message":message, "images": searched_images})

    else:
        message = "You haven't made any terms"
        return render(request, 'search_results.html', {"message":message})

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

monthly_challenges = {
    "january": "This is for January!",
    "february": "This is for February!",
    "march": "This is for March!",
    "april": "This is for April!",
    "may": "This is for May!",
    "june": "This is for June!",
    "july": "This is for July!",
    "august": "This is for August!",
    "september": "This is for September!",
    "october": "This is for October!",
    "november": "This is for November!",
    "december": "This is for December!",
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month_challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def month_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("There is no key like that in the month!")
    else:
        redirect_month = months[month - 1]
        redirect_path = reverse("month_challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)

def month_challenge(request, month):
    try:
       challenges_text = monthly_challenges[month.lower()]
       response_data = f"<h1>{challenges_text}</h1>"
       return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>Give me the valid month name!</h1>")


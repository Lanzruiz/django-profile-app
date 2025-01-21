from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
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

def month_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("There is no key like that in the month!")
    else:
        redirect_month = months[month - 1]
        return HttpResponseRedirect("/challenges/" + redirect_month)

def month_challenge(request, month):
    try:
       challenges_text = monthly_challenges[month.lower()]
       return HttpResponse(challenges_text)
    except:
        return HttpResponseNotFound("Give me the valid month name!")


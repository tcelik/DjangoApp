from django.http import HttpResponse

def year_archive(request, year):
    return HttpResponse("{0}, {1}".format(year, "tugberk"))
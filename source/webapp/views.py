from django.shortcuts import render

from webapp.cat import Cat


my_cat = Cat("Unknown")

def index(request):
    if request.method == "GET":
        return render(request, "index.html")


def cat(request):
    my_cat.name = request.POST.get("cat_name") if request.POST.get("cat_name") else my_cat.name
    print(request.POST.get("act"))
    if request.POST.get("act") == "play":
        my_cat.play()
    elif request.POST.get("act") == "feed":
        my_cat.feed()
    elif request.POST.get("act") == "sleep":
        my_cat.sleep()
    return render(request, "cat.html", context=my_cat.dict())


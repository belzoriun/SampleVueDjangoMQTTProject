from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
import json
from ..managers import usermanager

def user(request):
    if request.method == "GET":
        user = usermanager.get_user_info(request.GET.get("userid"))
        if user:
            return HttpResponse(json.dumps({"code":"OK", "data":user}))
        else:
            return HttpResponseBadRequest(json.dumps({"code":"USER_NOT_FOUND"}))
    elif request.method == "POST":
        id = request.POST.get("id")
        if id:
            usermanager.set_user_info(
                id,
                request.POST.get("firstname"),
                request.POST.get("lastname"),
                request.POST.get("email"),
                request.POST.get("login"),
            )
        else:
            id=usermanager.add_user(
                request.POST.get("firstname"),
                request.POST.get("lastname"),
                request.POST.get("email"),
                request.POST.get("login"),
            )
            #TODO : send mail
        return HttpResponse(json.dumps({"code":"OK", "id":str(id)}))
    return HttpResponseNotAllowed(["GET", "POST"])

def userById(request, id):
    if request.method == "GET":
        return HttpResponse(json.dumps({"code":"OK", "data":usermanager.get_user_info(id)}))
    elif request.method == "DELETE":
        return HttpResponseBadRequest({"code":"NOT_YET_INTEGRATED"})
    return HttpResponseNotAllowed(["GET", "DELETE"])

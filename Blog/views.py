from django.shortcuts import render ,HttpResponse

from django.http import JsonResponse
def sayHello(req):
    return JsonResponse({"message": "how are you"})

def postUser(req):
    return JsonResponse({"message ":"posted a user"})


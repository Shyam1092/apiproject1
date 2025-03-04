from django.shortcuts import render
from .models import *
from .serialization import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests

# Create your views here.

@api_view(['GET'])
def getall(request):
    stdata=todo.objects.all()
    serial=todoSerializer(stdata,many=True)
    return Response(data=serial.data)

@api_view(['GET'])
def getid(request,id):
    try:
        stid=todo.objects.get(id=id)
    except todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serial=todoSerializer(stid)
    return Response(data=serial.data)


@api_view(['GET','DELETE'])
def deleteid(request,id):
    try:
        stid=todo.objects.get(id=id)
    except todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serial=todoSerializer(stid)
        return Response(data=serial.data)
    if request.method=='DELETE':
        todo.delete(stid)
        return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['POST'])
def savedata(request):
    if request.method=='POST':
        serail=todoSerializer(data=request.data)
        if serail.is_valid():
            serail.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET','PUT'])
def updatedata(request,id):
    try:
        stid=todo.objects.get(id=id)
    except todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serial=todoSerializer(stid)
        return Response(data=serial.data)
    if request.method=='PUT':
        serail=todoSerializer(data=request.data,instance=stid)
        if serail.is_valid():
            serail.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
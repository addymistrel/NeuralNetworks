from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
from . import costGenerator

# Create your views here.
@api_view(['GET'])
def getData(request):
    return Response("my name is Aditya")

@api_view(['POST'])
def newData(request):
    gotDataDic = json.loads(request.body.decode("utf-8"))
    print(gotDataDic,type(gotDataDic))
    newTrain = costGenerator.CostGenrator(int(gotDataDic["each1"]),int(gotDataDic["no"]),0)
    result = newTrain.generateCost()
    returnData = {"routePoints":result[0],"totalCost":result[1],"weightFull":result[2]}
    print(returnData)
    return Response(json.dumps(returnData))
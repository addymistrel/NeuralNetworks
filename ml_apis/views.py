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
    newTrain = costGenerator.CostGenrator(int(gotDataDic["wagcap"]),int(gotDataDic["wagno"]),0,gotDataDic["graphPlot"])
    result = newTrain.generateCost()
    # print(result)
    returnData = {"routePoints":result[0],"totalCost":result[1],"weightFull":result[2]}
    print(returnData)
    return Response(json.dumps(returnData))
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
from . import costGenerator
import pickle
# model = pickle.load(open('model.pkl','rb'))

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
    returnData = {"routePoints":result[0],"totalCost":result[1],"weightFull":result[2],"weightsEach":result[3],"stockFactor":result[4]}
    print(returnData)
    return Response(json.dumps(returnData))

@api_view(['POST'])
def mloutput(request):
    gotDataDic = json.loads(request.body.decode("utf-8"))
    print(gotDataDic,type(gotDataDic))
    return Response(json.dumps(gotDataDic))
    # x = model.predict([[x1,x2,x3]])[0][0]
    # # st.subheader(x)0
    # if x > 0.51514834:
    #     print(1)
    # else:
    #     print(2)
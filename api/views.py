import pickle
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import pandas as pd
import os
# Create your views here.



class LoginView(APIView):

    def analyse(self, data):
        model_path = "static/model/big_model.pkl"
        with open(model_path, 'rb') as infile:
            model = pickle.load(infile)
        content = str(data).strip()
        l = []
        l.append(content)
        new_x = model['tfidf'].transform(l)
        new_y_pred = model['lr'].predict(new_x)
        res = pd.DataFrame({
            '预测': model['y_encoder'].inverse_transform(new_y_pred),
        })
        return res



    def post(self, request, *args, **kwargs):
        print(request.data['news'])

        result = self.analyse(request.data['news'])
        print(result)
        return Response({
            "res": result
        })

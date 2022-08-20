from django.shortcuts import render, HttpResponse
import pandas as pd
from django.http import JsonResponse

import json

# Create your views here.


def home(request):
    # r=None
    # data = pd.read_excel (r'C:\Users\Kishor Kore\Desktop\pandas\master8_excel.xlsx')

    # if request.method=='POST':
    #     agent_data=request.POST['agent']
    #     subclint_data=request.POST['Subclient']
    #     job_status_data=request.POST['Job status']

    #     if agent_data and subclint_data and job_status_data is not None:
    #         l1=list(data[data['Job_status'].str.contains("{}".format(job_status_data)) & (data[data.columns[4]].str.contains("{}".format(subclint_data)) & data[data.columns[2]].str.contains("{}".format(agent_data)))].index).T
    #         data=data.loc[l1]
    #         data=data.to_dict()
    #         return render(request,'show_data.html',{'df':data})

    #     elif agent_data==''and subclint_data=='' and job_status_data is not None:
    #         data=data[data['Job_status'].str.contains("{}".format(job_status_data),na=False)]
    #         # return render(request,'show_data.html',{'df':data})

    #     elif agent_data=='' and job_status_data=='' and subclint_data is not None:
    #         data=data[data[data.columns[4]].str.contains("{}".format(subclint_data),na=False)]

    #     elif subclint_data=='' and job_status_data=='' and agent_data is not None:
    #         data=data[data[data.columns[2]].str.contains("{}".format(agent_data),na=False)]
    #         if data is None:
    #             return render(request,'show_data.html',{'df':data,r:r})
    #     else:
    #         return render(request,'show_data.html',{'df':data,r:r})

    #     data=data.to_dict()
    #     return render(request,'show_data.html',{'df':data})
    # data=data.iloc[0:11]
    # data=data.to_dict()
    # # print(data)
    # return render(request,'show_data.html',{'df':data})
    return render(request, 'show_data.html')


def aj(request):

    if request.method == "GET":
        nick_name = request.GET['search_content']

        data = pd.read_excel(
            r'C:\Users\Kishor Kore\Desktop\pandas\master8_excel.xlsx')

        data = data[data['Subclient'].str.contains(
            "{}".format(nick_name), na=False, case=False)]

        data = data.fillna('')
        ms = data.to_dict('index')

        list_data = list(ms.values())

        jsondata = {'data': list_data}
        return JsonResponse(jsondata)


def aj1(request):

    if request.method == "GET":
        nick_name = request.GET['search_content']

        data = pd.read_excel(
            r'C:\Users\Kishor Kore\Desktop\pandas\master8_excel.xlsx')

        data = data[data['Job_status'].str.contains(
            "{}".format(nick_name), na=False, case=False)]

        data = data.fillna('')
        ms = data.to_dict('index')

        list_data = list(ms.values())

        jsondata = {'data': list_data}
        return JsonResponse(jsondata)


def aj2(request):

    if request.method == "GET":
        nick_name = request.GET['search_content']

        data = pd.read_excel(
            r'C:\Users\Kishor Kore\Desktop\pandas\master8_excel.xlsx')

        data = data[data['Server'].str.contains(
            "{}".format(nick_name), na=False, case=False)]

        data = data.fillna('')
        ms = data.to_dict('index')

        list_data = list(ms.values())

        jsondata = {'data': list_data}
        return JsonResponse(jsondata)


def hello(request):

    if request.method == "GET":
        data = pd.read_excel(
            r'C:\Users\Kishor Kore\Desktop\pandas\master8_excel.xlsx')
        data = data.fillna('')
        ms = data.to_dict('index')

        list_data = list(ms.values())

        jsondata = {'data': list_data}

        return JsonResponse(jsondata)

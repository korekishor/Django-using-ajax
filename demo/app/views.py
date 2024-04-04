from django.shortcuts import render, HttpResponse
import pandas as pd
from django.http import JsonResponse
from nltk.tokenize import word_tokenize
import json
import requests as r
import pyodbc
# Create your views here.
server = 'cisco-db-instance-kk.czyuq0wca34e.eu-north-1.rds.amazonaws.com'
database = 'cisco-db-instance-kk'
username = 'root'
password = 'cisco-db-instance-kk'

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};\
                      SERVER='+server+';\
                      UID='+username+';\
                      PWD='+ password)
print("_______________")

cursor = cnxn.cursor()
print("_______________",cursor)

def auto(request):
    if request.method == "GET":
        str1 = request.GET['search_content']
        google_serch=str1
        df=pd.read_csv(r"C:\Users\Kishor Kore\Desktop\pandas\bag_of_words")
        df.rename(columns = {df.columns[0]:'TEST'}, inplace = True)

        str1=str1.lower()
        words_serch=word_tokenize(str1)
        ds=df[df['col_1'].str.startswith(words_serch[-1])].index 

        list_val=[df['col_1'][x] for x in ds]
        words=word_tokenize(str1)
        lenw=len(words[-1])

        str_val=[str1[:len(str1)-lenw]+str(x) for x in list_val]

        jsondata = {'data': str_val}
        return JsonResponse(jsondata)



        url="http://suggestqueries.google.com/complete/search"
        params={
            'client':"firefox",
            'q':'{}'.format(google_serch),
            'hl':'en'
        }

        re=r.get(url,params=params)
        list_val=re.json()[1][:]
        str_val=[str1[:len(str1)-lenw]+str(x) for x in list_val]

        jsondata = {'data': str_val}
        return JsonResponse(jsondata)

def home(request):
    # r=None 
    return render(request, 'show_data.html')


# def aj(request):

#     if request.method == "GET":
#         nick_name = request.GET['search_content']

#         data = pd.read_excel(
#             r'C:\Users\Kishor Kore\Desktop\pandas\master8_excel.xlsx')

#         data = data[data['Subclient'].str.contains(
#             "{}".format(nick_name), na=False, case=False)]

#         data = data.fillna('')
#         ms = data.to_dict('index')

#         list_data = list(ms.values())

#         jsondata = {'data': list_data}
#         return JsonResponse(jsondata)


# def aj1(request):

#     if request.method == "GET":
#         nick_name = request.GET['search_content']

#         data = pd.read_excel(
#             r'C:\Users\Kishor Kore\Desktop\pandas\master8_excel.xlsx')

#         data = data[data['Job_status'].str.contains(
#             "{}".format(nick_name), na=False, case=False)]

#         data = data.fillna('')
#         ms = data.to_dict('index')

#         list_data = list(ms.values())

#         jsondata = {'data': list_data}
#         return JsonResponse(jsondata)


# def aj2(request):

#     if request.method == "GET":
#         nick_name = request.GET['search_content']

#         data = pd.read_excel(
#             r'C:\Users\Kishor Kore\Desktop\pandas\master8_excel.xlsx')

#         data = data[data['Server'].str.contains(
#             "{}".format(nick_name), na=False, case=False)]

#         data = data.fillna('')
#         ms = data.to_dict('index')

#         list_data = list(ms.values())

#         jsondata = {'data': list_data}
#         return JsonResponse(jsondata)


# def hello(request):

#     if request.method == "GET":
#         data = pd.read_excel(
#             r'C:\Users\Kishor Kore\Desktop\pandas\master8_excel.xlsx')
#         data = data.fillna('')
#         ms = data.to_dict('index')

#         list_data = list(ms.values())

#         jsondata = {'data': list_data}

#         return JsonResponse(jsondata)


# <script>

#     // output = "",
#     //     $.ajax({
#     //         url: 'auto',
#     //         type: 'GET',
#     //         success: function (ress) {
#     //             data = ress['data']
#     //             console.log(ress)

#     //             output = ""
#     //             for (i = 0; i < data.length; i++) {
#     //                 output += "<tr><td>" + data[i].Job_ID + "</td><td>" + data[i].Server + "</td><td>" + data[i].Agent + "</td><td>" + data[i].BackupSet + "</td><td>" + data[i].Subclient + "</td><td>" + data[i].Backup_Type
#     //                     + "</td><td>" + data[i].Backup_Type + "</td><td>" + data[i].Start_Time + "</td><td>" + "</td><td>" + data[i].MediaAgent + data[i].Job_status + "</td><td>" + data[i].Virtualization_Client
#     //             }
#     //             $("#tbody").html(output);
#     //         },
#     //         failure: function (data) {
#     //             alert('Got an error dude');
#     //         }
#     //     });

#     $("#Auto_search").on("change paste keyup", function () {
#         var search_content = $(this).val();
#         output = "";
#         console.log(search_content)
#         $.ajax({
#             type: 'GET',
#             url: "{% url 'aj1' %}",
#             data: { "search_content": search_content },

#             success: function (ress) {
#                 console.log(ress)
#                 data = ress['data']
#                 console.log(ress)
#                 output = ""

#                 for (i = 0; i < data.length; i++) {
#                     output += "<tr><td>" + data[i].Job_ID + "</td><td>" + data[i].Server + "</td><td>" + data[i].Agent + "</td><td>" + data[i].BackupSet + "</td><td>" + data[i].Subclient + "</td><td>" + data[i].Backup_Type
#                         + "</td><td>" + data[i].Backup_Type + "</td><td>" + data[i].Start_Time + "</td><td>" + "</td><td>" + data[i].MediaAgent + data[i].Job_status + "</td><td>" + data[i].Virtualization_Client
#                 }
#                 $("#tbody").html(output);
#             },
#             failure: function (data) {
#                 alert('Got an error dude');
#             }
#         })
#     })
#     // $("#myTextBox").on("change paste keyup", function () {
#     //     var search_content = $(this).val();
#     //     output = "";
#     //     console.log(search_content)
#     //     $.ajax({
#     //         type: 'GET',
#     //         url: "{% url 'aj' %}",
#     //         data: { "search_content": search_content },

#     //         success: function (ress) {
#     //             console.log(ress)
#     //             data = ress['data']
#     //             console.log(ress)
#     //             output = ""

#     //             for (i = 0; i < data.length; i++) {
#     //                 output += "<tr><td>" + data[i].Job_ID + "</td><td>" + data[i].Server + "</td><td>" + data[i].Agent + "</td><td>" + data[i].BackupSet + "</td><td>" + data[i].Subclient + "</td><td>" + data[i].Backup_Type
#     //                     + "</td><td>" + data[i].Backup_Type + "</td><td>" + data[i].Start_Time + "</td><td>" + "</td><td>" + data[i].MediaAgent + data[i].Job_status + "</td><td>" + data[i].Virtualization_Client
#     //             }
#     //             $("#tbody").html(output);
#     //         },
#     //         failure: function (data) {
#     //             alert('Got an error dude');
#     //         }
#     //     })
#     // })

#     // $("#myTextBox1").on("change paste keyup", function () {
#     //     var search_content = $(this).val();
#     //     output = "";
#     //     console.log(search_content)
#     //     $.ajax({
#     //         type: 'GET',
#     //         url: "{% url 'aj1' %}",
#     //         data: { "search_content": search_content },

#     //         success: function (ress) {
#     //             console.log(ress)
#     //             data = ress['data']
#     //             console.log(ress)
#     //             output = ""

#     //             for (i = 0; i < data.length; i++) {
#     //                 output += "<tr><td>" + data[i].Job_ID + "</td><td>" + data[i].Server + "</td><td>" + data[i].Agent + "</td><td>" + data[i].BackupSet + "</td><td>" + data[i].Subclient + "</td><td>" + data[i].Backup_Type
#     //                     + "</td><td>" + data[i].Backup_Type + "</td><td>" + data[i].Start_Time + "</td><td>" + "</td><td>" + data[i].MediaAgent + data[i].Job_status + "</td><td>" + data[i].Virtualization_Client
#     //             }
#     //             $("#tbody").html(output);
#     //         },
#     //         failure: function (data) {
#     //             alert('Got an error dude');
#     //         }
#     //     })
#     // })

#     // $("#myTextBox2").on("change paste keyup", function () {
#     //     var search_content = $(this).val();
#     //     output = "";
#     //     console.log(search_content)
#     //     $.ajax({
#     //         type: 'GET',
#     //         url: "{% url 'aj2' %}",
#     //         data: { "search_content": search_content },

#     //         success: function (ress) {
#     //             console.log(ress)
#     //             data = ress['data']
#     //             console.log(ress)
#     //             output = ""

#     //             for (i = 0; i < data.length; i++) {
#     //                 output += "<tr><td>" + data[i].Job_ID + "</td><td>" + data[i].Server + "</td><td>" + data[i].Agent + "</td><td>" + data[i].BackupSet + "</td><td>" + data[i].Subclient + "</td><td>" + data[i].Backup_Type
#     //                     + "</td><td>" + data[i].Backup_Type + "</td><td>" + data[i].Start_Time + "</td><td>" + "</td><td>" + data[i].MediaAgent + data[i].Job_status + "</td><td>" + data[i].Virtualization_Client
#     //             }
#     //             $("#tbody").html(output);
#     //         },
#     //         failure: function (data) {
#     //             alert('Got an error dude');
#     //         }
#     //     })
#     // })


# </script>

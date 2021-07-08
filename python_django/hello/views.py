from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# import sqlite3
# from .models import Files
from mogo import connect, session

connect("fileww")

@csrf_exempt
def home(request):
    # from pymongo import Connection

    # databaseName = "fileww"
    # connection = Connection()

    # fileDB = connection.databaseName
    # # db = connection.databaseName.employees = db('files')
    # file1 = { "name" : "file-name","fileSrc" : "fileSrc"}
    # file2 = { "name" : "file-name2","fileSrc" : "fileSrc2"}
    # print ("clearing")
    # fileDB.remove()
    # print ("saving")
    # fileDB.save(file1)
    # fileDB.save(file2)
    # print ("searching")
    # for e in fileDB.find():
    #     print (e["name"] + " " + unicode(e["fileSrc"]))

# ------------------------------trying to connect to sqlite, havent succeeded yet---------------------------
    # connection = sqlite3.connect('fileDjango.db')
    # cursor = connection.execute('select * from fileDjango.db')
    # names = list(map(lambda x: x[0], cursor.description))
    # print(names)
# ------------------------------trying to connect to sqlite, havent succeeded yet---------------------------
    # conn = sqlite3.connect("db.sqlite3")
    # c = conn.cursor()
    # print("c")
    # print(c)
    # print("c")
    # c.execute("INSERT INTO files (name, fileSrc) VALUES(?, ?)", ("fileName", "fileSrc"))
    # c.execute("select * from files")
    # files = []
    # for row in c.execute("SELECT * FROM files"):
    #     currFile = {
    #         'name': row[0],
    #         'fileSrc': row[1]
    #     }
    #     print(currFile)
    #     files.append(currFile)
    # c.commit()
# ------------------------------trying to connect to sqlite, havent succeeded yet---------------------------
    print(request.method)
    if(request.method == 'GET'):
        print('holly shit im in GET')
        examplefile = {
            'name': 'hadar',
            'fileSrc': 'hadar'
        }
        # Files.get("files", ["big darn hero"])
        return HttpResponse(examplefile)
    if(request.method == 'POST'):
        print('holly shit im in POST')
        print(request.body)
        post_data=request.body # result is bytes
        post_data_str = post_data.decode("utf-8") # result is string
        startIndex = post_data_str.index('","fileSrc') 
        fileName = post_data_str[9:startIndex]
        updateStertIdx = startIndex+13
        fileSrc = post_data_str[updateStertIdx:-2]
        print(fileName)
        print(fileSrc)
        #insert into DB!!!!!!!!!

        return HttpResponse("hadar is the king of POSTS")
    return HttpResponse(request)

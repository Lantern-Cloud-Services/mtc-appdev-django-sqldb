from django.shortcuts import render
from django.http import HttpResponse
import pyodbc

# Create your views here.
def index(request):
    # TODO move app property
    server = 'demo-mtc-appdev-sqlser1.database.windows.net'
    database = 'demo-mtc-appdev-sqldb1'
    username = ''
    password = ''
    driver = '{ODBC Driver 17 for SQL Server}'


    result = "<h1>Hello from django</h1><br /><br /><b>DB Stuff:</b><br />"

#    with pyodbc.connect(
#            'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password) as conn:
#        with conn.cursor() as cursor:
#            cursor.execute("SELECT TOP 3 name, collation_name FROM sys.databases")
#            row = cursor.fetchone()
#            while row:
#                result += str(row[0]) + " " + str(row[1] + "<br />")
#                print(str(row[0]) + " " + str(row[1]))
#                row = cursor.fetchone()

    return HttpResponse(result)

import os
from django.shortcuts import render
from django.http import HttpResponse
import pyodbc

# Create your views here.
def index(request):
    result = "<h1>Hello from django</h1><br /><br /><b>DB Stuff:</b><br />"

    sqlstr = os.environ.get('dbconststr', "dbconststr variable does not exist")

    with pyodbc.connect(sqlstr) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT TOP 3 name, collation_name FROM sys.databases")
            row = cursor.fetchone()
            while row:
                result += str(row[0]) + " " + str(row[1] + "<br />")
                print(str(row[0]) + " " + str(row[1]))
                row = cursor.fetchone()

    return HttpResponse(result)

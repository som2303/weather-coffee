from django.shortcuts import render, HttpResponse
import csv
from .models import DataOrigin, DataSex, DataAge

import json
from django.core.serializers.json import DjangoJSONEncoder


def index(request):
    data = DataOrigin.objects.values()
    data_json = json.dumps(list(data), cls=DjangoJSONEncoder)

    data1 = DataSex.objects.values()
    data_json1 = json.dumps(list(data1), cls=DjangoJSONEncoder)

    data2 = DataAge.objects.values()
    data_json2 = json.dumps(list(data2), cls=DjangoJSONEncoder)
    
    context = {
    #html로 보내는 필드명을 ''(따옴표)안에 넣어주면 됩니다.
    'data_json': data_json,
    'data_json1': data_json1,
    'data_json2': data_json2,
    }
 
 
##html로 값을 보내는 부분    
    return render(request, 'index.html', context)


def add_data(request):
    path = './data/data.csv'
    file = open(path)
    reader = csv.reader(file)
    next(reader)
    list = []
    for row in reader:
        list.append(DataOrigin(temperature=row[1],count=row[2]))
    DataOrigin.objects.bulk_create(list)
    file.close()

    path = './data/data_f.csv'
    file = open(path)
    reader = csv.reader(file)
    next(reader)
    list = []
    for row in reader:
        list.append(DataSex(temperature=row[1],count=row[2],sex=row[3]))
    DataSex.objects.bulk_create(list)
    file.close()
    
    path = './data/data_m.csv'
    file = open(path)
    reader = csv.reader(file)
    next(reader)
    list = []
    for row in reader:
        list.append(DataSex(temperature=row[1],count=row[2],sex=row[3]))
    DataSex.objects.bulk_create(list)

    path = './data/data10.csv'
    file = open(path)
    reader = csv.reader(file)
    next(reader)
    list = []
    for row in reader:
        list.append(DataAge(temperature=row[1],count=row[2],age=row[3]))
    DataAge.objects.bulk_create(list)
    file.close()

    path = './data/data20.csv'
    file = open(path)
    reader = csv.reader(file)
    next(reader)
    list = []
    for row in reader:
        list.append(DataAge(temperature=row[1],count=row[2],age=row[3]))
    DataAge.objects.bulk_create(list)
    file.close()

    path = './data/data30.csv'
    file = open(path)
    reader = csv.reader(file)
    next(reader)
    list = []
    for row in reader:
        list.append(DataAge(temperature=row[1],count=row[2],age=row[3]))
    DataAge.objects.bulk_create(list)
    file.close()

    path = './data/data40.csv'
    file = open(path)
    reader = csv.reader(file)
    next(reader)
    list = []
    for row in reader:
        list.append(DataAge(temperature=row[1],count=row[2],age=row[3]))
    DataAge.objects.bulk_create(list)
    file.close()

    path = './data/data50.csv'
    file = open(path)
    reader = csv.reader(file)
    next(reader)
    list = []
    for row in reader:
        list.append(DataAge(temperature=row[1],count=row[2],age=row[3]))
    DataAge.objects.bulk_create(list)
    file.close()

    path = './data/data60.csv'
    file = open(path)
    reader = csv.reader(file)
    next(reader)
    list = []
    for row in reader:
        list.append(DataAge(temperature=row[1],count=row[2],age=row[3]))
    DataAge.objects.bulk_create(list)
    file.close()

    return HttpResponse("complete")

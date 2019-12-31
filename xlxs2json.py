#!/usr/bin/env python
# -*- coding:utf-8 -*-
import xlrd
import json
file = "cn.xlsx"
data = xlrd.open_workbook(file)
table = data.sheets()[0]
nrows = table.nrows
returnData = {}
for i in range(nrows):
    content = table.row_values(i)
    returnData[content[0]] = content[1]
returnJson = json.dumps(returnData)
print returnJson

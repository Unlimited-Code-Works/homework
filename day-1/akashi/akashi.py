import pyexcel
import json

with open('./courses.json') as json_data:
    data = json.load(json_data)
    pyexcel.save_as(records=data, dest_file_name="akashi.xls")

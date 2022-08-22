import json
sampleJson = { 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}
json_file = "sample.json"
sampleJson["company"]["employee"]["birth_date"] = "20.01.93"
with open(json_file, 'w') as file_obj:
    json.dump(sampleJson, file_obj,indent = 2, sort_keys=True)


# with open(json_file, 'r') as file_obj:
#     sample = json.load(file_obj)



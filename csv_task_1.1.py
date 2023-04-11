import csv
import json

def read_colon_from_file(key: str, file_response: list, file: str):
   with open(file, "r") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        for row in reader:
            if key in row:     
                file_response.append(row[key])                  
def list_of_silts(file1_response: list, file2_response: list, write_file_response: list):
    if len(file1_response) >= len(file2_response):
        i = 0
        while i < len(file1_response):
            write_file_response.append([file1_response[i],  file2_response[i], file1_response[i] == file2_response[i]])
            i+=1
    elif len(file2_response) >= len(file1_response):
        i = 0
        while i < len(file2_response):
            write_file_response.append([file1_response[i],  file2_response[i], file1_response[i] == file2_response[i]])
            i+=1
    else:   
        None

key = 'responseToken'
file1_response = []
file2_response = []
write_file_response = []

read_colon_from_file(key, file1_response, "file1.csv")
read_colon_from_file(key, file2_response, "file2.csv")
list_of_silts(file1_response, file2_response, write_file_response)

# add heders
with open("writing_file.csv", '+w') as writing_file:
    writer = csv.writer(writing_file)
    writer.writerow([key + ' file 1',key + ' file 2', 'Bool'])

# write in file
for element in write_file_response:
    with open("writing_file.csv", '+a') as writing_file:
        writer = csv.writer(writing_file)
        writer.writerow(element)

dictionary = {}
dictionary['file1_response'] = []
for elements in file1_response:
    dictionary['file1_response'].append(elements)
dictionary['file2_response'] = []
for elements in file2_response:
    dictionary['file2_response'].append(elements)
#print(dir(json))

with open('new_file.json', 'w') as f:
    jsonString = json.dump(dictionary, f)

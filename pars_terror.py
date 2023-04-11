import requests
import csv
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class Connector:

    def __init__(self, url: str, headers: dict):
        self.url = url
        self.headers = headers
    
    def execute(self) -> list:
        response = requests.get(self.url, headers = self.headers, verify = False)
        divs = BeautifulSoup(response.text, 'html.parser').find('div', 'ibox-content').find_all('div', 'panel-group')
        return divs[2].find_all('li')

class GetData:

    def __init__(self, liData: str):
        self.liData = liData
    
    def execute(self) -> list:
        list_of_dicts = []
        for element in self.liData:
            data = (element.text).split(',')
            number = data[0].split('.')[0]
            name = data[0].split('.')[1]
            birthday = data[1]
            try:
                city = data[2]
            except:
                city = ''
            slovar = {'number': number, 'name': name, 'birthday': birthday, 'city': city}
            list_of_dicts.append(slovar)
        return list_of_dicts

class SaveToFile:

    def __init__(self, fieldnames: list):
        self.fieldnames = fieldnames

    def execute(self, delimiter: str = ',', list_of_dicts: list = [], fileNameToSave: str = 'terrorists.csv'):
        with open(fileNameToSave, '+w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, delimiter = ',', fieldnames = self.fieldnames)
            writer.writeheader()
            print('count: ' + str(len(list_of_dicts)))
            for element in list_of_dicts:
                writer.writerow(element)

class Terrorist:

    def __init__(self, number: str, name: str, birthday: str, city: str):
        self.number = number
        self.name = name
        self.birthday = birthday
        self.city = city
    
    def getNumber(self):
        return self.number
    
    def getName(self):
        return self.name
    
    def getBirthday(self):
        return self.birthday
    
    def getCity(self):
        return self.city

# terr = Terrorist('2', 'Test Testov Testovich', '21.03.1990', 'Blablabvlalblsagjdbfkgjs')

# slovar = {'number': terr.getNumber(), 'name': terr.getName(), 'birthDay': terr.getName(), 'city': terr.getCity()}


class GetTerroristFromFedResource:
    def __init__(self, url: str, headers: dict):
        self.connector = Connector(url=url, headers=headers)
        self.fieldnames=['number','name','birthday','city']
        
    def execute(self):
        liData: list = self.connector.execute()

        getData = GetData(liData=liData)
        listOfTerrs: list = getData.execute()

        saveToFile = SaveToFile(fieldnames=self.fieldnames)
        saveToFile.execute(list_of_dicts=listOfTerrs)


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
url = 'https://fedsfm.ru/documents/terrorists-catalog-portal-act'

getTerrs = GetTerroristFromFedResource(url=url, headers=headers)
getTerrs.execute()


# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
# response = requests.get('https://fedsfm.ru/documents/terrorists-catalog-portal-act', headers = headers, verify = False)
# divs = parsed_information.find_all('div', 'panel-group')
# part_of_pars = divs[2].find_all('li')
# # print(part_of_pars)

# with open('terrorists.csv', '+w', newline='') as csvfile:
#     fieldnames = ['number','name','birthday','city']
#     writer = csv.DictWriter(csvfile, delimiter = ',', fieldnames = fieldnames)
#     writer.writeheader()
#     for element in part_of_pars:
#         data = (element.text).split(',')
#         number = data[0].split('.')[0]
#         name = data[0].split('.')[1]
#         birthday = data[1]
#         try:
#             city = data[2]
#         except:
#             city = ''
#         slovar = {'number': number, 'name': name, 'birthday': birthday, 'city': city}
#         writer.writerow(slovar)

        # test = {'number': number, 'name': name, 'birthday': birthday, 'city': city }

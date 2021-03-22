import csv

class CsvReader:

    def __init__(self):
        pass

    def loadData(self, filepath):
        data = []
        with open(filepath) as text_data:
            csv_data = csv.DictReader(text_data, delimiter=',')
            for row in csv_data:
                data.append(row)
        return data

    def return_data_as_objects(self, class_name):
        objects = []
        for row in self.data:
            objects.append(ClassFactory(class_name, row))
        return objects
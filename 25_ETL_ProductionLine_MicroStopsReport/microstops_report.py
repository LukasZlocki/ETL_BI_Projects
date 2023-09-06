import os
import csv

class MicrostopsReport:
    '''
    '''
    _csv_dataset = []


    def load_dataset_from_csv_file(self,path, file_name):
        """
        load raw report dataset from csv file and store it in __raw_dataset
        : param path: path to file with csv dataset
        : param file_name: name of file with raw csv datasset
        : type report: array
        : type source_path: pathlib object Path
        : type output_file: string
        """
        # Open the CSV file in read mode
        with open(os.path.join(path, file_name), 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            for element in csv_reader:
                self._csv_dataset.append(element)
    
    def print_dataset(self, dataset, rows_to_print):
        """
        Printing given dataset
        : param dataset: report dataset in csv format
        : param rows_to_print: quantity of raws to be printed. 0 - all raws
        : type dataset: array
        : type rows_to_print: integer
        """
        counter = 0
        for element in dataset:
            print(element)
            counter = counter +1
            if counter == rows_to_print:
                break
        print("")

    def print_given_column_in_dataset(self, dataset, column_to_print, rows_to_print):
        """
        Printing given column in dataset
        : param dataset: report dataset in csv format
        : param column_to_print: number of column to be printed
        : param rows_to_print: quantity of raws to be printed. 0 - all raws
        : type dataset: array
        : type rows_to_print: integer
        """
        counter = 0
        for element in dataset:
            print(element[column_to_print])
            counter = counter +1
            if counter == rows_to_print:
                break
        print("")
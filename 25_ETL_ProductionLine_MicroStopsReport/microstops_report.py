import os
import csv
from time_resolver import TimeResolver

class MicrostopsReport:

    _csv_dataset = []

    def resolve_time_description_and_transformstrings_to_time_in_minutes(self, column_with_time_to_resolve):
        '''
        Resolve time in [minute] from dataset with string of words and numbers
        : param column_with_time_to_resolve: column number were time is given as word or nmbe ras a string to resolve
        : type column_with_time_to_resolve: integer
        '''
        tr = TimeResolver()
        count = 0
        for element in self._csv_dataset:
            if count == 0:
                count = count + 1
                continue
            resolved_time = tr.resolve_string_and_return_time_in_minutes(element[column_with_time_to_resolve])
            element[column_with_time_to_resolve] = resolved_time
            print(resolved_time)
        #tr.resolve_string_and_return_time_in_minutes

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
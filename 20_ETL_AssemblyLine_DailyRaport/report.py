import csv
import os

class Report:
    def __init__(self):
        self.__raw_dataset = []
    
    def load_raw_dataset_from_csv_file(self,path, file_name):
        """
        load raw report dataset from csv file and store it in __raw_dataset
        : param path: path to file with csv dataset
        : param file_name: name of file with raw csv datasset
        : type report: array
        : type source_path: pathlib object Path
        : type output_file: string
        """
        # Open the CSV file in read mode
        with open(os.path.join(path, file_name), 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for element in csv_reader:
                self.__raw_dataset.append(element)
    
    def save_transformed_report_to_csv_file(self, report, output_path, output_file):
        """
        Save report to csv file
        : param report: report dataset
        : param output_path: output path name 
        : param output_file: output file name for report csv data
        : type report: array
        : type source_path: pathlib object Path
        : type output_file: string
        """
    
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

    def get_raw_dataset(self):
        """
        Return raw dataset
        : return: raw csv dataset
        : rtype: array
        """
        return self.__raw_dataset
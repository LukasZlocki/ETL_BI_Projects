import csv
import os
import data_transformator as data_transformator

class Report:
    def __init__(self):
        self.__raw_dataset = []
        self.__base_dataset = []

    def transform_raw_dataset_to_base_dataset(self, raw_dataset):
        dt = data_transformator.DataTransformator()
        self.__base_dataset = dt.transform_date_in_dataset(raw_dataset)

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
        with open(os.path.join(output_path, output_file), mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            for row in report:
                csv_writer.writerow(row)
    
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

    def get_raw_dataset(self):
        """
        Return raw dataset
        : return: raw csv dataset
        : rtype: array
        """
        return self.__raw_dataset

    # Calculate oee for given data. Return value raunded to two digits
    def _calculate_oee(self, planned_output, real_output):
        percentage_result = round(real_output*100/planned_output,2)
        return percentage_result
    
    # Extract dates from given raport. Return list of dates
    def _extract_all_dates_from_raport(self, dataset):
        """
        Extracting dates from given dataset
        : param dataset: dataset in csv format
        : type dataset: array
        : return: dates list
        : rtype: array
        """
        dates = []
        for element in dataset:
            if(element[1] == "Date"): # Removing "Date" description in column
                continue
            #date_without_time = super()._remove_not_needed_elements_from_date(element[1])
            if element[1] not in dates:
                dates.append(element[1])
        return dates
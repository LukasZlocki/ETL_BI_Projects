# Extract data from excel files and save it to csv format 

import os
import pandas as pd
import csv

class DataExtractor:
    def __init__(self):
        self.__dataset = []

    def extract_hourly_reports_data_from_excel(self, source_path, file_name):
        """
        Extract hourly reports data from excel file
        : param source_path: source path name 
        : param file_name: file name with source data
        : type source_path: pathlib object Path
        : type file_name: string
        """
        self.__dataset = self.__extract_jedox_hourly_targets_sheet(os.path.join(source_path, file_name))

    def print_extracted_data(self):
        print(self.__dataset)

    def save_extracted_data_to_csv_file(self, output_path, output_file):
        """
        Save extracted data to csv file
        : param output_path: source path name 
        : param output_file: output file name for extracted csv data
        : type source_path: pathlib object Path
        : type output_file: string
        """
        self.__dataset.to_csv(os.path.join(output_path, output_file))

    # READ pure data of hourly reports from jedox file
    def __extract_jedox_hourly_targets_sheet(self, path):
        """
        Extract hourly reports data from excel file
        : param path: source path name 
        : type source_path: os lib object
        : return: formated dataset of haurly targets 
        : rtype: pandas library dataset
        """
        column_numbers = [3, 1, 4, 5]
        xls = pd.ExcelFile(path)
        dataset = pd.read_excel(
            xls, 'Sheet3', 
            usecols="A,B,E,F", 
            names=['Date', 'Hours', 'Planned', 'Output'
            ])
        return dataset
# Extracting data from excel file

import pandas as pd
from pathlib import Path
import os


class DataExtractor:

    _extracted_dataset = []

    # Extract apecific data from excel file  
    def extract_micro_stops_data_from_excel_sheet(self, source_path, file_name):
        """
        Extract micro stops data from excel file
        : param source_path: source path name 
        : param file_name: file name with source data
        : type source_path: pathlib object Path
        : type file_name: string
        """
        self._extracted_dataset = self._extract_microstops_data(os.path.join(source_path, file_name))

    def print_extracted_dataset(self):
        print(self._extracted_dataset)

    def save_extracted_data_to_csv_file(self, output_path, output_file):
        """
        Save extracted data to csv file
        : param output_path: source path name 
        : param output_file: output file name for extracted csv data
        : type source_path: pathlib object Path
        : type output_file: string
        """
        self._extracted_dataset.to_csv(os.path.join(output_path, output_file))

    # READ pure data of hourly reports from jedox file
    def _extract_microstops_data(self, path):
        """
        Extract micro stops data from excel file
        : param path: source path name 
        : type source_path: os lib object
        : return: formated dataset of haurly targets 
        : rtype: pandas library dataset
        """
        xls = pd.ExcelFile(path)
        dataset = pd.read_excel(
            xls, 'Sheet6', 
            usecols="A,B, C, D, F", 
            names=['Date', 'MainFailure', 'AssemblyFailure', 'FailureDescr', 'TimeLost'
            ])
        return dataset



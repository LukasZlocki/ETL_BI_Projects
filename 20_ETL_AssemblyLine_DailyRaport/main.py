# Script to automate data collection for micro stops on production line

from pathlib import Path

import data_extractor as de
import report

SOURCE_PATH = Path("./src/")
OUTPUT_PATH = Path("./out/")
SOURCE_FILE = "jedox_new.xlsm"

def main():
    # EXTRACT dataset of hourly target raports from excel file and store it to csv file
    data_extractor = de.DataExtractor()
    data_extractor.extract_hourly_reports_data_from_excel(SOURCE_PATH, SOURCE_FILE)
    data_extractor.print_extracted_data()
    data_extractor.save_extracted_data_to_csv_file(OUTPUT_PATH, "raw_raports.csv")

    # LOAD data from raw csv file and print data
    rep = report.Report()
    rep.load_raw_dataset_from_csv_file(OUTPUT_PATH, "raw_raports.csv")
    row_dataset = rep.get_raw_dataset()
    rep.print_dataset(row_dataset, 5)

    # ToDo: TRANSFORM data to daily reports
    



    # ToDo: Calculate OEE
    # ToDo: Create final daily report
    # ToDo: Save daily reports to csv file

    # ToDo: TRANSFORM data to shift reports
    # ToDo: Calculate OEE for each shift
    # ToDo: Create final shift reports
    # ToDo: Save shift reports to csv file



if __name__ == '__main__':
    main() 
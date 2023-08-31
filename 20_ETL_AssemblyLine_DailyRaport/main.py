# Script to automate data collection for micro stops on production line

from pathlib import Path

import data_extractor as de
import report
import daily_report as dr
import data_transformator as dt
import shift_report as sr

SOURCE_PATH = Path("./src/")
OUTPUT_PATH = Path("./out/")
SOURCE_FILE = "jedox_new.xlsm"

def main():
    # EXTRACT dataset of hourly target raports from excel file and store it to csv file
    data_extractor = de.DataExtractor()
    data_extractor.extract_hourly_reports_data_from_excel(SOURCE_PATH, SOURCE_FILE)
    print("Extracted data ***")
    data_extractor.print_extracted_data()
    data_extractor.save_extracted_data_to_csv_file(OUTPUT_PATH, "raw_raports.csv")

    # LOAD data from raw csv file and print data
    rep = report.Report()
    rep.load_raw_dataset_from_csv_file(OUTPUT_PATH, "raw_raports.csv")
    row_dataset = rep.get_raw_dataset()
    print("Raw dataset ***")
    rep.print_dataset(row_dataset, 5)

    # TRANSFORM raw dataset and modify data(removing time stamp) in each row
    data_transformator = dt.DataTransformator()
    transformed_row_dataset = data_transformator.transform_date_in_dataset(row_dataset) 
    print("Transformed data - base_dataset ***")
    rep.print_dataset(transformed_row_dataset, 10)
    # Save transformed dataset (with date without time) to csv file 
    rep.save_transformed_report_to_csv_file(transformed_row_dataset, OUTPUT_PATH, "raw_dataset_clear_date.csv")

    # TRANSFORM data to daily reports
    rep_daily = dr.DailyReport()
    rep_daily.load_raw_dataset_from_csv_file("./out/", "raw_dataset_clear_date.csv")
    data_set = rep_daily.get_raw_dataset()
    print("dataset to convert to daily report ***")
    rep_daily.print_dataset(data_set, 8)
    rep_daily.transform_dataset_to_daily_reports(data_set)
    daily_reports = rep_daily.get_daily_reports()
    print("Printing 25 daily reports:")
    rep_daily.print_dataset(daily_reports,25)
    rep.save_transformed_report_to_csv_file(daily_reports, OUTPUT_PATH, "daily_reports.csv")

    # TRANSFORM dataset to shift reports
    rep_shift = sr.ShiftReport()
    rep_shift.load_raw_dataset_from_csv_file("./out/", "raw_dataset_clear_date.csv")
    data_set_ = rep_shift.get_raw_dataset()
    print("dataset to convert to shift report - eight samples***")
    rep_shift.print_dataset(data_set, 8)
    # Create final shift reports
    rep_shift.transform_dataset_to_shift_reports(data_set)
    shift_reports = rep_shift.get_shift_reports()
    print("Printing 26 shift reports:")
    rep_shift.print_dataset(shift_reports, 26)
    # Save shift reports to csv file
    rep_shift.save_transformed_report_to_csv_file(shift_reports, "./out/", "shift_reports.csv" )
   
if __name__ == '__main__':
    main() 
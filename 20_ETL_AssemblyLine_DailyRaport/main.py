# Script to automate data collection for micro stops on production line

from pathlib import Path

import data_extractor as de
import report
import daily_report as dr
import data_transformator as dt

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

    # Transform raw dataset and modify data(removing time stamp) in each row
    data_transformator = dt.DataTransformator()
    transformed_row_dataset = data_transformator.transform_date_in_dataset(row_dataset) 
    print("Transformed data - base_dataset ***")
    rep.print_dataset(transformed_row_dataset, 10)

    ## to delete (?)
    #rep._transform_date_to_date_without_time_in_dataset(row_dataset)
    #print("Printing 25 base dataset elements:")
    #base_dataset = #.get_base_dataset()
    # rep.print_dataset(base_dataset, 25)


    # ToDo: TRANSFORM data to daily reports
    rep_daily = dr.DailyReport()
    rep_daily.load_raw_dataset_from_csv_file("./out/", "raw_raports.csv")
    data_set_raw = rep_daily.get_raw_dataset()
    rep_daily.print_dataset(data_set_raw, 5)
    rep_daily.transform_dataset_to_daily_reports(data_set_raw)
    daily_reports = rep_daily.get_calculated_daily_reports()
    print("Printing 25 daily reports:")
    rep_daily.print_dataset(daily_reports,25)

    # ToDo: Calculate OEE
    # ToDo: Create final daily report
    # ToDo: Save daily reports to csv file

    # ToDo: TRANSFORM data to shift reports
    # ToDo: Calculate OEE for each shift
    # ToDo: Create final shift reports
    # ToDo: Save shift reports to csv file



if __name__ == '__main__':
    main() 
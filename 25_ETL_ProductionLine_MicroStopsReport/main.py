# This script Extract data from operators production data sheets
# Extracted data are saved to csv data file
# Transformation are being done in order to
# A. recalculating time of microstops and transfer it to minutes.
# A. standardize operators descriptions of micro stops and transformig the data to standardized failures data tree

from pathlib import Path
import data_extract as de
import microstops_report as ms
import time_resolver as tr

SOURCE_PATH = Path("./src/")
OUTPUT_PATH = Path("./out/")
SOURCE_FILE = "jedox_new.xlsm"
RAW_CSV_DATA_MICROSTOPS = ("raw_micro_stops.csv")

def main():
    '''
    '''
# Step: Load data from excel
data_extractor = de.DataExtractor ()
data_extractor.extract_micro_stops_data_from_excel_sheet(SOURCE_PATH, SOURCE_FILE)
data_extractor.print_extracted_dataset()
# Steps ToDo: Save data to csv file
data_extractor.save_extracted_data_to_csv_file(OUTPUT_PATH, RAW_CSV_DATA_MICROSTOPS)
# Steps ToDo: Load data from csv file 
ms_report = ms.MicrostopsReport()
ms_report.load_dataset_from_csv_file(OUTPUT_PATH, RAW_CSV_DATA_MICROSTOPS)
print("Printing 10 dataset from raw csv file:")
ms_report.print_dataset(ms_report._csv_dataset, 10)

# * Micro stops time resolving *
# Steps ToDo: Create dictionary to cover all micro stops times (like 1h -> 60 [minutes], like 1h 30minut -> 90 [minutes] )
# Create class TimeResolver with all algorithms to transfer each description into time in [minutes]
print("Printing 10 dataset from raw csv and only column with waste time description")
ms_report.print_given_column_in_dataset(ms_report._csv_dataset, 5, 5)

#''' Write a test methods to cover testing of the code and different scenerios
# resolving time from string - TESTS ! 
time_resolver = tr.TimeResolver()
string_array = time_resolver._extracting_words_and_numbers_from_string("1h 24 min")
print(string_array)
string_array = time_resolver._extracting_words_and_numbers_from_string("10 m")
print(string_array)
string_array = time_resolver._extracting_words_and_numbers_from_string("26.")
print(string_array)
string_array = time_resolver._extracting_words_and_numbers_from_string("10m")
print(string_array)
string_array = time_resolver._extracting_words_and_numbers_from_string("")
print(string_array)
string_array = time_resolver._extracting_words_and_numbers_from_string(" ")
print(string_array)
string_array = time_resolver._extracting_words_and_numbers_from_string("3 godziny")
print(string_array)

# Test 1: "1 godz. 30 m.""
string_array = time_resolver._extracting_words_and_numbers_from_string("1 godz. 30 m.")
print(string_array)
print("Testing retriving multipilcator and number. Test Variant: 1 godz. 30 m. ")
resolved_time = time_resolver._extracting_time_from_array_of_words_and_numbers(string_array)
for element in resolved_time:
    print(element)
time = time_resolver._resolve_time_form_final_array(resolved_time)
print(time)

# Test 1\2: "5""   !!!! FIX THIS IN  CODE ! 
string_array = time_resolver._extracting_words_and_numbers_from_string("5")
print(string_array)
print("Testing retriving multipilcator and number. Test Variant: 5")
resolved_time = time_resolver._extracting_time_from_array_of_words_and_numbers(string_array)
for element in resolved_time:
    print(element)
time = time_resolver._resolve_time_form_final_array(resolved_time)
print(time)
#'''


# Steps ToDo: Create method pointing that script is not able to resolve micro stop given b operator . This operation will be done manualy and description will be added to dictionary manualy
# Steps TodO: Save data to output csv file
# * Micro stops root cause standardization *
# Steps ToDo: steps need to be staed here
# Steps ToDo: steps need to be stated here


if __name__ == '__main__':
    main() 
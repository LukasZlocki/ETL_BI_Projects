# This script Extract data from operators production data sheets
# Extracted data are saved to csv data file
# Transformation are being done in order to
# A. recalculating time of microstops and transfer it to minutes.
# A. standardize operators descriptions of micro stops and transformig the data to standardized failures data tree

from pathlib import Path
import data_extract as de

SOURCE_PATH = Path("./src/")
OUTPUT_PATH = Path("./out/")
SOURCE_FILE = "jedox_new.xlsm"

def main():
    '''
    '''
# Step: Load data from excel
data_extractor = de.DataExtractor ()
data_extractor.extract_micro_stops_data_from_excel_sheet(SOURCE_PATH, SOURCE_FILE)
data_extractor.print_extracted_dataset()
# Steps ToDo: Save data to csv file
data_extractor.save_extracted_data_to_csv_file(OUTPUT_PATH, "raw_micro_stops.csv")
# Steps ToDo: Load data from csv file 
# * Micro stops time resolving *
# Steps ToDo: Load data from csv file
# Steps ToDo: Create dictionary to cover all micro stops times (like 1h -> 60 [minutes], like 1h 30minut -> 90 [minutes] )
# Steps ToDo: Create method pointing that script is not able to resolve micro stop given b operator . This operation will be done manualy and description will be added to dictionary manualy
# Steps TodO: Save data to output csv file
# * Micro stops root cause standardization *
# Steps ToDo: steps need to be staed here
# Steps ToDo: steps need to be stated here


if __name__ == '__main__':
    main() 
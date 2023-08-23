# Goal of script is to gather data of CostCenters and related Work Center and id of sets of machines (DW)

# Scripting plan
# [done] Read data from separate file (controling and maintanance)
# exclude needed data basis on cost center number
# create new dataset according to class etl_costcenters
# add object of etl_costcenter class to table
# write array of the objects to csv file

import database as database
import csv
import pandas as pd

def read_data_from_file(filename):
    """
    Read dataset from csv file using csv library
    : param filename: name of the csv file with data
    : type dataset: string
    : return: list of data set
    : rtype: string
    """
    dataset = []
    with open(filename, 'r', encoding='iso-8859-1') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            dataset.append(row)
    #csv_file.close()
    return dataset

def print_dataset(dataset, max_print_rows):
    """
    Printing dataset on screen
    : param dataset: A csv list
    : type dataset: list
    : param max_print_rows: max rows to print, 0 - printing all rows
    : type max_print_rows: integer
    """
    counter = 0
    for row in dataset:
        # Process the data in each row
        print(row)  # This will print each
        counter = counter + 1
        if counter == max_print_rows:
            break
    print("*********************** END OF DATA ****************************")

# Creation of cost center list basis on maintanance dataset
def create_costcenter_list(maintanance_datset):
    """
    Extract cost centers(row[2]) from given dataset
    : param maintanance_dataset: A csv list
    : type dataset: string
    : return: list of cost centers
    : rtype: string
    """
    costcenter_list = []
    for element in maintanance_datset:
        if element[2] not in costcenter_list:
            costcenter_list.append(element[2])
    return costcenter_list

def switch_column_in_dataset (dataset,column_to_switch, switch_with_column):
    """
    Switching columns in dataset
    : param dataset: A csv list
    : param column_to_switch: column number to switch
    : param switch_with_column: column number to switch with column to switch  
    : type dataset: string
    : type column_to_switch: integer
    : type switch_with_column: integer
    : return: switched list of data set
    : rtype: string
    """
    switched_dataset = []
    for element in dataset:
        temp_to_switch = element[column_to_switch]
        temp_switch_with = element[switch_with_column]
        element[column_to_switch] = temp_switch_with
        element[switch_with_column] = temp_to_switch
        switched_dataset.append(element)
    return switched_dataset

def save_dataset_to_csv_file(dataset, csv_file_name):
    """
    save dataset to csv file
    : param dataset: dataset 
    : type dataset1: string
    """
    with open(csv_file_name, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(dataset)

def main():

    # Read data from csv files
    maintanance_dataset = read_data_from_file("db_Maintanance.csv")
    controlling_dataset = read_data_from_file("db_Controlling.csv") 
    print_dataset(maintanance_dataset,5)
    print_dataset(controlling_dataset,5)

    # Extracting list of cost centers
    cost_center_list = create_costcenter_list(maintanance_dataset)
    print_dataset(cost_center_list,0)

    # Switching columns to have cost centers as a first column in each dataset
    switched_controlling = switch_column_in_dataset(controlling_dataset, 1,0)
    switched_maintanance = switch_column_in_dataset(maintanance_dataset, 2,0)
    print("Columns switched:")
    print_dataset(switched_controlling,5)
    print_dataset(switched_maintanance,5)

    # Save dataset to csv file
    save_dataset_to_csv_file(switched_controlling, 'controlling_output.csv')
    save_dataset_to_csv_file(switched_maintanance, 'maintanance_output.csv')

if __name__ == "__main__":
    main()
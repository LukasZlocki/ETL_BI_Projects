# Transform data to user needs

from datetime import datetime

class DataTransformator:
        
    def transform_date_in_dataset(self, dataset):
        transformed_dataset_with_date_without_time = self._transform_date_to_date_without_time_in_dataset(dataset)
        return transformed_dataset_with_date_without_time
    
    def _transform_date_to_date_without_time_in_dataset(self, dataset):
        """
        Transform date in dataset to date without time(hour, minutes, seconds)
        : param dataset: report dataset in csv format
        : param rows_to_print: quantity of raws to be printed. 0 - all raws
        : type dataset: array
        : type rows_to_print: integer
        """
        transformed_dataset = []
        for row in dataset:
            date = row[1]
            if(date == "Date"):
                continue
            date_without_time = self._remove_not_needed_elements_from_date(date)
            row[1] = date_without_time
            transformed_dataset.append(row)
        return transformed_dataset

    def _remove_not_needed_elements_from_date(self, date):
        date_to_date_time = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        #date_without_time = date_to_date_time.date()
        pure_date = date_to_date_time.strftime("%Y-%m-%d")
        return pure_date
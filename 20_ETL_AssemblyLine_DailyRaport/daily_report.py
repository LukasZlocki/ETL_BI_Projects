import report

class DailyReport(report.Report):
    
    # List of dates in dataset
    __dates_list = []
    
    # Daily reports 
    daily_reports_dataset = []

    def transform_dataset_to_daily_reports(self):
        self.__dates_list = self.__extract_all_dates_from_raport(self.__raw_dataset)
        self.daily_reports_dataset = self.__calculate_raport_for_given_days(self.__dates_list, self.__raw_dataset)

    # Extract dates from given raport. Return list of dates
    def __extract_all_dates_from_raport(self, dataset):
        """
        Extracting dates from given dataset
        : param dataset: dataset in csv format
        : type dataset: array
        : return: dates list
        : rtype: array
        """
        dates = []
        for element in dataset:
            if element[1] not in dates:
                dates.append(element[1])
        dates.remove('Date')
        return dates

    # Calculate raports for given list of dates. Return list of daily raports
    def __calculate_raport_for_given_days(self, dates_list):
        """
        Calculate daily reports base on raw dataset and list of dates 
        : param dates_lit: list of dates
        : type dataset: array
        : return: list of daily reports
        : rtype: array
        """
        daily_reports = []
        for day in dates_list:
            daily_raport = self.__calculate_raport_for_this_day(day)
            daily_reports.append(daily_raport)
        return daily_reports
    
    # Calcule report for one whole day. Return report table
    def __calculate_raport_for_this_day(self, day):
        """
        Calculate daily report for given day
        : param day: date
        : type dataset: string
        : return: daily report
        : rtype: array of strings
        """
        daily_output_real = 0
        daily_planned_output = 0
        for element in self.__dataset:
            if element[1]== day:
                daily_planned_output = daily_planned_output + int(element[3])
                daily_output_real = daily_output_real + int(element[4])
        oee = self.__calculate_oee(daily_planned_output, daily_output_real)
        day_report = [day, daily_planned_output, daily_output_real, oee]
        return day_report
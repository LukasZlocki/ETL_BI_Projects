import report

class ShiftReport(report.Report):
    def __init__(self):
        super().__init__()  # Call the constructor of the base class
        # Shift time frames
        self.__shift_I = ["0600-0700", "0700-0800", "0800-0900", "0900-1000", "1000-1100", "1100-1200", "1200-1300", "1300-1400"]
        self.__shift_II = ["1400-1500", "1500-1600", "1600-1700", "1700-1800", "1800-1900", "1900-2000", "2000-2100", "2100-2200"]
        self.__shift_III = ["2200-2300", "2300-0000", "0000-0100", "0100-0200", "0200-0300", "0300-0400", "0400-0500", "0500-0600"]

    # Shift reports
    _shift_reports_dataset = []

    def transform_dataset_to_shift_reports(self, dataset):
        """
        ToDo: Write code here
        """
        # Extracting dates from dataset
        dates = super()._extract_all_dates_from_raport(dataset)
        self._calculate_shift_raports_for_given_list_of_dates(dates, dataset)

    def get_shift_reports(self):
        return self._shift_reports_dataset

    # Calculate shit raports base on list of dates
    def _calculate_shift_raports_for_given_list_of_dates(self, list_of_dates, dataset):
        """
        calculate reports for each shift (I, II, III) basis on list of dates and given dataset
        : param list_of_dates: list with all dates to calculate shift reports
        : param dataset: dataset with production data
        : type list_of_dates: array of string
        : type dataset: array of string
        """
        for date in list_of_dates:
            shift_1_rep =  self._calculate_shifts_raport_for_given_day_and_shift(date, 1, dataset)
            shift_2_rep =  self._calculate_shifts_raport_for_given_day_and_shift(date, 2, dataset)
            shift_3_rep =  self._calculate_shifts_raport_for_given_day_and_shift(date, 3, dataset)
            # add only if raport exist and exclude empty reports
            if shift_1_rep:
                self._shift_reports_dataset.append(shift_1_rep)
            if shift_2_rep:
                self._shift_reports_dataset.append(shift_2_rep)
            if shift_3_rep:
                self._shift_reports_dataset.append(shift_3_rep)

    # Extract shifts in date given
    # Format [day, shift_number, output_planned, output real, oee]
    def _calculate_shifts_raport_for_given_day_and_shift(self, day, shift_number, dataset):
        shift_hourly_target = []
        # invoke def to calculate hourly targets for needed shift
        if shift_number == 1:
            shift_hourly_target = self._extract_shift_hourly_targets_based_on_shift_hours_set(day ,dataset, self.__shift_I,1)
        if shift_number == 2:
            shift_hourly_target = self._extract_shift_hourly_targets_based_on_shift_hours_set(day, dataset, self.__shift_II,2)
        if shift_number == 3:
            shift_hourly_target = self._extract_shift_hourly_targets_based_on_shift_hours_set(day, dataset, self.__shift_III,3)
        return shift_hourly_target
 
    # Extract report for given shift and given day
    # Output format [date, shift_number, output_planned, output_real. oee]
    def _extract_shift_hourly_targets_based_on_shift_hours_set(self, day, dataset, shift_hours_seter, shift_number):
        shift_raport = []
        shift_output_real = 0
        shift_planned_output = 0
        oee = 0
        for element in dataset:
            if element[1]== day:
                for timeframe in shift_hours_seter:
                    if element[2] == timeframe:
                        shift_planned_output = shift_planned_output + int(element[3])
                        shift_output_real = shift_output_real + int(element[4])
        if (shift_planned_output > 0):
            oee = super()._calculate_oee(shift_planned_output, shift_output_real)
            shift_raport.append([day, shift_number, shift_planned_output , shift_output_real, oee])
            shift_output_real = 0
            shift_planned_output = 0           
        return shift_raport
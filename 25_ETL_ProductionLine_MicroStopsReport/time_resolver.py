# This class resolve production operators' wasted time description into standard unit time in minutes
# ex: 
# 5h -> resolved to -> 300 minutes
# 10. -> resolved to -> 10 minutes
# 1h 40 min -> resolved to -> 100 minutes

class TimeResolver:
    '''
    '''
    # Code algorithm to transform wasted time description like 1m / 1 m / 1godz. / 1 god / 1 godz 30 min
    # try to avoid using dictionary as solution. Reason: too much afford to collect all possible errors in time description.
    _multiplicator_dict = {
        "h": 60,
        " h": 60,
        "m": 1,
        " m": 1,
        "god.": 60,
        " god.": 60,
        "god": 60,
        " god": 60,
        ".": 1,
        "godz.": 60,
        " godz.": 60,
        "godziny": 60,
        " godziny": 60,
        "godz": 60,
        " godz": 60,
        "MIN": 1,
        " MIN": 1,
        "min": 1,
        " min": 1,
        "m.": 1,
    }
    
    
    def resolve_string_and_return_time_in_minutes(self, string_to_resolve):
        # extracting words and numbers from string
        array_of_words_and_numbers = self._extracting_words_and_numbers_from_string(self, string_to_resolve)
        resolved_time_array = self._extracting_time_from_array_of_words_and_numbers(array_of_words_and_numbers)
        resolved_time = self._resolve_time_from_final_array(resolved_time_array)
        return resolved_time

    def _resolve_time_from_final_array(self, resolved_time_array):
        time = 0
        for element in resolved_time_array:
                time = time + element[0] * element[1]
        return time

    def _extracting_time_from_array_of_words_and_numbers(self, array):
        """
        Extracting time from passed array of words and numbers
        : param array: words and numbers stored in array to resolve and change to time 
        : type array: array of strings
        : return: time in [minutes]
        : rtype: string
        """
        isNumber = True # resolving timr from number
        calculation_array = []
        _number = 0
        _multiplicator = 0
        for element in array:
            if (isNumber):
                _number = int(element)
                isNumber = False # switch to look for number from word
            else:
                multiplicator_as_string = self._retrive_multiplicator_from_word(element)
                _multiplicator = int(multiplicator_as_string) # Convert word to proper multipilcator (ex word: 1h = 60 min)
                isNumber = True
                calculation_array.append([_number, _multiplicator])
                _number = 0
                _multiplicator = 0

        return calculation_array

    def _retrive_multiplicator_from_word(self, word):
        try:
            multiplicator = self._multiplicator_dict[word] # taking data from multiplicator dictionary
            return multiplicator
        except KeyError:
            return "Not in dictionary"



    def _extracting_words_and_numbers_from_string(self, time_to_resolve_string):
        """
        Extracting words and numbers from passed string
        : param time_to_resolve_string: string that consist words and numbers 
        : type time_to_resolve_string: string
        : type source_path: pathlib object Path
        : type output_file: string
        : return: extracted words and numbers from given string
        : rtype: array
        """
        # ex:
        # input: "1h 24min"
        # output: [1, h, 24, min] <- new algorithm will be created to resolve this array and convert to minutes
        is_digit_mode = True
        is_word_mode = False
        string_array = []
        temporary_string = ""
        for char in time_to_resolve_string:
            if ((char.isdigit() == True) & (is_digit_mode == True)): # retriving number from string mode
                temporary_string = temporary_string + char
                continue
            elif((char.isdigit() == False) & (is_word_mode == True) & (ord(char) != 32)): # retriving word from string mode 
                temporary_string = temporary_string + char
                continue
            elif((char.isdigit() == False) & (is_digit_mode == True)  & (ord(char) != 32)): # This is first char in new word
                string_array.append(temporary_string)
                temporary_string = "" + char # reset temporary string and write first char of new word
                is_digit_mode = False
                is_word_mode = True
                continue
            elif((char.isdigit() == True) & (is_word_mode == True)): # This is first char of new number
                string_array.append(temporary_string)
                temporary_string = "" + char # reset temporary string and write first char of new number
                is_digit_mode = True
                is_word_mode = False
                continue
        string_array.append(temporary_string) # add last string
        if (len(string_array) == 1 and string_array[0] != ""): # if string have only one sign (like "1") then adding description "min"
            string_array.append("min")
        return string_array
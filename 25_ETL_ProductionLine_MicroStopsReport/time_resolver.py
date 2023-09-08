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
    resolving_dict = {
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
    }
    
    
    resolving_dict_old = {
        "1h": 60,
        "2h": 120,
        "3m": 3,
        "3 m": 3,
        "1m": 1,
        "1god.30": 90,
        "1god.30": 90,
        "1god.30": 90,
        "1god.30": 90,
        "1god.30": 90,
        "1god.30": 90,
        "1god.30": 90,
        "1god.30": 90,
        "1god.30": 90,
        "1god.30": 90,
    }

    def resolve_string_and_return_time_in_minutes(self, string_to_resolve):
        resolved_time = 0
        # extracting words and numbers from string
        array_of_words_and_numbers = self._extracting_words_and_numbers_from_string(self, string_to_resolve)
        return resolved_time

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
        return string_array
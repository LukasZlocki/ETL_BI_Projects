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

    def _resolve_this_string_to_separate_words_and_numbers(self, time_to_resolve_string):
        # Descr examples:  1god.30 , 8 godz , 1 godz. 18 min , 3 godz 47min
        # charakteristic of time description : number | time description | number | time description
        # step: check char by char retrvie number | next char is not a number - switch to looking for time description
        # step: check char by char retrvie time description | next char is number - switch to looking to retrive number
        # output: string divided to array of strings
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
            elif((char.isdigit() == False) & (is_word_mode == True)): # retriving word from string mode 
                temporary_string = temporary_string + char
                continue
            elif((char.isdigit() == False) & (is_digit_mode == True)): # This is first char in new word
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
        return string_array
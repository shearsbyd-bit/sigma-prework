import time
import datetime as dt

def input_formatter(raw_date):
    cleaned_date = raw_date.replace("/", " ").replace(":", " ").replace(";", " ").replace("-", " ")
    formatted_date = cleaned_date.split()
    formatted_date_list = [float(x) for x in formatted_date]
    return formatted_date_list

def date_comparer(formatted_date_list, formatted_current_date_list):

    if formatted_date_list[1] < formatted_current_date_list [1]:
        return formatted_current_date_list[0] - formatted_date_list[-1]
    elif formatted_date_list[1] > formatted_current_date_list [1]:
        return formatted_current_date_list[0] - formatted_date_list[-1] - 1
    else:
        if formatted_date_list[0] <= formatted_current_date_list[2]:
            return formatted_current_date_list[0] - formatted_date_list[-1]
        else:
            return formatted_current_date_list[0] - formatted_date_list[-1] - 1

if __name__ == "__main__":
    raw_date = input("Enter a date to figure out how long ago it was (dd-mm-yyyy): ")
    current_date = str(dt.date.today())
    formatted_date_list = input_formatter(raw_date)
    formatted_current_date_list = input_formatter(current_date)
    print(int(date_comparer(formatted_date_list, formatted_current_date_list)))
def formatting(user_input):

    cleaned = user_input.replace("[", "").replace("]", "")
    raw_items = cleaned.split(",")
    
    new_list = []
    for x in raw_items:
        x = x.strip()
        new_list.append(int(x))
    return new_list

def max_min(formatted_list):
    '''
    I could just use sorted(formatted_list) and take the first and last item but that seems against the spirit of this task.
    So instead I will use a basic sorting algorithm such as bubble sort (as it's the most simple).
    '''
    while True:
        swaps = 0
        for i in range(0,len(formatted_list)-1):
            if formatted_list[i] > formatted_list[i+1]:
                swaps += 1
                holding_variable = formatted_list[i]
                formatted_list[i] = formmatted_list[i+1]
                formatted_list[i+1] = holding_variable

        if swaps == 0: 
            break 

    min_max_list = []
    min_max_list.append(formatted_list[0])
    min_max_list.append(formatted_list[-1])
    
    return min_max_list

if __name__ == "__main__":
    user_input = input("Enter a list of numbers: ")
    formmatted_list = formatting(user_input) 
    print(max_min(formmatted_list))
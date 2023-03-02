# %%
#Create a function that returns with a subsest of a list.
#The subset's starting and ending indexes should be set as input parameters (the list aswell).
#return type: list
#function name must be: subset
#input parameters: input_list,start_index,end_index

# %%
def subset(input_list,start_index,end_index):
    return input_list[start_index:end_index+1]


# %%
#Create a function that returns every nth element of a list.
#return type: list
#function name must be: every_nth
#input parameters: input_list,step_size

# %%
def every_nth(input_list,step_size):
    return input_list[::step_size]


# %%
#Create a function that can decide whether a list contains unique values or not
#return type: bool
#function name must be: unique
#input parameters: input_list

# %%
def unique(input_list):
    return len(set(input_list)) == len(input_list)  #convert to set --> only unique items


# %%
#Create a function that can flatten a nested list ([[..],[..],..])
#return type: list
#fucntion name must be: flatten
#input parameters: input_list

# %%
def flatten(input_list):
    flat_list = [num for sublist in input_list for num in sublist]
    return flat_list


# %%
#Create a function that concatenates n lists
#return type: list
#function name must be: merge_lists
#input parameters: *args


# %%
def merge_lists(*args):
    concat_list = []
    for lst in args:
        concat_list += lst
    return concat_list


# %%
#Create a function that can reverse a list of tuples
#example [(1,2),...] => [(2,1),...]
#return type: list
#fucntion name must be: reverse_tuples
#input parameters: input_list

# %%
def reverse_tuples(input_list):
    """Reverses a list of tuples. Works for any length"""
    output_list = []
    for tpl in input_list:
        output_list.append(tuple(reversed(tpl)))
    return output_list

# %%
#Create a function that removes duplicates from a list
#return type: list
#fucntion name must be: remove_tuplicates
#input parameters: input_list

# %%
def remove_duplicates(input_list):
    return list(set(input_list))


# %%
#Create a function that transposes a nested list (matrix)
#return type: list
#function name must be: transpose
#input parameters: input_list

# %%
def transpose(input_list):
    """Transposes a nested list."""
    n_rows = len(input_list)
    n_cols = len(input_list[0]) #first row's length = cols
    output_list = []
    for j in range(n_cols):
        new_row = []
        for i in range(n_rows):
            new_row.append(input_list[i][j])
        output_list.append(new_row)
    return output_list

# %%
#Create a function that can split a nested list into chunks
#chunk size is given by parameter
#return type: list
#function name must be: split_into_chunks
#input parameters: input_list,chunk_size

# %%
def split_nested_list(nested_list, chunk_size):
    result = []
    for sublist in nested_list:
        sublist_chunks = [sublist[i:i+chunk_size] for i in range(0, len(sublist), chunk_size)]
        result.extend(sublist_chunks)
    return result

# %%
#Create a function that can merge n dictionaries
#return type: dictionary
#function name must be: merge_dicts
#input parameters: *dict

# %%
def merge_dicts(*dicts):
    merged_dict = {}
    for d in dicts:
        merged_dict.update(d)
    return merged_dict

# %%
#Create a function that receives a list of integers and sort them by parity
#and returns with a dictionary like this: {"even":[...],"odd":[...]}
#return type: dict
#function name must be: by_parity
#input parameters: input_list

# %%
def by_parity(input_list):
    even = []
    odd = []
    for num in input_list:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return {"even": sorted(even), "odd": sorted(odd)}

# %%
#Create a function that receives a dictionary like this: {"some_key":[1,2,3,4],"another_key":[1,2,3,4],....}
#and return a dictionary like this : {"some_key":mean_of_values,"another_key":mean_of_values,....}
#in short calculates the mean of the values key wise
#return type: dict
#function name must be: mean_key_value
#input parameters: input_dict

# %%
def mean_key_value(input_dict):
    output_dict = {}
    for key in input_dict:
        values = input_dict[key]
        mean_value = sum(values) / len(values)
        output_dict[key] = mean_value
    return output_dict


# %%
#If all the functions are created convert this notebook into a .py file and push to your repo



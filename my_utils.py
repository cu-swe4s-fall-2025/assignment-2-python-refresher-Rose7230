def get_column(file_name, query_column, query_value, result_column):
    """
    Gets values from a CSV file where one column matches a search value
    """
    results = []  # array to store matching values
    
    # open the file and read line by line
    with open(file_name, 'r') as file:
        for line in file:
            # split the line into an array
            row = line.strip().split(',')
            
            # check if the query column matches our search value
            if len(row) > query_column and row[query_column] == query_value:
                # add the result column value to our results
                if len(row) > result_column:
                    results.append(row[result_column])
    
    return results

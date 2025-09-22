def get_column(file_name, query_column, query_value, result_column=1):
    """
    Reads a CSV file and finds rows where one column matches what we're looking for
    
    AI Usage: Core implementation logic developed with Claude AI guidance for
    CSV parsing, file handling, and parameter structure
    """
    results = []  # list to save the values we find
    
    # read the file one line at a time
    with open(file_name, 'r') as file:
        for line in file:
            # break the line into pieces at each comma
            row = line.strip().split(',')
            
            # see if this row has what we're searching for
            if len(row) > query_column and row[query_column] == query_value:
                # grab the value we want from this row
                if len(row) > result_column:
                    results.append(row[result_column])
    
    return results

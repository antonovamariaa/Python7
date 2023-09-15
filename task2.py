def print_operation_table(operation, num_rows = 6, num_cols = 6):
    for x in range(1,num_cols+1):
        for y in range(1, num_rows+1):
            print (operation(x, y), end = " ")
        print("\n")



print_operation_table(lambda x, y: x * y)
    
    
    
    
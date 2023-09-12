def print_operation_table(operation, num_rows = 6, num_cols = 6):
    for i in range(1,num_cols+1):
        for j in range(1, num_rows+1):
            print (operation, end = " ")
        print("\n")



print_operation_table(lambda i, j: i * j)
    
    
    
    
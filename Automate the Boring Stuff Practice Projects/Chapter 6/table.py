#This function prints a transposed version of the tables passed to it, with each item right-justified

def print_table(table):
    col_widths = [0] * len(table)
    for i, each_list in enumerate(table):
        for item in each_list:
            if len(item) > col_widths[i]:
                col_widths[i] = len(item)
    for l in range(len(each_list)):
        for j in range(len(table)):    
            print(table[j][l].rjust(col_widths[j]), end=' ')
        print()

table_data = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

print_table(table_data)
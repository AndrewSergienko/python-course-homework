def get_start_middle_end_symbols(path, num_сhars):
    with open(path) as f:
        file_content = f.read()
        if len(file_content) < num_сhars * 3:
            print("The length of the file is less than you want to output")
            return
        middle_indexes = [len(file_content)//2-num_сhars//2, len(file_content)//2+(num_сhars - num_сhars//2 - 1)]
        print(f"start: {file_content[:num_сhars]}\n"
              f"middle: {file_content[middle_indexes[0]:middle_indexes[1]+1]}\n"
              f"end: {file_content[-num_сhars:]}")


get_start_middle_end_symbols('test.txt', 5)
print("=====================================")
get_start_middle_end_symbols('test2.txt', 3)
print("=====================================")
get_start_middle_end_symbols('test3.txt', 3)

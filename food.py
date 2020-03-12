
def open_and_append(text_file):
    try:
        with open(text_file, 'a') as ordering_food:
            ordering_food.append()
    except FileNotFoundError as error_three:
        print("ITEMS NOT ADDING TO LISTS")
        print(error_three)
        print(open_and_append())


# Reading The 'food.txt' File with 'r'.
def open_file_to_read(text_file):
    try:
        with open(text_file, 'r') as file:
            read_lines = file.readlines()
            for lines in read_lines:
                print(lines.title())

    except FileNotFoundError as Error_1:
        print("CHECK YOUR FILES!!!")
        print(Error_1)

    finally:
        print("SHUTS DOWN WHEN ERRORS ARE FOUND")

    print(open_file_to_read())
#
# def open_and_write(file):
#     try:
#         with open('food.txt', 'w') as write_order:
#             write_order.write()
#     except FileNotFoundError as Error_two:
#         print("NOT WRITING ITEMS")
#         print(Error_two)
#
#     finally:
#         print("SHUTS DOWN WHEN ERRORS ARE FOUND")
#
#     print(open_and_write())
#
#
#
#
# # user_input = ''
# # user_input = input("What would you like to have?\n")
#
# food_order_list = []


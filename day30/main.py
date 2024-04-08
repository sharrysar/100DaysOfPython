# try a line of code that might cause an error
# if file does not exist, a FileNotFoundError will raise

# try:
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
#     print(a_dict['key'])

# # do this if there is an error
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")

# # do this for KeyError
# except KeyError as error_msg:
#     print(f"The key {error_msg} does not exist.")

# # do this if there is no error
# else:
#     content = file.read()
#     print(content)

# # do this regardless of error or not
# finally:
#     raise TypeError("This is an error that I made up")

#---------------------------------------------------------#
fruits = eval(input())
# 🚨 Do not change the code above

# TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print(fruit + " pie")
    else:
        print(fruit + " pie")


# 🚨 Do not change the code below
make_pie(4)



# # We do not have to close this file as we used the "with" statement:
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)
#
# #Open file without needing to close:
# # We do not have to close this file as we used the "with" statement:
# with open("my_file.txt", mode="r") as file: #By default the mode is set to READ ONLY, you CANNOT WRITE
#     file.write("This is some randon text")
#
# # WRITE: replaces all prev text
# with open("my_file.txt", mode="w") as file: #mode set to WRITE
#     file.write("This is some randon text") #all text in my file got replaced by "This is some randon text"
#
# # ADD: adds to the prev set that was in the file
# with open("my_file.txt", mode="a") as file: #mode set to WRITE
#     file.write("\nThis is some randon text") #all text in my file got replaced by "This is some randon text"

# CREATE NEW FILE: if the name specified does not have a file in that name, it will CREATE one!
# with open("new_file.txt", mode="w") as file: #mode set to WRITE
#     file.write("\nThis is some randon text") #all text in my file got replaced by "This is some randon text"

# #Opening a file using file path
# with open("C:/Users/fatem/OneDrive/Desktop/my_file.txt") as file:
#     contents = file.read()
#     print(contents)
#
#Opening a file using file path
with open("C:/Users/fatem/OneDrive/Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)


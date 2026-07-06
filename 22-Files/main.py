# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# mode w  - rewrites the entire content
# with open("my_file.txt", mode="w") as file:
#     file.write("New written text")

with open("my_file.txt", mode="a") as file:
    file.write("\nNew written text using append mode")
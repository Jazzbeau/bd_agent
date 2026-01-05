from functions.get_file_content import get_file_content

print(
    "Result for current directory, valid file over limit:\n"
    + get_file_content("calculator", "lorem.txt")
)

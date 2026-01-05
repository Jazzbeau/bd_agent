from functions.get_file_content import get_file_content

print(
    "Result for current directory, valid file over character limit:\n"
    + get_file_content("calculator", "lorem.txt")
)

print(
    "Result for current directory, valid file:\n"
    + get_file_content("calculator", "main.py")
)

print(
    "Result for subdirectory, valid file:\n"
    + get_file_content("calculator", "pkg/calculator.py")
)

print(
    "Result for invalid directory (out of bounds):\n"
    + get_file_content("calculator", "/bin/cat")
)

print(
    "Result for invalid file (in bounds, does not exist):\n"
    + get_file_content("calculator", "pkg/does_not_exist.py")
)

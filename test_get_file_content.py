from functions.get_file_content import get_file_content

print("Result for lorem.txt:")
print(get_file_content("calculator", "lorem.txt"))
print()

print("Result for 'main' directory:")
print(get_file_content("calculator", "main.py"))
print()

print("Result for 'pkg/calculator.py' directory:")
print(get_file_content("calculator", "pkg/calculator.py"))
print()

print("Error #1:")
print(get_file_content("calculator", "/bin/cat"))
print()

print("Error #2:")
print(get_file_content("calculator", "pkg/does_not_exist.py"))
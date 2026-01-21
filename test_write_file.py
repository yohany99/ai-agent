from functions.write_file import write_file

print("Test #1:")
print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
print()

print("Test #2:")
print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
print()

print("Test #3:")
print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

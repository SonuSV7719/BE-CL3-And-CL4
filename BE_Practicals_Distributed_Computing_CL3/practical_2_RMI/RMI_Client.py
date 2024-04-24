import Pyro4

# Get the remote object proxy
string_concatenator = Pyro4.Proxy("PYRONAME:string.concatenator")

# Get input from the user
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# Call the remote method to concatenate strings
result = string_concatenator.concatenate(str1, str2)

# Display the result
print("Concatenated string:", result)

#MadLib.py
#Name: Tessa Horn
#Date: 08/25/25
#Assignment: Lab 1 MadLib

def main():
  print("Madlib")
  #Ask user for words
food1 = input("Enter a food: ")
adjective1 = input("Enter an adjective: ")
food2 = input("Enter a food: ")
adjective2 = input("Enter an adjective: ")
verb1 = input("Enter a verb: ")
time1 = input("Enter a time: ")
  #Print the story with the user supplied words.
print("I love eating "+food1+"!")
print("It is very "+adjective1+".")
print("However, I hate eating "+food2+"!")
print("It is so "+adjective2+".")
print("After eating, I "+verb1+".")
print("I do this for "+time1+".")
#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()

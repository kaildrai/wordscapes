#importing the library
import enchant
import itertools

def array_to_string(arr):
  return ''.join(arr)

#creating a dictionary
d = enchant.Dict("en_US")
checked = []

print("\n###\tWelcome to the anti-fun zone\t###")

while(1):
    scrambled = input("Enter the scrambled word: ")
    if(scrambled == 'q'): break
    print("Valid Words:")
    # do some logic to find all valid words in 'scrambled'
    for i in range(3,7):
        for word in itertools.permutations(scrambled,i):
            w = array_to_string(word)
            if (d.check(w) and w not in checked):
                print("  "+w)
                checked.append(w)

    checked.clear()

print('###\t\tExiting...\t\t###\n')


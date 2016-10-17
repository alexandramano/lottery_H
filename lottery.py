import random

print ("Welcome the Lottery numbers generator")
how_many = int(raw_input("Please enter how many random numbers would you like to have: "))

def main():
    random_no = random.sample(range(1,50), how_many)
    print (random_no)

main()


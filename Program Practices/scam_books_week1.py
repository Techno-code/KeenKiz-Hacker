# Input 13 digits, calculate by multiplying the digits alternatively by 1 and 3
# Then add the results
# If can multiply by 10, it is not a scam

def get_ints_from_string(str):
    int_list = []
    for c in str:
        c_int = int(c)
        int_list.append(c_int)
    return int_list

isbn = input("What is your ISBN? ")
isbn_numbers = get_ints_from_string(isbn)

sum = 0
for i in range(0, len(isbn_numbers)):
    if i % 2 == 0:
        sum += isbn_numbers[i]
    else:
        sum += isbn_numbers[i] * 3

if sum % 10 == 0:
    print("Yo legit book boi")
else:
    print("Oof fake book probably scam my guy")
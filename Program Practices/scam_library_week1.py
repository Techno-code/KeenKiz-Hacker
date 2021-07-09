

isbn_list = ["9781535607629", "9780224599051", "9787805752891", "9780508922424", "9780217323017", "9787089244371", "9787001254364", "9785237891875", "9784766597677", "9785272747259", "9781713085522", "9785567719022", "9785567719022", "9982173479036", "9782399105092"]

def get_ints_from_string(str):
    int_list = []
    for c in str:
        c_int = int(c)
        int_list.append(c_int)
    return int_list

def check_isbn(isbn):
    isbn_numbers = get_ints_from_string(isbn)

    sum = 0
    for i in range(0, len(isbn_numbers)):
        if i % 2 == 0:
            sum += isbn_numbers[i]
        else:
            sum += isbn_numbers[i] * 3

    if sum % 10 == 0:
        return True
    else:
        return False

valid_isbns = []
invalid_isbns = 0

for i in isbn_list:
    if check_isbn(i) == True:
        valid_isbns.append(i)
    else:
        invalid_isbns += 1

print(valid_isbns)
print(invalid_isbns)
# Detect if the last 4 digits of a phone number adds to 20
# If yes, scam call, if no, not scam call

def get_ints_from_string(str):
    int_list = []
    for c in str:
        c_int = int(c)
        int_list.append(c_int)
    return int_list

phone_num = input("Type the last 4 digits of the phone number: ")
phone_num_int = get_ints_from_string(phone_num)

sum = 0
for i in range(0, len(phone_num_int)):
	sum += phone_num_int[i]

if sum == 20:
    print("That is a scam call!")
else:
    print("It is not a scam call ;)")

input()
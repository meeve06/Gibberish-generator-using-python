#generates ut-tha-ga version of gibberish
def type_one(s):
    l=s.split()
    new_s=""
    for i in l:
        word=""
        word1=""
        last=i[len(i)-1]
        first=i[0]
        for j in range(1,len(i)-1):
            if(i[j] in ['a','e','i','o','u','A','E','I','O','U']):
                word+="th-tha-ga"+i[j]
            else:
                word+= i[j]
        if(first != last and len(i)!=1):
            word1=first+word+last
            new_s+= word1
        else:
            new_s+=first
    print(new_s)

def type_two(s):
    l=s.split()
    new_s=""
    for i in l:
        word=""
        word1=""
        last=i[len(i)-1]
        first=i[0]
        for j in range(1,len(i)-1):
            if(i[j] in ['a','e','i','o','u','A','E','I','O','U']):
                word+="id-ig"+i[j]
            else:
                word+= i[j]
        if(first != last and len(i)!=1):
            word1=first+word+last
            new_s+= word1
        else:
            new_s+=first
    print(new_s)

def user_input():
    sent=input("Enter the sentence or word :")
    return sent
def user_choice():
    print("1- enter 'a' to generate gibberish type 1\n2- enter 'b' to generate gibberish type 2\n"
          "3- enter 'e' to exit\n")
    ch=input("your choice here :")
    return ch

choice=""
while choice not in ['e','E','exit','Exit','EXIT']:

    choice=user_choice()
    sent = user_input()
    if(choice == 'a'):
        type_one(sent)
    elif(choice == 'b'):
        type_two(sent)
    else:
        print("\n invalid entry , please make a valid selection: ")
        user_choice()
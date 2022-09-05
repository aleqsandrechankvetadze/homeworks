def maps(a):
    #ცარიელი სიის შექმნა
    #for ციკლის გამოყენებით გადაუარეთ ძველი სიის ელემენტებს
    #ახალ სიაში გაორმაგებული ელემენტების append 

    my_list = []
    for element in a:
        my_list.append(element * 2)

    return my_list
    
    print(maps([5, 15, 30]))

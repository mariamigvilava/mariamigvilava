# )შექმენით ფუნქცია, რომელშიც იქნება რიცხვებით სავსე სია, ფუნქციამ
# უნდა გამოითვალოს ამ სიაში არსებული რიცხვების ჯამი]



def la_lista():
    list = [1,2,3,4,5,6,7]
    sum = 0
    for i in range(len(list)):
        sum += list[i]
        print(sum)
        

la_lista()
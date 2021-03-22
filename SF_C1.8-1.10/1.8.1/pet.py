from practice_c1.cat import Cat

cats = [
    Cat(
        name= "Baron",
        gender= "male",
        age= "2"
    ),
    Cat(
        name= "Sam",
        gender= "male",
        age= "2"
    )
]

for pet in cats:
    print(pet.print_cats())



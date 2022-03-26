class movie:
    """movie class developed by nafees for python demo"""

    def __init__(self, title, hero, heroine):
        self.title= title
        self.hero= hero
        self.heroine= heroine

    def info(self):
        print("movie name: ", self.title)
        print("hero name: ", self.hero)
        print("heroine name", self.heroine)

list_of_movie= []
while True:
    title= input("Enter movie name: ")
    hero= input("Enter hero name: ")
    heroine= input("heroine name: ")

    m = movie(title, hero, heroine)           # object created

    list_of_movie.append(m)

    print(":::movie added successfully:::")

    option = input("Do you want to add more movie: Yes| No: ")
    if option.lower()== 'no':
        break

print("\n****************************************************************")
print("################## All movie information #######################")
print("****************************************************************")
for movie in list_of_movie:
    movie.info()
    print()



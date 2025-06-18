class emp:
    def __init__(self, name, sal):
        self.name = name
        self.sal = sal

    @property
    def first_name(self):
        l = self.name.split(" ")
        return l[0]

    @first_name.setter
    def first_name(self, first):
        l = self.name.split(" ")
        if len(l) > 1:
            new_name = f"{first} {l[1]}"
        else:
            new_name = first  # or f"{first} Lastname" if you want to ensure two parts
        self.name = new_name

e = emp("Pranav", 10000000)

print(e.first_name)    # Output: Pranav
e.first_name = "Sahil"
print(e.name)          # Output: Sahil

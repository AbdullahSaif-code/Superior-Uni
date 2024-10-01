# Main Grand_Father
class main_1:
    def __init__(self, Gfather):
        self.Gfather = Gfather

    def show_gfather(self):
        print(f"Grandfather: {self.Gfather}")
# children
class sub_1(main_1):
    def __init__(self, Gfather):
        super().__init__(Gfather)

class sub_2(main_1):
    def __init__(self, Gfather):
        super().__init__(Gfather)

# Sub child
class baby(sub_1, sub_2):
    def __init__(self, Gfather):
        super().__init__(Gfather)

# Create an instance of baby
b = baby("Abdullah")

# Call method to show Gfather
b.show_gfather()

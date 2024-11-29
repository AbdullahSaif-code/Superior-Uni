class Board:
    def __init__(self):
        self.cells = {i: " " for i in range(1, 10)}

    def display(self):
        display_cells = {k: (v if v != " " else str(k)) for k, v in self.cells.items()}
        print(f" {display_cells[1]} | {display_cells[2]} | {display_cells[3]} ")
        print("-----------")
        print(f" {display_cells[4]} | {display_cells[5]} | {display_cells[6]} ")
        print("-----------")
        print(f" {display_cells[7]} | {display_cells[8]} | {display_cells[9]} ")

    def update(self, cell, symbol):
        if self.cells[cell] == " ":
            self.cells[cell] = symbol
            return True
        return False

    def is_full(self):
        return all(value != " " for value in self.cells.values())

    def reset(self):
        self.cells = {i: " " for i in range(1, 10)}

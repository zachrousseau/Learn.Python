class Column:
    def __init__(self):
        self.values = [0, 1, 2, 3, 4, 5, 6, 8, 9]


    def spin(self):
        from random import randrange
        
        position = randrange(10)
        self.values = self.values[position:] + self.values[:position]

class SlotMachine: 
    def __init__(self):
        self.column1 = Column()
        self.column2 = Column() 
        self.column3 = Column() 

    def __str__(self):
        display_array = [
            [self.column1.values[0], self.column2.values[0], self.column3.values[0]],
            [self.column1.values[1], self.column2.values[1], self.column3.values[1]],
            [self.column1.values[2], self.column2.values[2], self.column3.values[2]],
        ]
        
        display_string = f"""
        | - | - | - |
        | {display_array[0][0]} | {display_array[0][0]} | {display_array[0][0]} | 
        | {display_array[1][0]} | {display_array[1][1]} | {display_array[1][2]} | 
        | {display_array[2][0]} | {display_array[2][1]} | {display_array[2][2]} | 
        | - | - | - |
        """
        return display_string


    def __spin(self):
        self.column1.spin()
        self.column2.spin()
        self.column3.spin()

    def lever(self):
        self.__spin()

    



def main():
    print("Play Slots!")

    machine1 = SlotMachine() 
    machine1.lever()

    print(machine1)



if __name__ == "__main__":
    main()
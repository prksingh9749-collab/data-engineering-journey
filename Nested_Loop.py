height = 5
for row in range(height):
    for col in range(height * 2):
        if row == 0 and col == height:
            print("*", end="")
        elif row != 0:
            if col == height - row or col == height + row:
                print("*", end="")
            elif row == height // 2 and height - row < col < height + row:
                print("*", end="")
            else:
                print(" ", end="")
        else:
            print(" ", end="")
    print()

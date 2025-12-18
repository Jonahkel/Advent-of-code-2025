def main():
    pos = 50
    count = 0

    with open("day-01.txt", 'r') as file:
        for line in file:
            print("Next rotation:")
            rotation = int(line[1:])
            if rotation == 0: continue
            count += rotation // 100
            rotation %= 100
            if line[0] == "L":
                rotation *= -1
            new_pos = pos+rotation 
            print(pos)
            if new_pos >= 100 or (pos and new_pos <= 0):
                count += 1

            pos = new_pos % 100
            print(pos)
    
    print(count)




if __name__ == "__main__":
    main()
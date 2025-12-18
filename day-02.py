def main():
    with open("day-02.txt", 'r') as file:
        content = file.read()
        items = content.split(',')
    
    invalid_sum = 0

    for item in items:
        begin, _, end = item.partition('-')
        for id in range(int(begin), int(end)+1):
            id = str(id)
            for num_repeats in range(2, len(id)+1):
                if len(id)%num_repeats == 0: 
                    id_part = id[:len(id)//num_repeats]
                    is_invalid = True
                    for i in range(1, num_repeats):
                        if id_part != id[(i * len(id))//num_repeats:((i+1)*len(id))//num_repeats]:
                            is_invalid = False
                    if is_invalid:
                        invalid_sum += int(id)
                        print(f"Invalid: {id}")
                        break

            
    
    print(invalid_sum)


if __name__ == "__main__":
    main()
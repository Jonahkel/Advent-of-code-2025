def main():
    total = 0
    digit_value = lambda x: int(x[1])
    num_digits = 12
    with open("day-03.txt", 'r') as file:
        for line in file:
            line = line.strip()
            indices = [-1]
            for digit in range(num_digits):
                end_range = len(line) - num_digits + digit + 1
                next_index = max(enumerate(line[indices[-1]+1:end_range]), key=digit_value)[0]
                next_index+=indices[-1]+1
                print(f"Digit {digit}: Index {next_index}, Value {line[next_index]}")
                indices.append(next_index)
            value_str = ''.join(line[index] for index in indices[1:])
            print(value_str)
            total += int(value_str)
        
    print(total)



if __name__ == "__main__":
    main()
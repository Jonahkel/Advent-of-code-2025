import math
def main():
    with open("day-06.txt", 'r') as file:
        lines = [line for line in file]
        columns = [list(col) for col in zip(*lines)]
        equations = []
        col_idx = 0
        while col_idx < len(columns):
            nums = []
            operator = columns[col_idx][-1]
            end_of_equation = False
            while col_idx < len(columns) and not end_of_equation:
                num = ''
                for digit in columns[col_idx][:-1]:
                    if digit.isdigit():
                        num += digit
                if num.isdigit():
                    nums.append(num)
                else:
                    end_of_equation = True
                col_idx += 1
            nums.append(operator)
            equations.append(nums)
        answers = []
        for equation in equations:
            operator = equation[-1]
            terms = (int(term) for term in equation[:-1])
            if operator == '+':
                answers.append(sum(terms))
            elif operator == '*':
                answers.append(math.prod(terms))
            print(f"{operator.join(str(term) for term in equation[:-1])} = {answers[-1]}")
        print(sum(answers))

        




if __name__ == "__main__":
    main()
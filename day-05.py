def main():
    ranges = []
    with open("day-05.txt", 'r') as file:
        for line in file:
            line = line.strip()
            if line == '':
                break
            start, _, end = line.partition('-')
            ranges.append((int(start), int(end)))
        ranges.sort(key=lambda x:x[0])

        merged = []

        cur_start, cur_end = ranges[0]
        for start, end in ranges:
            if start <= cur_end:
                cur_end = max(end, cur_end)
            else:
                merged.append((cur_start, cur_end))
                cur_start, cur_end = start, end
        
        merged.append((cur_start, cur_end))

        total = 0
        for start, end in merged:
            total += end-start+1
        
        print(total, merged)
        
        # num_fresh = 0
        # for line in file:
        #     id = int(line.strip())
        #     is_fresh = False
        #     for start, end in ranges:
        #         if id >= start and id <= end:
        #             is_fresh = True
        #             break
        #     num_fresh += 1 if is_fresh else 0

        # print(num_fresh)




if __name__ == "__main__":
    main()
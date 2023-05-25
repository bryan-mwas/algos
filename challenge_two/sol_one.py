def solution(l):
    # Your code here
    if l is None or len(l) == 0:
        return 0
    elif len(l) == 1 and sum(l) % 3 != 0:
        return 0
    else:
        l.sort(reverse=True)
        remainder = sum(l) % 3
        if remainder == 0:
            return int(''.join(map(str, l)))
        else:
            num_with_remainder = [n for n in l if n % 3 == remainder]
            if len(num_with_remainder) >= 1:
                # remove the last num since its the smallest
                l.remove(num_with_remainder[-1])
            else:
                # remove 2 digits that have remainder of 1 or 2
                cache = [n for n in l if n % 3 == (3 - remainder) % 3]
                l.remove(cache[-1])
                l.remove(cache[-2])

            # Handle edge case when both values have been removed, for double digit numbers
            if (len(l) == 0):
                return 0

            return int(''.join(map(str, l)))


if __name__ == '__main__':
    num = [3, 1, 4, 1]
    num = [3, 1, 4, 1, 5, 9]
    num = [1]
    num = [7, 4]
    print(solution(num))

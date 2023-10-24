
def to_binary(num_of_days: int, number: int) -> str:
    to_str = str(bin(number))
    padding = num_of_days - len(to_str[2:])
    return "0" * padding + to_str[2:]


def ways_to_miss(num_of_days: int):
    num_of_ways = 0
    for i in range(2 ** num_of_days):
        to_bin = to_binary(num_of_days=num_of_days, number=i)
        if "0000" not in to_bin:
            num_of_ways += 1
    return num_of_ways


def probability_of_missing(num_of_days: int):
    num_of_ways_to_miss = 0
    for i in range(2 ** (num_of_days - 1)):
        to_bin = to_binary(num_of_days, i)
        if "0000" not in to_bin:
            num_of_ways_to_miss += 1
    return num_of_ways_to_miss


def main(num_of_days: int):
    _ways_to_miss = ways_to_miss(num_of_days=num_of_days)
    _probability_of_missing = probability_of_missing(num_of_days=num_of_days)
    print(f"{_probability_of_missing}/{_ways_to_miss}", end="")

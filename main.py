import argparse
import csv
from tabulate import tabulate


def read_csv(file_path: str) -> list:
    with open(file_path, newline="", encoding="utf-8") as csvfile:
        file = csv.DictReader(csvfile)
        return list(file)


def filter_data(data: list, column: str, operator: str, value: str) -> list:
    if not data:
        return []

    if column not in data[0]:
        raise ValueError(f"Column {column} not found")

    try:
        val = float(value)
    except ValueError:
        val = value

    result = []
    for row in data:
        column_value = row[column]

        try:
            col_val = float(column_value)
        except ValueError:
            col_val = column_value

        if operator == "=":
            if col_val == val:
                result.append(row)

        elif operator == ">":
            if col_val > val:
                result.append(row)

        elif operator == "<":
            if col_val < val:
                result.append(row)

        else:
            raise ValueError(f"Unsupported operator {operator}")
    return result


def aggregate_data(data: list, column: str, func: str):
    if not data:
        return None

    if column not in data[0]:
        raise ValueError(f"Column {column} not found")

    try:
        numbers = [float(row[column]) for row in data]
    except ValueError:
        raise ValueError(f"Cannot aggregate non-numeric column {column}")

    if func == "max":
        return max(numbers)

    elif func == "min":
        return min(numbers)

    elif func == "avg":
        return sum(numbers) / len(numbers)

    else:
        raise ValueError("Unsupported aggregation function")


def main():
    parser = argparse.ArgumentParser(description="CSV parser")

    parser.add_argument("file", help="Path to csv-file")
    parser.add_argument("--where", nargs=3, metavar=("COLUMN", "OPERATOR", "VALUE"),
                        help="Filter condition")
    parser.add_argument("--aggregate", nargs=2, metavar=("COLUMN", "FUNCTION"),
                        help="Aggregate column")

    args = parser.parse_args()

    data = read_csv(args.file)

    if args.where:
        column, operator, value = args.where
        data = filter_data(data, column, operator, value)

    if args.aggregate:
        column, func = args.aggregate
        result = aggregate_data(data, column, func)
        print(tabulate([[result]], headers=[func]))
    else:
        print(tabulate(data, headers="keys"))


if __name__ == "__main__":
    main()

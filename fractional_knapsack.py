def fractional_knapsack(weights, values, capacity):
    n = len(values)
    ratio = [(values[i] / weights[i], i) for i in range(n)]
    ratio.sort(reverse=True)

    total_value = 0.0
    remaining_capacity = capacity
    selected_items = []

    for r, i in ratio:
        if weights[i] <= remaining_capacity:
            total_value += values[i]
            remaining_capacity -= weights[i]
            selected_items.append((i + 1, 1.0))
        else:
            fraction = remaining_capacity / weights[i]
            total_value += values[i] * fraction
            selected_items.append((i + 1, fraction))
            break

    print("\nSelected items (item number, fraction taken):")
    for item, frac in selected_items:
        print(f"Item {item}: {frac*100:.1f}% taken")

    return total_value

while True:
    print("Ctrl+C to terminate...")
    n = int(input("Enter number of items: "))
    values = [float(i) for i in input("Enter values of items (space separated): ").split()]
    weights = [float(i) for i in input("Enter weights of items (space separated): ").split()]
    capacity = float(input("Enter maximum weight (capacity): "))

    max_profit = fractional_knapsack(weights, values, capacity)
    print(f"\nThe maximum value of items that can be carried: {max_profit:.2f}\n")
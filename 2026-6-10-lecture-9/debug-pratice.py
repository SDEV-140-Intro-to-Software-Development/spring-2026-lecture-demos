def weekly_pay(hours, rate):
    # Overtime should be 1.5x for any hours over 40
    if hours > 40:
        overtime_hours = hours - 40
        base_pay = (40 * rate)
        overtime_pay = overtime_hours * rate * 1.5
        return base_pay + overtime_pay

    return hours * rate

# print(weekly_pay(40, 10))  # expected 400
print(weekly_pay(45, 10))  # expected 475
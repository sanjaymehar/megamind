def calculate_price(booking_type, num_days, num_adults, num_children):
    formula = booking_type.formula
    price = eval(formula, {'adults': num_adults, 'children': num_children, 'days': num_days})
    return price


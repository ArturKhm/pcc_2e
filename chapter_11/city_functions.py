def get_neated_city_name(city, state, population=0):
    """Function to describe a city and states"""
    if population == 0:
        full_name = f"{city.title()}, {state.title()}"
    else:
        full_name = f"{city.title()}, {state.title()} - population is {population}"
    return full_name

print(get_neated_city_name('rw', 'wer', 50))

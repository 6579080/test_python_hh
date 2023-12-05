def run_rec(is_raining, temperature):
    if is_raining:
        return 'на улице дождь'
    elif temperature < 5:
        return 'слишком холодно'
    elif temperature >= 5 and temperature <= 15:
        return ' на пробежку'
    else:
        return 'слишком жарко'

raining = False
temperature = 6
print(run_rec(raining, temperature))

# if is_raining: в первом случае и elif temperature >= 5 and temperature <= 15
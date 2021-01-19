def bananas_per_hour_check(piles, hours, bananas_per_hour):
    elapsed_time = 0
    for bananas in piles:
        if bananas % bananas_per_hour > 0:
            elapsed_time += bananas // bananas_per_hour + 1
        else:
            elapsed_time += bananas // bananas_per_hour
    if elapsed_time <= hours:
        return True
    else:
        return False

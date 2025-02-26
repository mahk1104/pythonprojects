def EXPECTED_BAKE_TIME():
    return 40  # Expected bake time in minutes

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes).
    """
    return EXPECTED_BAKE_TIME() - elapsed_bake_time  


elapsed_time = 30
remaining_time = bake_time_remaining(elapsed_time)
print(f"Remaining bake time: {remaining_time} minutes")

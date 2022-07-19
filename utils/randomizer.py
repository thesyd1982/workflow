import random


def random_time_sleep(time_sleep, time_random_offset):
    return random.uniform(time_sleep - time_random_offset, time_sleep + time_random_offset)
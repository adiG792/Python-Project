import random


def estimated_pi(n):
    num_points_inside_circle = 0
    num_points_outside_circle = 0
    for _ in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = x ** 2 + y ** 2
        if distance <= 1:
            num_points_inside_circle += 1
        num_points_outside_circle += 1

    return 4*num_points_inside_circle/num_points_outside_circle

print(estimated_pi(100))

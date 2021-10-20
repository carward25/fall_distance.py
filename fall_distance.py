def fall_distance(falling_time):
    return 0.5 * 9.8 * falling_time * falling_time


time = float(input("Enter the amount of time for which the object is falling: "))
print("Distance the object has fallen is", fall_distance(time))
H = int(input("Enter the hour (0-12): "))
M = int(input("Enter the minute (0-59): "))

if H < 0 or H > 12 or M < 0 or M > 59:
    print("Invalid time input.")
else:
    hour_angle = (H % 12) * 30 + M * 0.5

    minute_angle = M * 6

    angle1 = abs(hour_angle - minute_angle)
    angle2 = 360 - angle1

    min_angle = min(angle1, angle2)
    print(f"The minimum angle between the hour and minute hands is: {int(min_angle)} degrees")

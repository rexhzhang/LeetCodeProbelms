"""
Calculate the angle between hour hand and minute hand
This problem is know as Clock angle problem where we need to find angle between hands of an analog clock at a given time.

Examples:

Input:  h = 12:00, m = 30.00
Output: 165 degree

Input:  h = 3.00, m = 30.00
Output: 75 degree


Calculate the angle between hour hand and minute hand.

There can be two angles between hands, we need to print minimum of two. Also, we need to print floor of final result
angle. For example, if the final angle is 10.61, we need to print 10.

Input:

The first line of input contains a single integer T denoting the number of test cases. Then T test cases follow. Each
test case consists of one line conatining two space separated numbers h and m where h is hour and m is minute.

Output:
Coresponding to each test case, print the angle b/w hour and min hand in a separate line.

Constraints:

1 ≤ T ≤ 100
1 ≤ h ≤ 12
1 ≤ m ≤ 60

Example:

Input
2
9 60
3 30

Output
90
75
"""

class Solution():
    def ClockAngleProblem(self, hour, minute):
        if hour is None or minute is None or hour < 0 or minute < 0:
            return print("Wrong input values")

        hour = hour % 12
        minute = minute % 60

        minuteAngle = minute / 60.0 * 360
        hourAngle = (hour/12.0) * 360 + minuteAngle/12.0


        result = max(hourAngle, minuteAngle) - min(hourAngle,minuteAngle)
        return result if result <= 180 else result % 180

test = Solution()
result = test.ClockAngleProblem(3, 30)
print(result)
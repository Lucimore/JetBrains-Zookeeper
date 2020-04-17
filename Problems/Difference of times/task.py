#  Posted from EduTools plugin
# put your python code here
hours1 = int(input()) * 60 * 60
minutes1 = int(input()) * 60
seconds1 = int(input())
hours2 = int(input()) * 60 * 60
minutes2 = int(input()) * 60
seconds2 = int(input())
answer = (hours1 + minutes1 + seconds1) - (hours2 + minutes2 + seconds2)
print(abs(answer))

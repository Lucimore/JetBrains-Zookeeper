#  Posted from EduTools plugin
# put your python code here
first_group = int(input())
second_group = int(input())
third_group = int(input())
if first_group % 2 != 0:
    first_group += 1
if second_group % 2 != 0:
    second_group += 1
if third_group % 2 != 0:
    third_group += 1
answer = int((first_group + second_group + third_group) / 2)
print(answer)
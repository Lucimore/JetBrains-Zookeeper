#  Posted from EduTools plugin
start_number = int(input())
end_number = int(input())
period = 12
answer = 0
while start_number > end_number:
    start_number /= 2
    answer += period
print(answer)
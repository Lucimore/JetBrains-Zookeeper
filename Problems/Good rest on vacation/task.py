#  Posted from EduTools plugin
# put your python code here
days = int(input())
food = int(input())
flight = int(input()) * 2
hotel = int(input())
total = days * food + (days - 1) * hotel + flight
print(total)
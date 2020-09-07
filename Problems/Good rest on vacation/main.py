# put your python code here
duration_of_vacation = int(input())
total_food_in_day = int(input())
one_way_cost_flight = int(input())
cost_of_one_night_in_hotel = int(input())
print(int((total_food_in_day * duration_of_vacation) + (one_way_cost_flight * 2) + (cost_of_one_night_in_hotel * (duration_of_vacation - 1))))
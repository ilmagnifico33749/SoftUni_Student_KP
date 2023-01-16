from _collections import deque

water_available = int(input())

my_queue_1_people = deque()

command = input()

while command != "Start":

    my_queue_1_people.append(command)
    command = input()

else:
    for person in range(len(my_queue_1_people)):
        command_two = input()
        while command_two != "End":
            command_details = command_two.split()
            print(f"Water Available: {water_available}")
            if len(command_details) == 1:
                water_to_consume = int(command_details[0])
                print(f"Water to consume: {water_to_consume}")
                print(f"Water Available: {water_available}")

                if water_to_consume <= water_available:
                    water_available -= water_to_consume
                    # print(f"{print(my_queue_1_people.popleft())} got water")
                    print(f"{my_queue_1_people[0]} got water")
                    my_queue_1_people.popleft()
                else:
                    # print(f"{print(my_queue_1_people.popleft())} must wait")
                    print(f"{my_queue_1_people[0]} must wait")
                    my_queue_1_people.popleft()
            elif len(command_details) == 2:
                if command_details[0] == "refill":
                    print(f"Refilling")
                    print(command_details[0])
                    print(command_details[1])
                    print(water_available)
                    water_available += int(command_details[1])
                    print(f"REFILLING")
                    print(f"Water Available: {water_available}")
            command_two = input()

        else:
            print(f"{water_available} liters left")
            break


print(water_available)




# Creating to help make it easier to read in terminal
def print_new_line(stuff):
    print("")
    print(stuff)


new_list = [
{'train': "72C", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "72D", 'frequency_in_minutes': 15, 'direction': "south"},
{'train': "610", 'frequency_in_minutes': 5, 'direction': "north"},
{'train': "611", 'frequency_in_minutes': 5, 'direction': "south"},
{'train': "80A", 'frequency_in_minutes': 30, 'direction': "east"},
{'train': "80B", 'frequency_in_minutes': 30, 'direction': "west"},
{'train': "110", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "111", 'frequency_in_minutes': 15, 'direction': "south"}
]

# 1
train111_direction = new_list[-1]['direction']
print_new_line(train111_direction) # checking to see if it was saved correctly

# 2
train80b_frequency = new_list[5]['frequency_in_minutes']
print_new_line(train80b_frequency) # checking to see if it was saved correctly

# 3
train610_direction = new_list[2]['direction']
print_new_line(train610_direction)

# 4
print('')
train_names = []
for i in new_list:
    if i['direction'] == 'north':
        train_names.append(i['train'])

print(train_names)

# 5
print('')
east_trains = []
for i in new_list:
    if i['direction'] == 'east':
        east_trains.append(i['train'])

print(east_trains)

# 6
def add_train(train_list, direction):
    temp_train = []
    for i in train_list:
        if i['direction'] == direction:
            temp_train.append(i['train'])
    return temp_train

# 7
new_list[0]['first_departure_time'] = 6
print_new_line(new_list[0])
        
# 8
trains = [
{'train': "72C", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "72D", 'frequency_in_minutes': 15, 'direction': "south"},
{'train': "610", 'frequency_in_minutes': 5, 'direction': "north"},
{'train': "611", 'frequency_in_minutes': 5, 'direction': "south"},
{'train': "80A", 'frequency_in_minutes': 30, 'direction': "east"},
{'train': "80B", 'frequency_in_minutes': 30, 'direction': "west"},
{'train': "110", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "111", 'frequency_in_minutes': 15, 'direction': "south"}
]

trains_by_frequency = {}
for train in trains:
    freq = train['frequency_in_minutes']
    name = train['train']
    if freq in trains_by_frequency:
        trains_by_frequency[freq].append(name)
    else:
        trains_by_frequency[freq] = [name]

print(trains_by_frequency)
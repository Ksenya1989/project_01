# Пункт А c использованием метода random и datetime

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Stayin\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

import random
a, b, c = random.randint(0,2), random.randint(3,5), random.randint(6,8)
import datetime
print(f"Три песни {my_favorite_songs[a][0]}, {my_favorite_songs[b][0]}, {my_favorite_songs[c][0]}", end="")
print(f"звучат {datetime.timedelta(seconds = (int(round((my_favorite_songs[a][1] + my_favorite_songs[b][1] + my_favorite_songs[c][1]), 2)*60)))} минут")


# Пункт B c использованием метода random и datetime
 
my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Stayin\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

my_favorite_songs_2 = []
for song in my_favorite_songs_dict:
    my_favorite_songs_2.extend([[song, my_favorite_songs_dict[song]]])

import random
random_songs = []
thing = 0
while thing < 3:
    random_songs.append(my_favorite_songs_2[random.randint(0, len(my_favorite_songs_2)-1)])
    thing += 1
print(f"Три песни {random_songs[0][0]}, {random_songs[1][0]}, {random_songs[2][0]}", end="") 
print(f' звучат {datetime.timedelta(seconds = (int(sum([i[1] for i in random_songs])*60)))} минут')






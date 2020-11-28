class Track:
    def __init__(self, track_title, duration):
        self.track_title = track_title
        self.duration = int(duration)

    def __str__(self):
        return (f'{self.track_title} - {self.duration} мин')

    def __lt__(self, other):
      return self.duration > other.duration   


class Album:
    def __init__(self, album_title, band):
        self.album_title = album_title
        self.band = band
        self.tracks_list = []

    def add_tracks(self, track):
        self.tracks_list.append(track)
        return self.tracks_list

    def get_duration(self):
        summa = 0
        for i in self.tracks_list:
            summa += i.duration
        print(f'Длина альбома «{self.album_title}» — {summa} минут')

    def __str__(self):
      print (f'Группа: {self.band}')
      print (f'Альбом: {self.album_title} ')
      for i in self.tracks_list:
          print (f'Трек: {i.track_title} - {i.duration} мин')
      return('')    


track_one = Track('первый трек', 1)
track_two = Track('второй трек', 2)
track_three = Track('третий трек', 3)
track_four = Track('четвертый трек', 4)
track_five = Track('пятый трек', 4)
track_six = Track('шестой трек', 4)

album_one = Album('Первый альбом', 'Первая группа')
album_one.add_tracks(track_one)
album_one.add_tracks(track_two)
album_one.add_tracks(track_three)

album_two = Album('Второй альбом', 'Вторая группа')
album_two.add_tracks(track_four)
album_two.add_tracks(track_five)
album_two.add_tracks(track_six)

print(album_one) 
print(album_two)
# album_one.get_duration()
# album_two.get_duration()

print(track_one)
print(track_two)

print(track_one < track_two)






  




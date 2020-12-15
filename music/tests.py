import datetime
from unittest.suite import TestSuite
from django.test import TestCase
import django
from music.models import *
# Create your tests here.

def test_separator(func):
    def separator(*arg):
        print('---------',func.__name__,'-------------')
        return func(arg)
    return separator
class DBTestCase(TestCase):
    @staticmethod
    def printList(lst):
        for i in lst:
            print(i)

    def setUp(self):
        ar1=Artist.objects.create(name= 'artist1')
        ar2=Artist.objects.create(name= 'artist2')
        ar3=Artist.objects.create(name= 'artist3')
        ar4=Artist.objects.create(name= 'artist4')
        ar5=Artist.objects.create(name= 'artist5')
        #album has many to many with artist
        a1=Album.objects.create(name="album1", release_date='1234-12-03', album_type = 1)
        a2=Album.objects.create(name="album2", release_date='1234-12-03', album_type = 3)
        a3=Album.objects.create(name="album3", release_date='1234-12-03', album_type = 2)
        a4=Album.objects.create(name="album4", release_date='1234-12-03', album_type = 0)
        a5=Album.objects.create(name="album5", release_date='1234-12-03', album_type = 2)
        
        #track has many to many with artist
        d = datetime.timedelta(seconds = 60) 
        t1=Track.objects.create(name = 'track1',track_number = 0, duration = d, album = a1)
        t2=Track.objects.create(name = 'track2',track_number = 1, duration = d, album = a2)
        t3=Track.objects.create(name = 'track3',track_number = 2, duration = d, album = a3)
        t4=Track.objects.create(name = 'track4',track_number = 3, duration = d, album = a4)
        t5=Track.objects.create(name = 'track5',track_number = 4, duration = d, album = a5)

        #add album owner
        a1.artist.add(ar1,ar2,ar3)
        a2.artist.add(ar4,ar2,ar5)
        a3.artist.add(ar3,ar4,ar1)

        #add track credit
        t1.artist_credits.add(ar1,ar4,ar5)
        t2.artist_credits.add(ar3)
        t3.artist_credits.add(ar2,ar1)
        t4.artist_credits.add(ar1,ar2,ar5)
        t5.artist_credits.add(ar4)
    @test_separator
    def test_print_all_artist(self):
        """object print are defined"""
        artists = Artist.objects.all()
        DBTestCase.printList(artists)    
    @test_separator
    def test_print_all_albums(self):
        """object print are defined"""
        albums = Album.objects.all()
        DBTestCase.printList(albums)
    @test_separator
    def test_print_all_tracks(self):
        """object print are defined"""
        tracks = Track.objects.all()
        DBTestCase.printList(tracks)
    @test_separator
    def test_print_all_credit(self):
        """object print are defined"""
        credits = Credit.objects.all()
        DBTestCase.printList(credits)

# class MiscTest(TestCase):
#     def test_DJango_version(self):
#         print(django.get_version())



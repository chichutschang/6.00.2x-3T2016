# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 16:30:52 2016

@author: chi-chu tschang
"""

class SongList(object):
    def __init__(self, max_size):
        self.max_size = max_size
        self.remaining_size = max_size
        self.list = []

    def get_max_size(self):
        return self.max_size
    
    def get_remaining_size(self):
        return self.remaining_size
        
    def get_list(self):
        return self.list

    def space_for_song(self, song):
        return song.get_size()<= self.remaining_size
        
    def add_song(self, song):
        self.list.append(song.get_name())
        self.remaining_size -= song.get_size()        

class Song(object):
    def __init__(self, song):
        self.name = song[0]
        self.length = song[1]
        self.size = song[2]
        
    def get_name(self):
        return self.name
    
    def get_length(self):
        return self.length
        
    def get_size(self):
        return self.size

def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """
    songlist=SongList(max_size)
    playlist=[]
    for s in songs:
        playlist.append(Song(s))

    if len(playlist) > 0 and songlist.space_for_song(playlist[0]):
            songlist.add_song(playlist.pop(0))
            playlist.sort(key = lambda x: x.get_size())
            while len(playlist) > 0 and songlist.space_for_song(playlist[0]):
                songlist.add_song(playlist.pop(0))
        
    return songlist.get_list()
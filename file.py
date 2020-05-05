def song_decoder(song):
    cadena=""
    word=song.split('WUB')
    new_song = [i for i in word if i.strip()]
    for i in range(len(new_song)):
        if i<len(new_song)-1:
            cadena=cadena+new_song[i]+' '
        else:
            cadena=cadena+new_song[i]
        
    return cadena 

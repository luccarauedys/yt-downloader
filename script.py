from pytube import YouTube, Playlist

option = input('''O que deseja fazer?
- Digite V para baixar um VIDEO
- Digite P para baixar uma PLAYLIST
''')

if option.upper() == 'V':
    # FAZER DOWNLOAD DE SOMENTE UM VIDEO
    video_link = input('\nLINK DO VIDEO: ')
    video = YouTube(video_link)

    print(f'Baixando {video.title}...')
    video.streams.get_highest_resolution().download('./downloads/videos')
    print('Video baixado com sucesso.')
if option.upper() == 'P':
    # FAZER DOWNLOAD DE TODOS OS VIDEOS DE UMA PLAYLIST
    playlist_link = input('\nLINK DA PLAYLIST: ')
    playlist = Playlist(playlist_link)

    print(f'Baixando: {playlist.title}...')
    for video in playlist.videos:
        video.streams.get_highest_resolution().download(
            f'./downloads/playlists/{playlist.title}')
    print("Playlist baixada com sucesso.")

from pytube import YouTube, Playlist
from pytube.exceptions import VideoUnavailable

option = input('''O que deseja fazer?
- Digite V para baixar um VIDEO
- Digite P para baixar uma PLAYLIST

''')

if option.upper() == 'V':
    video_url = input('\nLINK DO VIDEO: ')
    try:
        video = YouTube(video_url)
    except VideoUnavailable:
        print(f'Erro ao realizar download. Video indisponivel.')
    else:
        print(f'\nBaixando: {video.title}...')
        video.streams.get_highest_resolution().download('./downloads/videos')
        print('Download concluido com sucesso.')

if option.upper() == 'P':
    playlist_url = input('\nLINK DA PLAYLIST: ')
    playlist = Playlist(playlist_url)
    print(f'\nIniciando download da playlist: {playlist.title}')

    for video_url in playlist.video_urls:
        try:
            video = YouTube(video_url)
        except VideoUnavailable:
            print(
                f'[Erro]: Video indisponivel em {video_url}. Pulando para o proximo...')
        else:
            video = YouTube(video_url)
            print(f'Baixando video: {video.title}')
            video.streams.get_highest_resolution().download(
                f'./downloads/playlists/{playlist.title}')

    print("Playlist baixada com sucesso.")

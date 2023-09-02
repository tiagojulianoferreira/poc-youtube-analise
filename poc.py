import os
from pytube import YouTube
from googleapiclient.discovery import build

# Chave de API do YouTube
API_KEY = 'AIzaSyBw8V3JN31MIHIsbkw71Go7H6FwCHJVllc'

# Inicializar a API do YouTube
youtube_api = build('youtube', 'v3', developerKey=API_KEY)

# Parâmetros da pesquisa
search_term = 'python'.lower()
max_results = 100  # Número máximo de resultados da pesquisa
region_code = 'BR'  # Código de região para o Brasil
language_code = 'pt'  # Código de idioma para o português

# Realizar a pesquisa
search_response = youtube_api.search().list(
    q=search_term,
    type='video',
    part='id,snippet',
    maxResults=max_results,
    regionCode=region_code,
    relevanceLanguage=language_code
).execute()

# Lista para armazenar URLs dos vídeos
video_urls = []

# Extrair URLs dos vídeos da resposta da pesquisa
for search_result in search_response.get('items', []):
    video_urls.append(f"https://www.youtube.com/watch?v={search_result['id']['videoId']}")

# Diretório para salvar os vídeos
output_directory = 'videos_python'
os.makedirs(output_directory, exist_ok=True)

# Baixar vídeos usando pytube
downloaded_videos = 0
max_videos_to_download = 20
max_video_duration = 240  # 4 minutos em segundos

for video_url in video_urls:
    if downloaded_videos >= max_videos_to_download:
        break

    try:
        yt = YouTube(video_url)
        if yt.length <= max_video_duration:
            # stream = yt.streams.get_highest_resolution()
            # print(f"Baixando: {yt.title}")
            # stream.download(output_path=output_directory)
            print(f'Baixando áudio de: {yt.title}')
            audio_stream = yt.streams.filter(only_audio=True).first()
            audio_stream.download(output_path='audio_downloads')  # Pasta onde os áudios serão salvos
            downloaded_videos += 1
    except Exception as e:
        print(f"Erro ao baixar o vídeo {video_url}: {e}")

print("Downloads concluídos.")

video_urls

import os
import googleapiclient.discovery
from dotenv import load_dotenv

# Carrega as configurações da API a partir do .env
load_dotenv()

#Define os critérios da busca
search_term = "tecnologia da informação"
max_results = 1000
region_code = 'BR'  # Código de região para o Brasil
language_code = 'pt'  # Código de idioma para o português

# Criamos uma instância do serviço de vídeos
youtube = googleapiclient.discovery.build("youtube", os.getenv("YOUTUBE_API_VERSION"), developerKey=os.getenv("YOUTUBE_API_KEY"))

# Buscamos vídeos em português para um termo "python"
search_response = youtube.search().list(
    q=search_term,
    #type="video",
    part='id,snippet',
    maxResults=max_results,
    regionCode=region_code,
    relevanceLanguage=language_code
).execute()

#print(search_response)

# Imprimimos os resultados
for item in search_response["items"]:
    print(f"Título: {item['snippet']['title']}")
    print(f"Canal: {item['snippet']['channelTitle']}")
    #print(f"Visualizações: {item['statistics']['viewCount']}")
    #print(f"Link: {item['snippet']['resourceId']['videoId']}")
    print()
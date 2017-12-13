import re
import requests
from bs4 import BeautifulSoup
from collections import defaultdict


def trim(s):
    '화이트스페이스 정리'
    return ' '.join(s.split())


def main():
    url = 'http://www.melon.com/chart/index.htm'

    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')

    # 불필요한 class="none" 태그 제거
    for tag in soup.select('.none'):
        tag.extract()

    song_dict = {}
    for tr_tag in soup.select('.d_song_list tbody tr'):
        song_tag = tr_tag.select('[href*=playSong]')[0]
        dummy, song_id = re.findall(r'\d+', song_tag['href'])
        title = trim(song_tag.text)
        singer = trim(tr_tag.select('[href*=goArtistDetail]')[0].text)
        song_dict[song_id] = {
            'title': title,
            'singer': singer,
            'like_count': None,
        }

    contsIds = ','.join(str(song_id) for song_id in song_dict.keys())
    like_response = requests.get('http://www.melon.com/commonlike/getSongLike.json', params={'contsIds': contsIds}).json()
    like_dict = { row['CONTSID']: row['SUMMCNT'] for row in like_response['contsLike'] }


    for song_id in song_dict:
        like_count = like_dict[int(song_id)]
        song_dict[song_id]['like_count'] = like_count

    sorted_song_list = sorted(
        song_dict.values(),
        key=lambda song: int(song['like_count']),
        reverse=True)

    for rank, song in enumerate(sorted_song_list[:10], 1):
        print('[{rank}] {title} - {like_count}'.format(rank=rank, **song))


if __name__ == '__main__':
    main()


import requests
from bs4 import BeautifulSoup
from collections import defaultdict


def main():
    url = 'https://datalab.naver.com/keyword/realtimeList.naver?where=main'

    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')

    keywords = defaultdict(int)
    for rank_tag in soup.select('.keyword_rank'):
        for tag in rank_tag.select('.list .title'):
            keywords[tag.text] += 1

    sorted_keywords = sorted(
        keywords.items(),
        key=lambda row: (-1 * row[1], row[0]))

    for rank, row in enumerate(sorted_keywords, 1):
        print('{}위 : {} ({}회 노출)'.format(rank, *row))


if __name__ == '__main__':
    main()


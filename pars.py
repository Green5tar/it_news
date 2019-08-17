import urllib.request
import csv
from bs4 import BeautifulSoup


burl = "https://www.itnews.com"

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def parse(html):
    projects = []
    soup = BeautifulSoup(html, 'html.parser')
#################################################################
    body = soup.find('section', class_='bodee')
    first=body.find('div', class_='top-story')
    second=body.find('div', class_='item-info')
    third=body.find('div', class_='read-more-link')

    photo=first.find('figure').find('a').find('img').get('src')

    projects.append({
        'image1': photo,
        'title': second.find('div').a.text,
        'discription': second.p.text,
        'read_more': 'https://www.itnews.com'+third.find('a').get('href')

    })
#################################################################
    all_news=body.find('div', class_='newsfeed news-col1')
    for new in all_news.find_all('div', class_='news-item'):

        unic_im=new.find('figure').find('a').find('img').get('data-original')
        unic_hed=new.find('div', class_="hed").find('div', class_='title').a.text
        unic_bot=new.p.text
        unic_read='https://www.itnews.com'+new.find('div', class_='read-more-link').find('a').get('href')

        projects.append ({
            'image1':unic_im,
            'title': unic_hed,
            'discription': unic_bot,
            'read_more': unic_read
        })
#################################################################
    main_second_col=body.find('div', class_='newsfeed news-col2')
    for second_col in  main_second_col.find_all('div', class_='news-item'):
        unic_im2 = second_col.find('figure').find('a').find('img').get('data-original')
        unic_hed2 = second_col.find('div', class_="hed").find('div', class_='title').a.text
        unic_bot2 = second_col.p.text
        unic_read2 ='https://www.itnews.com'+ second_col.find('div', class_='read-more-link').find('a').get('href')

        projects.append({
            'image1': unic_im2,
            'title': unic_hed2,
            'discription': unic_bot2,
            'read_more': unic_read2
        })
#################################################################
    for project in projects:
        print(project)

    return projects
##
##each row of '#' mean that it is the box which return all about news in one coln
##
def save(projects, path):

    with open(path, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')

        writer.writerow(('Image_Link','Title','Discription','News_Link'))

        writer.writerows(
            (project['image1'], project['title'], project['discription'], project['read_more']) for project in projects
        )

def main():
    projects = []

    projects.extend(parse(get_html(burl)))

    save(projects, 'it_news.csv')

if __name__ == '__main__':
    main()

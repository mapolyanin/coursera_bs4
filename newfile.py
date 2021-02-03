from bs4 import BeautifulSoup
import unittest
import re
import os

def parse(path_to_file):  
    html = open(path_to_file, encoding = 'utf-8').read()
    soup = BeautifulSoup(html, 'lxml')
    
    maindiv = soup.find('div', id= 'bodyContent')

    linkslen = 0
    """
    for a in maindiv.find_all('a'):
         print('tag: ', a.text)
         count_loc=0
         for s in  a.find_next_siblings():
             
             if s.name =='a':
                 count_loc +=1
             else:
                     if linkslen < count_loc:
                         linkslen = count_loc
             count_loc = 1
         print('LEN:', linkslen)
       """
    print(maindiv.prettyfy)   

def build_bridge(path, start_page, end_page):
    graf = {}
     
    """возвращает список страниц, по которым можно перейти по ссылкам со start_page на
    end_page, начальная и конечная страницы включаются в результирующий список"""

    # напишите вашу реализацию логики по вычисления кратчайшего пути здесь

def getlinks(page):
    link_list = []
    html = open(page, encoding = 'utf-8').read()
    soup = BeautifulSoup(html, 'lxml')
    for a in soup.find_all('a', href = True ):
        if re.match(r"/wiki", a['href']):
            if os.path.exists(a['href'][1:]):
                link_list.append(a['href'][1:])
    
    #print(link_list)                    
    return(page,  link_list)
    )
    

def get_statistics(path, start_page, end_page):
    """собирает статистику со страниц, возвращает словарь, где ключ - название страницы,
    значение - список со статистикой страницы"""

    # получаем список страниц, с которых необходимо собрать статистику 
    pages = build_bridge(path, start_page, end_page)
    # напишите вашу реализацию логики по сбору статистики здесь

    return statistic
             
             
getlinks('wiki/Artificial_intelligence')

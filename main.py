from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    course_cards = soup.find_all('div', class_="accordion")
    for course_one in course_cards :
        accordion_name = course_one.h2
        print(accordion_name);
    # print(course_cards);
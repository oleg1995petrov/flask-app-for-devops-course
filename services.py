import requests

from bs4 import BeautifulSoup as bs


def get_animal_img(animal):
    url = f'https://emojipedia.org/{animal}'
    response = requests.get(url)
    
    if response.status_code != 200: return
    
    soup = bs(response.content, 'html.parser')
    try:
        content = soup.find('div', class_='content')
        soup = bs(str(content), 'html.parser')
        img = soup.find('span').text
    except AttributeError:
        return 
    return img


def generate_message(animal=None, sound=None, count=None):
    message = ("You haven't passed all the arguments!\n"
               "Required arguments are:\n" 
               "-animal\n"
               "-sound\n"
               "-count\n")
    
    if all((animal, sound, count)):
        img = get_animal_img(animal)
        message = f'{animal} {img}  says {sound}\n' if img else message = f'{animal} says {sound}\n'
        
        if isinstance(count, int): 
            message *= count
            
        message += 'Made with ❤️  by Ventz.\n'
    return message 

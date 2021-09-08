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


def generate_error_msg():
    msg = ("You haven't passed all the arguments!\n"
           "The required arguments are:\n" 
           "- animal\n"
           "- sound\n"
           "- count\n")
    return msg


def generate_success_msg(animal=None, sound=None, count=None):
    if not all((animal, sound, count)):
        return generate_error_msg()

    img = get_animal_img(animal)
    msg = f'{animal.capitalize()} {img}  says {sound}.\n' if img else (
          f'{animal} says {sound}.\n')
    
    if isinstance(count, int): 
        msg *= count
    elif isinstance(count, str):
        try:
            msg *= int(count)
        except ValueError:
            pass                 

    msg += 'Made with ❤️  by Ventz.\n'
    return msg 


def generate_msg(data=None):    
    if not isinstance(data, dict):
        return generate_error_msg()

    animal = data.get('animal')
    sound = data.get('sound')
    count = data.get('count')
    return generate_success_msg(animal, sound, count)
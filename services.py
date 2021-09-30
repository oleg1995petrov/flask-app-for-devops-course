# import requests

# from bs4 import BeautifulSoup as bs
from emoji import emojize as emj

# The other way to retrieve an emoji 
# def get_animal_emoji(animal):
#     url = f'https://emojipedia.org/{animal.lower()}'
    
#     response = requests.get(url)
#     if response.status_code != 200: 
#         return
    
#     soup = bs(response.content, 'html.parser')
#     try:
#         content = soup.find('div', class_='content')
#         soup = bs(str(content), 'html.parser')
#         img = soup.find('span').text
#     except AttributeError:
#         return 
#     return img


def get_animal_emoji(animal):
    img = emj(f':{animal.lower()}:')
    img = img[1:-1].capitalize() if img.startswith(':') else img
    return img


def generate_error_msg():
    msg = ("You haven't passed all the required arguments!\n"
           "The following arguments are required:\n" 
           "- animal\n"
           "- sound\n"
           "- count\n")
    return msg


def generate_success_msg(animal=None, sound=None, count=None):
    if not all((animal, sound, count)):
        return generate_error_msg()

    img = get_animal_emoji(animal)
    msg = f'{img}  says {sound.lower()}.\n'
    
    if isinstance(count, int): 
        msg *= count
    elif isinstance(count, str):
        try:
            msg *= int(count)
        except ValueError:
            pass                 

    msg += 'Made with ❤️ by Ventz.\n'
    return msg 


def generate_msg(data=None):    
    if not isinstance(data, dict):
        return generate_error_msg()

    animal = data.get('animal')
    sound = data.get('sound')
    count = data.get('count')
    return generate_success_msg(animal, sound, count)

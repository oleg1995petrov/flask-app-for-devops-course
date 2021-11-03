from datetime import date
from emoji import emojize as emj


GREEN = '\033[32m'


def get_animal_emoji(animal):
    img = emj(f':{animal.lower()}:')
    img = img[1:-1].capitalize() if len(img) != 1 else img
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
    
    love = emj(':red_heart:')
    copyright = emj(':copyright:')
    curr_year = date.today().year
    msg += f"\n{GREEN}{copyright} {curr_year}. Made with {love}  by Ventz.\n"
    return msg


def generate_msg(data=None):    
    if not isinstance(data, dict):
        return generate_error_msg()

    animal = data.get('animal')
    sound = data.get('sound')
    count = data.get('count')
    return generate_success_msg(animal, sound, count)

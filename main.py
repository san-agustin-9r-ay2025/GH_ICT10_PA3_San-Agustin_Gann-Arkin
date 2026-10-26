# dictionaries
from pyscript import document, display #type:ignore

def game_details (e):
    document.getElementById('result').innerHTML = ''

    game = document.getElementById('dictionary').value.strip().title()
    game_developers = {
        'Roblox' : 'David Baszucki',
        'Codm' : 'TiMi Studio',
        'FNAF' : 'Scott Cawthon',
        'Minecraft' : 'Notch'
    } # specifying dictionaries
    game_check = game in game_developers
    display_message = ('Sorry,n your game is not in the list!', f'(game_developers)')
    display(display_message[game_check], target = 'result')
    game_developers['genshin impact'] = 'Hoyoverse' #adding a new element

    list_with_tuples = [(1, 'a'), (2, 'b'), (3, 'c')]
    tuple_with_strings = ('ab', 'cd', 'ef')
    list_with_strings = ['ax', 'by', 'cz']
    display(dict(list_with_tuples), target = 'result')
    display(dict(tuple_with_strings), target = 'result')
    display(dict(list_with_strings), target = 'result')

    keyword = ['Say', 'JM', 'Jay', 'Mace']
    value = ['Esguerra', 'Piansay', 'Estrada', 'Panela']
    students_nicknames = dict(zip(keyword, value))
    display(students_nicknames, target = 'result')

    philadelphia = {
        'c' : 'Joel Embiid',
        'pf' : 'Lebron James',
        'sf' : 'Jaylen Bronw',
        'sg' : 'VJ Edgecomb',
        'pg' : 'Tyrese Maxey'
    }

    philadelphia['pg'] = 'Stephen Curry' #updating
    del philadelphia['sg']
    display(philadelphia, target = 'result')

    dict1 = {'x' : 1, 'y' : 2, 'z' : 3}
    dict2 = {'a' : 4, 'b' : 5, 'c' : 6}

    display(dict1 | dict2, target = 'result') #combining
    merged_dictionary = {**dict1, **dict2}

    display(merged_dictionary, target = 'result')
    display(len(merged_dictionary), target = 'result')

    ai = {
        'tony stark' : 'creator',
        'JARVIS' : 'AI1',
        'FRIDAY' : 'AI2',
        'Edith' : 'AI3',
        'Vision' : 'AI4'
    }

    display('Vision' in ai, target = 'result') #chekcing
    display(ai.get('JARVIS'), target = 'result') # getting value
    display(ai.keys(), target = 'result') #getting a;; keywords
    display(ai.values(), target = 'result') #getting all values
    display(ai['tony stark'], target = 'result')

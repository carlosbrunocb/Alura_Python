import os

# print("##############################")
# print("####### Express Flavor #######")
# print("##############################", end="\n\n")

# Global Variables
__key_name     = 'name'
__key_category = 'category'
__key_active   = 'active'

__restaurant = [
    {'name'     : 'Fuzi',
     'category' : 'Japonesa',
     'active'   : False
    },
    {'name'     : 'Chão de Brasa',
     'category' : 'churrascaria',
     'active'   : False
    },
    {'name'     : 'Pizza Suprema',
     'category' : 'Italiana',
     'active'   : True
    }
]

def show_subtitle(text):
    '''
    Function: Show subtitle information.
    Parameters:
        - text = Message to be displayed
    '''
    os.system('cls')
    print(f'{text}')

def return_to_main_menu():
    '''
    Function: Return to main menu.
    '''
    input("""
    # ℙ𝕣𝕖𝕤𝕤 𝕖𝕟𝕥𝕖𝕣 𝕥𝕠 𝕣𝕖𝕥𝕦𝕣𝕟 𝕥𝕠 𝕥𝕙𝕖 𝕞𝕒𝕚𝕟 𝕞𝕖𝕟𝕦.
    """)
    main()

def closing_app():
    '''
    Function: Exit the App
    '''
    text = 'Closing App'
    show_subtitle(text)

def app_header():
    '''
    Function: Show the app header
    '''

    print("""
    ╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━━━┳╮
    ┃╭━━╯╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃╭━━┫┃
    ┃╰━━┳╮╭┳━━┳━┳━━┳━━┳━━╮┃╰━━┫┃╭━━┳╮╭┳━━┳━╮
    ┃╭━━┻╋╋┫╭╮┃╭┫┃━┫━━┫━━┫┃╭━━┫┃┃╭╮┃╰╯┃╭╮┃╭╯
    ┃╰━━┳╋╋┫╰╯┃┃┃┃━╋━━┣━━┃┃┃╱╱┃╰┫╭╮┣╮╭┫╰╯┃┃
    ╰━━━┻╯╰┫╭━┻╯╰━━┻━━┻━━╯╰╯╱╱╰━┻╯╰╯╰╯╰━━┻╯
    ╱╱╱╱╱╱╱┃┃
    ╱╱╱╱╱╱╱╰╯
    """)

def invalid_app_option():
    '''
    Function: Inform the user who entered the wrong option.
    '''

    print("\n$ Invalid Option! Choose between 1 to 4. ")
    print("""
        ░█▀▀█ █  █ █▀▀█ █▀▀█ █▀▀ █▀▀ 　 █▀▀▄ █▀▀ ▀▀█▀▀ █   █ █▀▀ █▀▀ █▀▀▄ 　 ▄█  　 ▀▀█▀▀ █▀▀█ 　  █▀█    
        ░█    █▀▀█ █  █ █  █ ▀▀█ █▀▀ 　 █▀▀▄ █▀▀   █   █▄█▄█ █▀▀ █▀▀ █  █ 　  █  　   █   █  █ 　 █▄▄█▄  ▄ 
        ░█▄▄█ ▀  ▀ ▀▀▀▀ ▀▀▀▀ ▀▀▀ ▀▀▀ 　 ▀▀▀  ▀▀▀   ▀    ▀ ▀  ▀▀▀ ▀▀▀ ▀  ▀ 　 ▄█▄ 　   ▀   ▀▀▀▀ 　    █  ░█
                  """)
    return_to_main_menu()

def register_new_restaurant():
    '''
    Function: Allow the user register a new restaurant in the database
    '''
    os.system('cls')
    print("""ℝ𝕖𝕘𝕚𝕤𝕥𝕣𝕒𝕥𝕚𝕠𝕟 𝕠𝕗 𝕟𝕖𝕨 𝕣𝕖𝕤𝕥𝕒𝕦𝕣𝕒𝕟𝕥𝕤
    """)
    restaurant_name     = input("# Enter the name of the restaurant you want to register: ")
    restaurant_category = input(f"# Enter the name of the {restaurant_name} restaurant category: ")

    __tmp_dict = {}
    __tmp_dict[__key_name]     = restaurant_name
    __tmp_dict[__key_category] = restaurant_category
    __tmp_dict[__key_active]   = False

    __restaurant.append(__tmp_dict)



    print(f'The {restaurant_name} restaurant has been sucessfully registered.')

    return_to_main_menu()

def show_list_restaurant(flag_clear_screen = True, flag_return_to_main_menu = True):
    '''
    Function  : Show all the restaurant registered in the database
    Parameters:
        - flag_clear_screen = True, used to enable o command clear screen in the terminal.
          Use True to enable or False to disable the command. (Command performed is cls)
        - flag_return_to_main_menu = True, used to enable the feature of main menu return.
          Use True to enable or False to disable the feature.
    '''
    if (flag_clear_screen):
        os.system('cls')

    print("""𝕃𝕚𝕤𝕥 𝕠𝕗 𝕣𝕖𝕘𝕚𝕤𝕥𝕖𝕣𝕖𝕕 𝕣𝕖𝕤𝕥𝕒𝕦𝕣𝕒𝕟𝕥𝕤""")
    print(f'  {'RESTAURANT NAME'.ljust(15)} # {'CATEGORY'.ljust(15)} # {'STATE'}')
    for i in __restaurant:
        try:
            name     = i['name']
            category = i['category']
            active   = i['active']
            print(f'* {name.ljust(15)} | {category.ljust(15)} | actived' if active
                  else f'* {name.ljust(15)} | {category.ljust(15)} | deactived')
        except:
            text = "@ Data list error!"
            show_subtitle(text)

    if(flag_return_to_main_menu):
        return_to_main_menu()

def switch_restaurant_state():
    '''
    Function: Allow the user to switch the restaurant's status to active or deactivated.
    '''
    os.system('cls')
    print("""ℂ𝕙𝕒𝕟𝕘𝕖 𝕥𝕙𝕖 𝕣𝕖𝕤𝕥𝕒𝕦𝕣𝕒𝕟𝕥❜𝕤 𝕤𝕥𝕒𝕥𝕦𝕤 𝕥𝕠 𝕒𝕔𝕥𝕚𝕧𝕖 𝕠𝕣 𝕕𝕖𝕒𝕔𝕥𝕚𝕧𝕒𝕥𝕖𝕕""")
    show_list_restaurant(False,False)

    flag_restaurant_found = False
    restaurant_name = input("\n# Enter the name of the restaurant you want to activate or deactivate: ")

    for i in __restaurant:
        if(i[__key_name] == restaurant_name):
            flag_restaurant_found = True
            i[__key_active] = not i[__key_active]
            print(f'>> {i[__key_name]} Restaurant Status Changed To ACTIVATE.' if i[__key_active]
                  else f'>> {i[__key_name]} Restaurant Status Changed To DEACTIVATE.')
            print(f'   {'RESTAURANT NAME'.ljust(15)} # {'CATEGORY'.ljust(15)} # {'STATE'}')
            print(f'   {i[__key_name].ljust(15)} | {i[__key_category].ljust(15)} | actived' if i[__key_active]
                  else f'>> {i[__key_name].ljust(15)} | {i[__key_category].ljust(15)} | deactived')
            break

    if(not flag_restaurant_found):
        print("""# ℝ𝕖𝕤𝕥𝕒𝕦𝕣𝕒𝕟𝕥 𝕟𝕠𝕥 𝕗𝕠𝕦𝕟𝕕❕""")

    return_to_main_menu()

def app_option():
    '''
    Function: Show user interaction options.
    '''
    print("1. Restaurant Registration")
    print("2. List Restaurant")
    print("3. Activate Restaurant")
    print("""4. Exit    
          """)
    try:
        option_selected = int(input("# Select an option: "))

        print('@ You selected the option {}'.format(option_selected))

        match option_selected:
            case 1:
                register_new_restaurant()
            case 2:
                show_list_restaurant()
            case 3:
                switch_restaurant_state()
            case 4:
                closing_app()
            case _:
                invalid_app_option()

        # if (option_selected == 1):
        #     print('Add new restaurant')
        # elif (option_selected == 2):
        #     print('List restaurant')
        # elif (option_selected == 3):
        #     print('Activate restaurant')
        # elif (option_selected == 4):
        #     closing_app()
        # else:
        #     print("\n$ Invalid Option! Choose between 1 to 4. ")
        #     print("""
        #     ░█▀▀█ █  █ █▀▀█ █▀▀█ █▀▀ █▀▀ 　 █▀▀▄ █▀▀ ▀▀█▀▀ █   █ █▀▀ █▀▀ █▀▀▄ 　 ▄█  　 ▀▀█▀▀ █▀▀█ 　  █▀█
        #     ░█    █▀▀█ █  █ █  █ ▀▀█ █▀▀ 　 █▀▀▄ █▀▀   █   █▄█▄█ █▀▀ █▀▀ █  █ 　  █  　   █   █  █ 　 █▄▄█▄  ▄
        #     ░█▄▄█ ▀  ▀ ▀▀▀▀ ▀▀▀▀ ▀▀▀ ▀▀▀ 　 ▀▀▀  ▀▀▀   ▀    ▀ ▀  ▀▀▀ ▀▀▀ ▀  ▀ 　 ▄█▄ 　   ▀   ▀▀▀▀ 　    █  ░█
        #               """)

    except:
        print("@ Your entered not valid option!")
        print("@ Please enter with value between 1 to 4.")
        # input("# Press enter to return for main menu")
        return_to_main_menu()
def main():
    app_header()
    app_option()

if(__name__ == '__main__'):
    main()
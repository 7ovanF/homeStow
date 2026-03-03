DAWG_TYPES = {
    "boi": ["he", "him", "his"],
    "girl": ["she", "her", "her"],
    "squid": ["The Fine Octa-legged Creature", "The Great", "Our Lord's"]
    }

dawgs = {}

class Dawg:
    __good = True

    def __init__(dawg, name, dawg_type):
        # attributes
        dawg.__name = name
        dawg.__type = dawg_type

        # statuses
        dawg.__hungry = True
        dawg.__bored = True

    def __str__(dawg):
        return dawg.__name

    def feed(dawg):
        dawg.__hungry = False
        return f'fed {dawg.__name}'

    def play(dawg):
        dawg.__bored = False
        return f'played with {dawg.__name}'

    def get_status(dawg):
        status = []
        status += ["hungry" if dawg.__hungry else "full"]
        status += ["bored" if dawg.__bored else "happy"]
        return status
    
    def check_good(dawg):
        if dawg.__type != 'squid':
            if dawg.__good:
                good = "\033[1myes\033[0m"
            else:
                dawg.__good = True
                good = "\033[1myes\033[0m"
        else:
            good = ""
        return good
    
    def leave(dawg):
        if dawg.__type != "squid":
            if not dawg.__hungry and not dawg.__bored:
                print(f'{dawg.__name} barks bye bye at you delightedly!')
            else:
                print(f'{dawg.__name} is sad! please come back soon!')
        else:
            if not dawg.__hungry and not dawg.__bored:
                print(f'{dawg.__name} is pleased.')
            else:
                print()
                print(f'{dawg.__name} is not pleased. Thy end is now.')
                death()
        print()


def create_dawg():
    dawg_conceived = False
    while not dawg_conceived:
        dawg_type = input('boi/girl?\n> ')
        
        if dawg_type in DAWG_TYPES:
            pass
        else:
            print('not a supported dawg type... yet!')
            continue
        
        name = input(f'{DAWG_TYPES[dawg_type][2]} name?\n> ')

        dawg_conceived = True
    
    dawgs[name] = Dawg(name, dawg_type)

    print()
    print(20 * '-')
    print('The dawg has awakened.')
    print(f'say hi to {name}!')
    print(20 * '-')
    print()

def choose_dawg():
    if not dawgs:
        print('ah...no dawgs yet')
        return None

    while True:
        print("ur dawgs:")
        for dawg_name in dawgs:
            print(f"- {dawg_name}")
        
        chosen_dawg = input("which dawg will you choose?\n> ")
        
        if chosen_dawg in dawgs:
            return dawgs[chosen_dawg]
        else:
            print('no dawg with that name\n')


def inspect_dawg(dawg):
    with_dawg = True

    while with_dawg:
        print(f"dawg: {dawg.get_name()}")
        print(f"type: {dawg.get_type()}")

        status = dawg.get_status()
        print(f"status: {", ".join(status)}")

        good = dawg.check_good()
        print(f"is a good {dawg.get_type()}? {good}")
        
        print("- feed")
        print("- play")
        print("- leave")

        action = input("what will you do with the dawg?\n> ")
        if action == 'feed':
            result = dawg.feed()
            print(result)
        elif action == 'play':
            result = dawg.play()
            print(result)
        elif action == 'leave':
            dawg.leave()
            with_dawg = False
        else:
            print('the dawg is confused at ur action.\n')


def death():
    print('\ndead')
    exit()

def main():
    print()
    print(40 * "=")
    print(f"{" WHAT THE DAWG DOIN ":*^40}")
    print(40 * "=")
    print()

    woof = True

    while woof:
        print("welcome to the dawg interface")
        print("1. create new dawg")
        print("2. check out dawg")
        print("3. exit")
        print()

        try:
            choice = int(input("what will you do? "))
        except ValueError:
            print('invalid choice fam...\n')
            continue

        match choice:
            case 1:
                create_dawg()
            case 2:
                selected_dawg = choose_dawg()
                if selected_dawg:
                    inspect_dawg(selected_dawg)
            case 3:
                print('\nbye bye')
                woof = False
            case _:
                print('invalid choice fam...\n')
    

if __name__ == "__main__":
    main()
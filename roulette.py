check_n = {'0' : [[],''], 
        '99' : [[],''], 
        '1' : [[],''],
        '2' : [[],''], 
        '3' : [[],''], 
        '4' : [[],''], 
        '5' : [[],''], 
        '6' : [[],''], 
        '7' : [[],''], 
        '8' : [[],''], 
        '9' : [[],''],
        '10' : [[],''], 
        '11' : [[],''], 
        '12' : [[],''],
        '13' : [[],''], 
        '14' : [[],''], 
        '15' : [[],''], 
        '16' : [[],''], 
        '17' : [[],''], 
        '18' : [[],''], 
        '19' : [[],''], 
        '20' : [[],''],
        '21' : [[],''], 
        '22' : [[],''], 
        '23' : [[],''],
        '24' : [[],''], 
        '25' : [[],''], 
        '26' : [[],''], 
        '27' : [[],''], 
        '28' : [[],''], 
        '29' : [[],''], 
        '30' : [[],''], 
        '31' : [[],''],
        '32' : [[],''], 
        '33' : [[],''], 
        '34' : [[],''],
        '35' : [[],''], 
        '36' : [[],'']}
casino = {'Odd' : [x for x in range(1, 37) if x % 2 != 0], 
    'Even' : [x for x in range(1, 37) if x % 2 == 0],
    '1st12' : [x for x in range(1, 13)], 
    '2nd12' : [x for x in range(13, 25)], 
    '3rd12' : [x for x in range(25, 37)], 
    'Black' : [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35], 
    'Red' : [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36], 
    'Line 1' : [x for x in range(3, 37, 3)], 
    'Line 2' : [x for x in range(2, 37, 3)], 
    'Line 3' : [x for x in range(1, 37, 3)], 
    '1to18' : [x for x in range(1, 19)], 
    '19to36' : [x for x in range(19, 37)]}
check_areas = {'Odd' : [[],''], 
        'Even' : [[],''],
        '1st12' : [[],''], 
        '2nd12' : [[],''], 
        '3rd12' : [[],''], 
        'Black' : [[],''], 
        'Red' : [[],''], 
        'Line 1' : [[],''], 
        'Line 2' : [[],''], 
        'Line 3' : [[],''],
        '1to18' : [[],''], 
        '19to36' : [[],'']}

for key in casino:
    print(f"{key}: {casino[key]}")

count = 0
register = []

print("\n")

class colors: 
    reset='\033[0m'
    bold='\033[01m'
    disable='\033[02m'
    underline='\033[04m'
    reverse='\033[07m'
    strikethrough='\033[09m'
    invisible='\033[08m'
    class fg: 
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'
    class bg: 
        black='\033[40m'
        red='\033[41m'
        green='\033[42m'
        orange='\033[43m'
        blue='\033[44m'
        purple='\033[45m'
        cyan='\033[46m'
        lightgrey='\033[47m'


print(f"""
{colors.bg.green}                                   {colors.reset}
{colors.bg.green}   {colors.reset}{colors.bg.lightgrey}{colors.fg.black}0{colors.reset}{colors.bg.black}3{colors.bg.red}6{colors.bg.black}9{colors.bg.red}12{colors.bg.black}15{colors.bg.red}18{colors.bg.black}21{colors.bg.red}24{colors.bg.black}27{colors.bg.red}30{colors.bg.black}33{colors.bg.red}36{colors.reset}{colors.bg.green} Line 1   {colors.reset}
{colors.bg.green}   {colors.reset}{colors.bg.lightgrey}{colors.fg.black}0{colors.reset}{colors.bg.red}2{colors.bg.black}5{colors.bg.red}8{colors.bg.black}11{colors.bg.red}14{colors.bg.black}17{colors.bg.red}20{colors.bg.black}23{colors.bg.red}26{colors.bg.black}29{colors.bg.red}32{colors.bg.black}35{colors.reset}{colors.bg.green} Line 2   {colors.reset}
{colors.bg.green}   {colors.reset}{colors.bg.lightgrey}{colors.fg.black}0{colors.reset}{colors.bg.black}1{colors.bg.red}4{colors.bg.black}7{colors.bg.red}10{colors.bg.black}13{colors.bg.red}16{colors.bg.black}19{colors.bg.red}22{colors.bg.black}25{colors.bg.red}28{colors.bg.black}31{colors.bg.red}34{colors.reset}{colors.bg.green} Line 3   {colors.reset}
{colors.bg.green}    1st12  2nd12  3rd12            {colors.reset}
{colors.bg.green}      1to18    18to36              {colors.reset}
""")

print("\n")

while True:

    x = int(input(f"What is on the roulette? "))
    register.append(x)
    
    print("\n")

    predictor_n = {}
    predictor_areas = {}

    for key in check_n:
        if x == int(key):
            check_n[key][0].append(True)
            check_n[key][1] = ""
        else:
            check_n[key][0].append(False)
            check_n[key][1] += "*"

    for key in check_areas:
        if x in casino[key]:
            check_areas[key][0].append(True)
            check_areas[key][1] = ""
        else:
            check_areas[key][0].append(False)
            check_areas[key][1] += "*"
    
    for key in check_n:
        predictor_n[key] = check_n[key][1]
    
    for key in check_areas:
        predictor_areas[key] = check_areas[key][1]

    predictor_n = sorted(((value, key) for (key, value) in predictor_n.items()), reverse = True)
    
    predictor_areas = sorted(((value, key) for (key, value) in predictor_areas.items()), reverse = True)
    
    count +=1
    print(f"Turns: {count}")
    print(register)

    print("\n")
    
    print("The following areas are predicted for the next turn: ")

    for i in range(0, 5):
        if 0 < len(predictor_areas[i][0]) <= 3:
            print(f"{predictor_areas[i][1]}: {colors.fg.red}{predictor_areas[i][0]}{colors.reset}")
        if 3 < len(predictor_areas[i][0]) <= 5:
            print(f"{predictor_areas[i][1]}: {colors.fg.orange}{predictor_areas[i][0]}{colors.reset}")
        if 5 < len(predictor_areas[i][0]):
            print(f"{predictor_areas[i][1]}: {colors.fg.green}{predictor_areas[i][0]}{colors.reset}")

    print("\n")

    print("The following numbers are predicted for the next turn: ")

    for i in range(0, 5):
        if 0 < len(predictor_n[i][0]) <= 18:
            print(f"{predictor_n[i][1]}: {colors.fg.red}{predictor_n[i][0]}{colors.reset} ({len(predictor_n[i][0])})")
        if 18 < len(predictor_n[i][0]) <= 36:
            print(f"{predictor_n[i][1]}: {colors.fg.orange}{predictor_n[i][0]}{colors.reset} ({len(predictor_n[i][0])})")
        if 36 < len(predictor_n[i][0]):
            print(f"{predictor_n[i][1]}: {colors.fg.green}{predictor_n[i][0]}{colors.reset} ({len(predictor_n[i][0])})")
    
    print("\n")



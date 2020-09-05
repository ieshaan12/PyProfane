censorSymbols = ['#','%','$','!','&']
censorSymbolsLength = 5

lettersToRemove = {'a', 'e', 'i', 'o', 'u', 'y', 'h', 'w'}
letterMappings = {'b': 1,'f': 1,'p': 1,'v': 1,'c': 2,'g': 2,'j': 2,'k': 2,'q': 2,'s': 2,'x': 2,'z': 2,'d': 3,'t': 3,'l': 4,'m': 5,'n': 5,'r': 6}

profaneWordSoundex = {'anal': 'A540', 'anus': 'A520', 'arse': 'A620', 'ass': 'A220', 'ballsack': 'B422', 'balls': 'B422', 
'bastard': 'B236', 'bitch': 'B320', 'biatch': 'B320', 'bloody': 'B430', 'blowjob': 'B421', 'bollock': 'B422', 'bollok': 'B422', 
'boner': 'B560', 'boob': 'B100', 'bugger': 'B266', 'bum': 'B500', 'bullcrap': 'B426', 'bullshit': 'B423', 'butt': 'B330', 
'buttplug': 'B314', 'clitoris': 'C436', 'clit': 'C430', 'cock': 'C220', 'coon': 'C500', 'crap': 'C610', 'cunt': 'C530', 
'damn': 'D550', 'dick': 'D220', 'dildo': 'D430', 'dyke': 'D200', 'fag': 'F200', 'feck': 'F220', 'fellate': 'F433', 'fellatio': 'F433', 
'felching': 'F425', 'fuck': 'F220', 'fuckface': 'F212', 'fudgepacker': 'F321', 'flange': 'F452', 'Goddamn': 'G355', 'hell': 'H440', 
'homo': 'H500', 'jerk': 'J620', 'jizz': 'J220', 'knobend': 'K515', 'labia': 'L100', 'lmao': 'L500', 'lmfao': 'L510', 'muff': 'M110', 
'nigger': 'N266', 'nigga': 'N220', 'penis': 'P520', 'piss': 'P220', 'poop': 'P100', 'prick': 'P622', 'pussy': 'P220', 
'scrotum': 'S263', 'sex': 'S200', 'shit': 'S300', 'shithead': 'S330', 'slut': 'S430', 'slutty': 'S433', 'wanker': 'W526', 
'smegma': 'S525', 'spunk': 'S152', 'tosser': 'T266', 'turd': 'T630', 'twat': 'T300', 'cumslut': 'C524', 'vagina': 'V250', 
'wank': 'W520', 'whore': 'W600', 'cuntfucker': 'C531', 'shag': 'S200', 'dickweed': 'D233', 'asswhore': 'A266', 'titjob': 'T321', 
'gangbang': 'G521', 'cuntlick': 'C534', 'horseshit': 'H623', 'dickless': 'D242', 'dammit': 'D533', 'negro': 'N260', 'negroes': 'N262', 
'motherfucking': 'M361', 'cockblock': 'C214', 'asspacker': 'A212', 'orgy': 'O620', 'assfucker': 'A212', 'balllicker': 'B426', 
'cocklover': 'C241', 'cocksucker': 'C262', 'dicksucker': 'D262', 'asshat': 'A233', 'meatbeatter': 'M313', 'camslut': 'C524', 
'fuckbag': 'F212', 'mothafucka': 'M312', 'pussylover': 'P241'}

profaneWords = {'anal', 'anus', 'arse', 'ass', 'ballsack', 'balls', 'bastard', 'bitch', 'biatch', 'bloody', 'blowjob', 'bollock', 
'bollok', 'boner', 'boob', 'bugger', 'bum', 'bullcrap', 'bullshit', 'butt', 'buttplug', 'clitoris', 'clit', 'cock', 'coon', 'crap', 
'cunt', 'damn', 'dick', 'dildo', 'dyke', 'fag', 'feck', 'fellate', 'fellatio', 'felching', 'fuck', 'fuckface', 'fudgepacker', 'flange',
'Goddamn', 'hell', 'homo', 'jerk', 'jizz', 'knobend', 'labia', 'lmao', 'lmfao', 'muff', 'nigger', 'nigga', 'penis', 'piss', 'poop', 
'prick', 'pussy', 'scrotum', 'sex', 'shit', 'shithead', 'slut', 'slutty', 'wanker', 'smegma', 'spunk', 'tosser', 'turd', 'twat', 
'cumslut', 'vagina', 'wank', 'whore', 'cuntfucker', 'shag', 'dickweed', 'asswhore', 'titjob', 'gangbang', 'cuntlick', 'horseshit', 
'dickless', 'dammit', 'negro', 'negroes', 'motherfucking', 'cockblock', 'asspacker', 'orgy', 'assfucker', 'balllicker', 'cocklover',
'cocksucker', 'dicksucker', 'asshat', 'meatbeatter', 'camslut', 'fuckbag', 'mothafucka', 'pussylover'}

profaneWordsSoundexValues = {'A540', 'A520', 'A620', 'A220', 'B422', 'B422', 'B236', 'B320', 'B320', 'B430', 'B421', 'B422', 'B422', 
'B560', 'B100', 'B266', 'B500', 'B426', 'B423', 'B330', 'B314', 'C436', 'C430', 'C220', 'C500', 'C610', 'C530', 'D550', 'D220', 
'D430', 'D200', 'F200', 'F220', 'F433', 'F433', 'F425', 'F220', 'F212', 'F321', 'F452', 'G355', 'H440', 'H500', 'J620', 'J220', 
'K515', 'L100', 'L500', 'L510', 'M110', 'N266', 'N220', 'P520', 'P220', 'P100', 'P622', 'P220', 'S263', 'S200', 'S300', 'S330', 
'S430', 'S433', 'W526', 'S525', 'S152', 'T266', 'T630', 'T300', 'C524', 'V250', 'W520', 'W600', 'C531', 'S200', 'D233', 'A266', 
'T321', 'G521', 'C534', 'H623', 'D242', 'D533', 'N260', 'N262', 'M361', 'C214', 'A212', 'O620', 'A212', 'B426', 'C241', 'C262', 
'D262', 'A233', 'M313', 'C524', 'F212', 'M312', 'P241'}
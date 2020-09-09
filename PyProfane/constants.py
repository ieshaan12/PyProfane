censorSymbols = ['#','%','$','!','&']
censorSymbolsLength = 5

lettersToRemove = {'a', 'e', 'i', 'o', 'u', 'y', 'h', 'w'}
letterMappings = {'b': 1,'f': 1,'p': 1,'v': 1,'c': 2,'g': 2,'j': 2,'k': 2,'q': 2,'s': 2,'x': 2,'z': 2,'d': 3,'t': 3,'l': 4,'m': 5,'n': 5,'r': 6}

profaneWordSoundex = {'anal': 'A540', 'anus': 'A520', 'arse': 'A620', 'ass': 'A220', 'ballsack': 'B422', 'balls': 'B422', 
'bastard': 'B236', 'bitch': 'B320', 'biatch': 'B320', 'bloody': 'B430', 'blowjob': 'B421', 'bollock': 'B422', 'bollok': 'B422', 
'boner': 'B560', 'boob': 'B100', 'bugger': 'B266', 'bum': 'B500', 'bullcrap': 'B426', 'bullshit': 'B423', 'butt': 'B330', 
'buttplug': 'B314', 'clitoris': 'C436', 'clit': 'C430', 'cock': 'C220', 'coon': 'C500', 'crap': 'C610', 'cunt': 'C530', 
'damn': 'D550', 'dick': 'D220', 'dildo': 'D430', 'dyke': 'D200', 'fag': 'F200', 'feck': 'F220', 'fellate': 'F433', 
'fellatio': 'F433', 'felching': 'F425', 'fuck': 'F220', 'fuckface': 'F212', 'fudgepacker': 'F321', 'fucker': 'F266', 
'fucking': 'F252', 'flange': 'F452', 'Goddamn': 'G355', 'hell': 'H440', 'homo': 'H500', 'jerk': 'J620', 'jizz': 'J220', 
'knobend': 'K515', 'labia': 'L100', 'muff': 'M110', 'nigger': 'N266', 'nigga': 'N220', 'piss': 'P220', 'poop': 'P100', 
'prick': 'P622', 'pussy': 'P220', 'scrotum': 'S263', 'sex': 'S200', 'shit': 'S300', 'shithead': 'S330', 'slut': 'S430', 
'slutty': 'S433', 'wanker': 'W526', 'smegma': 'S525', 'spunk': 'S152', 'tosser': 'T266', 'turd': 'T630', 'twat': 'T300', 
'cumslut': 'C524', 'vagina': 'V250', 'wank': 'W520', 'whore': 'W600', 'cuntfucker': 'C531', 'shag': 'S200', 'dickweed': 'D233', 
'asswhore': 'A266', 'titjob': 'T321', 'gangbang': 'G521', 'cuntlick': 'C534', 'horseshit': 'H623', 'dickless': 'D242', 'dammit': 
'D533', 'negro': 'N260', 'negroes': 'N262', 'motherfucking': 'M361', 'cockblock': 'C214', 'asspacker': 'A212', 'orgy': 'O620',
'assfucker': 'A212', 'balllicker': 'B426', 'cocklover': 'C241', 'cocksucker': 'C262', 'dicksucker': 'D262', 'asshat': 'A233', 
'meatbeater': 'M313', 'camslut': 'C524', 'fuckbag': 'F212', 'mothafucka': 'M312', 'pussylover': 'P241'}

profaneWordsSoundexValues = {'B426', 'D200', 'H500', 'B320', 'A233', 'J220', 'F200', 'S525', 'C524', 'A540', 'K515', 'S200', 'D550', 
'F452', 'L100', 'N266', 'W526', 'T266', 'D262', 'F252', 'P100', 'T321', 'S430', 'C534', 'T630', 'W520', 'D533', 'M361', 'W600', 
'C214', 'A520', 'D430', 'D233', 'D242', 'B100', 'B236', 'O620', 'B430', 'B560', 'N260', 'C241', 'B423', 'J620', 'S300', 'G355', 
'S433', 'C262', 'T300', 'D220', 'F220', 'G521', 'B314', 'M312', 'S152', 'H623', 'C430', 'V250', 'C530', 'F321', 'C610', 'M313', 
'P220', 'A266', 'F266', 'F425', 'B422', 'A212', 'S263', 'B330', 'B266', 'C500', 'A220', 'F433', 'B500', 'A620', 'P241', 'F212', 
'M110', 'P622', 'N262', 'N220', 'C531', 'C220', 'H440', 'S330', 'B421', 'C436'}

profaneWords = {'cuntfucker', 'assfucker', 'nigga', 'fuckface', 'ballsack', 'cuntlick', 'negro', 'dickweed', 'camslut', 'dyke', 
'biatch', 'pussy', 'boner', 'Goddamn', 'clitoris', 'flange', 'muff', 'dickless', 'twat', 'knobend', 'negroes', 'coon', 'labia', 
'feck', 'balllicker', 'smegma', 'gangbang', 'dicksucker', 'slutty', 'pussylover', 'butt', 'bugger', 'boob', 'bastard', 'whore', 
'anus', 'horseshit', 'bitch', 'fellate', 'fuck', 'bum', 'mothafucka', 'bollock', 'asspacker', 'sex', 'bloody', 'prick', 'blowjob', 
'piss', 'fudgepacker', 'meatbeater', 'vagina', 'dick', 'buttplug', 'dammit', 'shit', 'crap', 'clit', 'felching', 'fuckbag', 'dildo', 
'wank', 'fucking', 'wanker', 'cocklover', 'ass', 'homo', 'damn', 'turd', 'fellatio', 'asshat', 'fucker', 'cocksucker', 'bullcrap', 
'jerk', 'tosser', 'cunt', 'nigger', 'shag', 'titjob', 'slut', 'cumslut', 'motherfucking', 'shithead', 'cockblock', 'scrotum', 
'bollok', 'spunk', 'orgy', 'jizz', 'hell', 'anal', 'poop', 'arse', 'cock', 'balls', 'asswhore', 'fag', 'bullshit'}
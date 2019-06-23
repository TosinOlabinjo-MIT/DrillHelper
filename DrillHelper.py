import math

##############################
# Builders
##############################


def build_PlainSpeech(body):
    speech = {}
    speech['type'] = 'PlainText'
    speech['text'] = body
    return speech


def build_response(message, session_attributes={}):
    response = {}
    response['version'] = '1.0'
    response['sessionAttributes'] = session_attributes
    response['response'] = message
    return response


def build_SimpleCard(title, body):
    card = {}
    card['type'] = 'Simple'
    card['title'] = title
    card['content'] = body
    return card


##############################
# Responses
##############################


def conversation(title, body, session_attributes):
    speechlet = {}
    speechlet['outputSpeech'] = build_PlainSpeech(body)
    speechlet['card'] = build_SimpleCard(title, body)
    speechlet['shouldEndSession'] = False
    return build_response(speechlet, session_attributes=session_attributes)

def convo_and_reprompt(title, body, reprompt, session_attributes):
    speechlet = {}
    speechlet['outputSpeech'] = build_PlainSpeech(body)
    speechlet['reprompt'] = {'outputSpeech' : build_PlainSpeech(reprompt)}
    speechlet['card'] = build_SimpleCard(title, body)
    speechlet['shouldEndSession'] = False
    return build_response(speechlet, session_attributes=session_attributes)

def statement(title, body):
    speechlet = {}
    speechlet['outputSpeech'] = build_PlainSpeech(body)
    speechlet['card'] = build_SimpleCard(title, body)
    speechlet['shouldEndSession'] = True
    return build_response(speechlet)


def continue_dialog():
    message = {}
    message['shouldEndSession'] = False
    message['directives'] = [{'type': 'Dialog.Delegate'}]
    return build_response(message)


##############################
# Charts
##############################


drill_decimal_eq = {"80":0.0135,"79":0.0145,"1/64":0.0156,"78":0.016,"77":0.018,"76":0.02,"75":0.021,"74":0.0225,"73":0.024,"72":0.025,"71":0.026,"70":0.028,"69":0.0292,"68":0.031,"1/32":0.0312,"67":0.032,"66":0.033,"65":0.035,"64":0.036,"63":0.037,"62":0.038,"61":0.039,"60":0.04,"59":0.041,"58":0.042,"57":0.043,"56":0.0465,"3/64":0.0469,"55":0.052,"54":0.055,"53":0.0595,"0.0625":0.0625,"52":0.0635,"51":0.067,"50":0.07,"49":0.073,"48":0.076,"5/64":0.0781,"47":0.0785,"46":0.081,"45":0.082,"44":0.086,"43":0.089,"42":0.0935,"3/32":0.0938,"41":0.096,"40":0.098,"39":0.0995,"38":0.1015,"37":0.104,"36":0.1065,"7/64":0.1094,"35":0.11,"34":0.111,"33":0.113,"32":0.116,"31":0.12,"0.125":0.125,"30":0.1285,"29":0.136,"28":0.1405,"9/64":0.1406,"27":0.144,"26":0.147,"25":0.1495,"24":0.152,"23":0.154,"5/32":0.1562,"22":0.157,"21":0.159,"20":0.161,"19":0.166,"18":0.1695,"11/64":0.1719,"17":0.173,"16":0.177,"15":0.18,"14":0.182,"13":0.185,"0.1875":0.1875,"12":0.189,"11":0.191,"10":0.1935,"9":0.196,"8":0.199,"7":0.201,"13/64":0.2031,"6":0.204,"5":0.2055,"4":0.209,"3":0.213,"7/32":0.2188,"2":0.221,"1":0.228,"A":0.234,"15/64":0.2344,"B":0.238,"C":0.242,"D":0.246,"0.25":0.25,"F":0.257,"G":0.261,"17/64":0.2656,"H":0.266,"I":0.272,"J":0.277,"K":0.281,"9/32":0.2812,"L":0.29,"M":0.295,"19/64":0.2969,"N":0.302,"0.3125":0.3125,"O":0.316,"P":0.323,"21/64 ":0.3281,"Q":0.332,"R":0.339,"11/32 ":0.3438,"S":0.348,"T":0.358,"23/64 ":0.3594,"U":0.368,"0.375":0.375,"V":0.377,"W":0.386,"25/64 ":0.3906,"X":0.397,"Y":0.404,"13/32 ":0.4063,"Z":0.413,"27/64 ":0.4219,"0.4375":0.4375,"29/64":0.4531,"15/32":0.4688,"31/64":0.4844,"0.5":0.5,"33/64":0.5156,"17/32":0.5312,"35/64":0.5469,"0.5625":0.5625,"37/64":0.5781,"19/32":0.5938,"39/64":0.6094,"0.625":0.625,"41/64":0.6406,"21/32":0.6562,"43/64":0.6719,"0.6875":0.6875,"45/64":0.7031,"23/32":0.7188,"47/64":0.7344,"0.75":0.75,"49/64 ":0.7656,"25/32 ":0.7813,"51/64":0.7969,"13/16":0.8125,"53/64":0.8281,"27/32":0.8438,"55/64":0.8594,"0.875":0.875,"57/64":0.8906,"29/32":0.9062,"59/64":0.9219,"15/16":0.9375,"61/64":0.9531,"31/32":0.9688,"63/64":0.9844}

material_chart = {"stainless steel":50,"cast iron":80,"brass":160,"bronze":120,"aluminum":350,"steel":60,"plastic":270}

simple_tap_chart = {"0": {"aluminum": "3/64", "brass": "3/64", "plastic": "3/64", "steel": "55", "stainless steel": "55", "iron": "55"},

                    "1": {"aluminum": "53", "brass": "53", "plastic": "53", "steel": "0.0625", "stainless steel": "0.0625", "iron": "0.0625"},

                    "2": {"aluminum": "50", "brass": "50", "plastic": "50", "steel": "49", "stainless steel": "49", "iron": "49"},

                    "3": {"aluminum": "47", "brass": "47", "plastic": "47", "steel": "44", "stainless steel": "44", "iron": "44"},

                    "4": {"aluminum": "43", "brass": "43", "plastic": "43", "steel": "41", "stainless steel": "41", "iron": "41"},

                    "5": {"aluminum": "38", "brass": "38", "plastic": "38", "steel": "7/64", "stainless steel": "7/64", "iron": "7/64"},

                    "6":  {"aluminum": "36", "brass": "36", "plastic": "36", "steel": "32", "stainless steel": "32", "iron": "32"},

                    "8":  {"aluminum": "29", "brass": "29", "plastic": "29", "steel": "27", "stainless steel": "27", "iron": "27"},

                    "10":  {"aluminum": "25", "brass": "25", "plastic": "25", "steel": "20", "stainless steel": "20", "iron": "20"},

                    "12":  {"aluminum": "16", "brass": "16", "plastic": "16", "steel": "12", "stainless steel": "12", "iron": "12"}
                    }

#Click to expand
tap_chart ={"0": {"80": {"aluminum": "3/64", "brass": "3/64", "plastic": "3/64", "steel": "55", "stainless steel": "55", "iron": "55"}},"1": {"64": {"aluminum": "53", "brass": "53", "plastic": "53", "steel": "1/16", "stainless steel": "1/16", "iron": "1/16"},"72": {"aluminum": "53", "brass": "53", "plastic": "53", "steel": "52", "stainless steel": "52", "iron": "52"}},"2": {"56": {"aluminum": "50", "brass": "50", "plastic": "50", "steel": "49", "stainless steel": "49", "iron": "49"},"64": {"aluminum": "50", "brass": "50", "plastic": "50", "steel": "48", "stainless steel": "48", "iron": "48"}},"3": {"48": {"aluminum": "47", "brass": "47", "plastic": "47", "steel": "44", "stainless steel": "44", "iron": "44"},"56": {"aluminum": "45", "brass": "45", "plastic": "45", "steel": "43", "stainless steel": "43", "iron": "43"}},"4": {"40": {"aluminum": "43", "brass": "43", "plastic": "43", "steel": "41", "stainless steel": "41", "iron": "41"},"48": {"aluminum": "42", "brass": "42", "plastic": "42", "steel": "40", "stainless steel": "40", "iron": "40"}},"5": {"40": {"aluminum": "38", "brass": "38", "plastic": "38", "steel": "7/64", "stainless steel": "7/64", "iron": "7/64"},"44": {"aluminum": "37", "brass": "37", "plastic": "37", "steel": "35", "stainless steel": "35", "iron": "35"}},"6": {"32": {"aluminum": "36", "brass": "36", "plastic": "36", "steel": "32", "stainless steel": "32", "iron": "32"},"40": {"aluminum": "33", "brass": "33", "plastic": "33", "steel": "31", "stainless steel": "31", "iron": "31"}},"8": {"32": {"aluminum": "29", "brass": "29", "plastic": "29", "steel": "27", "stainless steel": "27", "iron": "27"},"36": {"aluminum": "29", "brass": "29", "plastic": "29", "steel": "26", "stainless steel": "26", "iron": "26"}},"10": {"24": {"aluminum": "25", "brass": "25", "plastic": "25", "steel": "20", "stainless steel": "20", "iron": "20"},"32": {"aluminum": "21", "brass": "21", "plastic": "21", "steel": "18", "stainless steel": "18", "iron": "18"}},"12": {"24": {"aluminum": "16", "brass": "16", "plastic": "16", "steel": "12", "stainless steel": "12", "iron": "12"},"28": {"aluminum": "14", "brass": "14", "plastic": "14", "steel": "10", "stainless steel": "10", "iron": "10"},"32": {"aluminum": "13", "brass": "13", "plastic": "13", "steel": "9", "stainless steel": "9", "iron": "9"}},"0.25": {"20": {"aluminum": "7", "brass": "7", "plastic": "7", "steel": "7/32", "stainless steel": "7/32", "iron": "7/32"},"28": {"aluminum": "3", "brass": "3", "plastic": "3", "steel": "1", "stainless steel": "1", "iron": "1"},"32": {"aluminum": "7/32", "brass": "7/32", "plastic": "7/32", "steel": "1", "stainless steel": "1", "iron": "1"}},"0.3125": {"18": {"aluminum": "F", "brass": "F", "plastic": "F", "steel": "J", "stainless steel": "J", "iron": "J"},"24": {"aluminum": "I", "brass": "I", "plastic": "I", "steel": "9/32", "stainless steel": "9/32", "iron": "9/32"},"32": {"aluminum": "9/32", "brass": "9/32", "plastic": "9/32", "steel": "L", "stainless steel": "L", "iron": "L"}},"0.375": {"16": {"aluminum": "5/16", "brass": "5/16", "plastic": "5/16", "steel": "Q", "stainless steel": "Q", "iron": "Q"},"24": {"aluminum": "Q", "brass": "Q", "plastic": "Q", "steel": "S", "stainless steel": "S", "iron": "S"},"32": {"aluminum": "11/32", "brass": "11/32", "plastic": "11/32", "steel": "T", "stainless steel": "T", "iron": "T"}},"0.4375": {"14": {"aluminum": "U", "brass": "U", "plastic": "U", "steel": "25/64", "stainless steel": "25/64", "iron": "25/64"},"20": {"aluminum": "25/64", "brass": "25/64", "plastic": "25/64", "steel": "13/32", "stainless steel": "13/32", "iron": "13/32"},"28": {"aluminum": "Y", "brass": "Y", "plastic": "Y", "steel": "Z", "stainless steel": "Z", "iron": "Z"}},"0.5": {"13": {"aluminum": "27/64", "brass": "27/64", "plastic": "27/64", "steel": "29/64", "stainless steel": "29/64", "iron": "29/64"}},"1/2": {"20": {"aluminum": "29/64", "brass": "29/64", "plastic": "29/64", "steel": "15/32", "stainless steel": "15/32", "iron": "15/32"}},"0.5": {"28": {"aluminum": "15/32", "brass": "15/32", "plastic": "15/32", "steel": "15/32", "stainless steel": "15/32", "iron": "15/32"}},"0.5625": {"12": {"aluminum": "31/64", "brass": "31/64", "plastic": "31/64", "steel": "33/64", "stainless steel": "33/64", "iron": "33/64"},"18": {"aluminum": "33/64", "brass": "33/64", "plastic": "33/64", "steel": "17/32", "stainless steel": "17/32", "iron": "17/32"},"24": {"aluminum": "33/64", "brass": "33/64", "plastic": "33/64", "steel": "17/32", "stainless steel": "17/32", "iron": "17/32"}},"0.625": {"11": {"aluminum": "17/32", "brass": "17/32", "plastic": "17/32", "steel": "0.5625", "stainless steel": "0.5625", "iron": "0.5625"},"18": {"aluminum": "37/64", "brass": "37/64", "plastic": "37/64", "steel": "19/32", "stainless steel": "19/32", "iron": "19/32"},"24": {"aluminum": "37/64", "brass": "37/64", "plastic": "37/64", "steel": "19/32", "stainless steel": "19/32", "iron": "19/32"}},"0.6875": {"24": {"aluminum": "41/64", "brass": "41/64", "plastic": "41/64", "steel": "21/32", "stainless steel": "21/32", "iron": "21/32"}},"0.75": {"10": {"aluminum": "21/32", "brass": "21/32", "plastic": "21/32", "steel": "0.6875", "stainless steel": "0.6875", "iron": "0.6875"},"16": {"aluminum": "11/16", "brass": "11/16", "plastic": "11/16", "steel": "45/64", "stainless steel": "45/64", "iron": "45/64"},"20": {"aluminum": "45/64", "brass": "45/64", "plastic": "45/64", "steel": "23/32", "stainless steel": "23/32", "iron": "23/32"}},"13/16": {"20": {"aluminum": "49/64", "brass": "49/64", "plastic": "49/64", "steel": "25/32", "stainless steel": "25/32", "iron": "25/32"}},"0.875": {"9": {"aluminum": "49/64", "brass": "49/64", "plastic": "49/64", "steel": "51/64", "stainless steel": "51/64", "iron": "51/64"},"14": {"aluminum": "13/16", "brass": "13/16", "plastic": "13/16", "steel": "53/64", "stainless steel": "53/64", "iron": "53/64"},"20": {"aluminum": "53/64", "brass": "53/64", "plastic": "53/64", "steel": "27/32", "stainless steel": "27/32", "iron": "27/32"}},"15/16": {"20": {"aluminum": "57/64", "brass": "57/64", "plastic": "57/64", "steel": "29/32", "stainless steel": "29/32", "iron": "29/32"}},"quarter": {"20": {"aluminum": "7", "brass": "7", "plastic": "7", "steel": "7/32", "stainless steel": "7/32", "iron": "7/32"},"28": {"aluminum": "3", "brass": "3", "plastic": "3", "steel": "1", "stainless steel": "1", "iron": "1"},"32": {"aluminum": "7/32", "brass": "7/32", "plastic": "7/32", "steel": "1", "stainless steel": "1", "iron": "1"}},"one quarter": {"20": {"aluminum": "7", "brass": "7", "plastic": "7", "steel": "7/32", "stainless steel": "7/32", "iron": "7/32"},"28": {"aluminum": "3", "brass": "3", "plastic": "3", "steel": "1", "stainless steel": "1", "iron": "1"},"32": {"aluminum": "7/32", "brass": "7/32", "plastic": "7/32", "steel": "1", "stainless steel": "1", "iron": "1"}},"five sixteenths": {"18": {"aluminum": "F", "brass": "F", "plastic": "F", "steel": "J", "stainless steel": "J", "iron": "J"},"24": {"aluminum": "I", "brass": "I", "plastic": "I", "steel": "9/32", "stainless steel": "9/32", "iron": "9/32"},"32": {"aluminum": "9/32", "brass": "9/32", "plastic": "9/32", "steel": "L", "stainless steel": "L", "iron": "L"}},"three eighths": {"16": {"aluminum": "5/16", "brass": "5/16", "plastic": "5/16", "steel": "Q", "stainless steel": "Q", "iron": "Q"},"24": {"aluminum": "Q", "brass": "Q", "plastic": "Q", "steel": "S", "stainless steel": "S", "iron": "S"},"32": {"aluminum": "11/32", "brass": "11/32", "plastic": "11/32", "steel": "T", "stainless steel": "T", "iron": "T"}},"seven sixteenths": {"14": {"aluminum": "U", "brass": "U", "plastic": "U", "steel": "25/64", "stainless steel": "25/64", "iron": "25/64"},"20": {"aluminum": "25/64", "brass": "25/64", "plastic": "25/64", "steel": "13/32", "stainless steel": "13/32", "iron": "13/32"},"28": {"aluminum": "Y", "brass": "Y", "plastic": "Y", "steel": "Z", "stainless steel": "Z", "iron": "Z"}},"half": {"13": {"aluminum": "27/64", "brass": "27/64", "plastic": "27/64", "steel": "29/64", "stainless steel": "29/64", "iron": "29/64"},"20": {"aluminum": "29/64", "brass": "29/64", "plastic": "29/64", "steel": "15/32", "stainless steel": "15/32", "iron": "15/32"},"28": {"aluminum": "15/32", "brass": "15/32", "plastic": "15/32", "steel": "15/32", "stainless steel": "15/32", "iron": "15/32"}},"one half": {"13": {"aluminum": "27/64", "brass": "27/64", "plastic": "27/64", "steel": "29/64", "stainless steel": "29/64", "iron": "29/64"},"20": {"aluminum": "29/64", "brass": "29/64", "plastic": "29/64", "steel": "15/32", "stainless steel": "15/32", "iron": "15/32"},"28": {"aluminum": "15/32", "brass": "15/32", "plastic": "15/32", "steel": "15/32", "stainless steel": "15/32", "iron": "15/32"}},"nine sixteenths": {"12": {"aluminum": "31/64", "brass": "31/64", "plastic": "31/64", "steel": "33/64", "stainless steel": "33/64", "iron": "33/64"},"18": {"aluminum": "33/64", "brass": "33/64", "plastic": "33/64", "steel": "17/32", "stainless steel": "17/32", "iron": "17/32"},"24": {"aluminum": "33/64", "brass": "33/64", "plastic": "33/64", "steel": "17/32", "stainless steel": "17/32", "iron": "17/32"}},"five eighths": {"11": {"aluminum": "17/32", "brass": "17/32", "plastic": "17/32", "steel": "0.5625", "stainless steel": "0.5625", "iron": "0.5625"},"18": {"aluminum": "37/64", "brass": "37/64", "plastic": "37/64", "steel": "19/32", "stainless steel": "19/32", "iron": "19/32"},"24": {"aluminum": "37/64", "brass": "37/64", "plastic": "37/64", "steel": "19/32", "stainless steel": "19/32", "iron": "19/32"}},"eleven sixteenths": {"24": {"aluminum": "41/64", "brass": "41/64", "plastic": "41/64", "steel": "21/32", "stainless steel": "21/32", "iron": "21/32"}},"three quarters": {"10": {"aluminum": "21/32", "brass": "21/32", "plastic": "21/32", "steel": "0.6875", "stainless steel": "0.6875", "iron": "0.6875"},"16": {"aluminum": "11/16", "brass": "11/16", "plastic": "11/16", "steel": "45/64", "stainless steel": "45/64", "iron": "45/64"},"20": {"aluminum": "45/64", "brass": "45/64", "plastic": "45/64", "steel": "23/32", "stainless steel": "23/32", "iron": "23/32"}},"three fourths": {"10": {"aluminum": "21/32", "brass": "21/32", "plastic": "21/32", "steel": "0.6875", "stainless steel": "0.6875", "iron": "0.6875"},"16": {"aluminum": "11/16", "brass": "11/16", "plastic": "11/16", "steel": "45/64", "stainless steel": "45/64", "iron": "45/64"},"20": {"aluminum": "45/64", "brass": "45/64", "plastic": "45/64", "steel": "23/32", "stainless steel": "23/32", "iron": "23/32"}},"thirteen sixteenths": {"20": {"aluminum": "49/64", "brass": "49/64", "plastic": "49/64", "steel": "25/32", "stainless steel": "25/32", "iron": "25/32"}},"seven eighths": {"9": {"aluminum": "49/64", "brass": "49/64", "plastic": "49/64", "steel": "51/64", "stainless steel": "51/64", "iron": "51/64"},"14": {"aluminum": "13/16", "brass": "13/16", "plastic": "13/16", "steel": "53/64", "stainless steel": "53/64", "iron": "53/64"},"20": {"aluminum": "53/64", "brass": "53/64", "plastic": "53/64", "steel": "27/32", "stainless steel": "27/32", "iron": "27/32"}},"fifteen sixteenths": {"20": {"aluminum": "57/64", "brass": "57/64", "plastic": "57/64", "steel": "29/32", "stainless steel": "29/32", "iron": "29/32"}}}

clear_chart = {"0": {"close": "52", "free": "50"},"1": {"close": "48", "free": "46"},"1": {"close": "48", "free": "46"},"2": {"close": "43", "free": "41"},"2": {"close": "43", "free": "41"},"3": {"close": "37", "free": "35"},"3": {"close": "37", "free": "35"},"4": {"close": "32", "free": "30"},"4": {"close": "32", "free": "30"},"5": {"close": "30", "free": "29"},"5": {"close": "30", "free": "29"},"6": {"close": "27", "free": "25"},"6": {"close": "27", "free": "25"},"8": {"close": "18", "free": "16"},"8": {"close": "18", "free": "16"},"10": {"close": "9", "free": "7"},"10": {"close": "9", "free": "7"},"12": {"close": "2", "free": "1"},"12": {"close": "2", "free": "1"},"12": {"close": "2", "free": "1"},"0.25": {"close": "F", "free": "H"},"0.25": {"close": "F", "free": "H"},"0.25": {"close": "F", "free": "H"},"0.3125": {"close": "P", "free": "Q"},"0.3125": {"close": "P", "free": "Q"},"0.3125": {"close": "P", "free": "Q"},"0.375": {"close": "W", "free": "X"},"0.375": {"close": "W", "free": "X"},"0.375": {"close": "W", "free": "X"},"0.4375": {"close": "29/64", "free": "15/32"},"0.4375": {"close": "29/65", "free": "15/33"},"0.4375": {"close": "29/66", "free": "15/34"},"0.5": {"close": "33/64", "free": "17/32"},"1/2": {"close": "33/65", "free": "17/33"},"0.5": {"close": "33/66", "free": "17/34"},"0.5625": {"close": "37/64", "free": "19/32"},"0.5625": {"close": "37/65", "free": "19/33"},"0.5625": {"close": "37/66", "free": "19/34"},"0.625": {"close": "41/64", "free": "21/32"},"0.625": {"close": "41/65", "free": "21/33"},"0.625": {"close": "41/66", "free": "21/34"},"0.6875": {"close": "45/64", "free": "23/32"},"0.75": {"close": "49/64", "free": "25/32"},"0.75": {"close": "49/65", "free": "25/33"},"0.75": {"close": "49/66", "free": "25/34"},"13/16": {"close": "53/64", "free": "27/32"},"0.875": {"close": "57/64", "free": "29/32"},"0.875": {"close": "57/65", "free": "29/33"},"0.875": {"close": "57/66", "free": "29/34"},"15/16": {"close": "61/64", "free": "31/32"},"1": {"close": "1.0156", "free": "1.0312"},"1": {"close": "1.0156", "free": "1.0312"},"1": {"close": "1.0156", "free": "1.0312"},"quarter": {"close": "F", "free": "H"},"quarter": {"close": "F", "free": "H"},"quarter": {"close": "F", "free": "H"},"one quarter": {"close": "F", "free": "H"},"one quarter": {"close": "F", "free": "H"},"one quarter": {"close": "F", "free": "H"},"five sixteenths": {"close": "P", "free": "Q"},"five sixteenths": {"close": "P", "free": "Q"},"five sixteenths": {"close": "P", "free": "Q"},"three eighths": {"close": "W", "free": "X"},"three eighths": {"close": "W", "free": "X"},"three eighths": {"close": "W", "free": "X"},"seven sixteenths": {"close": "29/64", "free": "15/32"},"seven sixteenths": {"close": "29/65", "free": "15/33"},"seven sixteenths": {"close": "29/66", "free": "15/34"},"half": {"close": "33/64", "free": "17/32"},"half": {"close": "33/65", "free": "17/33"},"half": {"close": "33/66", "free": "17/34"},"one half": {"close": "33/64", "free": "17/32"},"one half": {"close": "33/65", "free": "17/33"},"one half": {"close": "33/66", "free": "17/34"},"nine sixteenths": {"close": "37/64", "free": "19/32"},"nine sixteenths": {"close": "37/65", "free": "19/33"},"nine sixteenths": {"close": "37/66", "free": "19/34"},"five eighths": {"close": "41/64", "free": "21/32"},"five eighths": {"close": "41/65", "free": "21/33"},"five eighths": {"close": "41/66", "free": "21/34"},"eleven sixteenths": {"close": "45/64", "free": "23/32"},"three quarters": {"close": "49/64", "free": "25/32"},"three quarters": {"close": "49/65", "free": "25/33"},"three quarters": {"close": "49/66", "free": "25/34"},"three fourths": {"close": "49/64", "free": "25/32"},"three fourths": {"close": "49/65", "free": "25/33"},"three fourths": {"close": "49/66", "free": "25/34"},"thirteen sixteenths": {"close": "53/64", "free": "27/32"},"seven eighths": {"close": "57/64", "free": "29/32"},"seven eighths": {"close": "57/65", "free": "29/33"},"seven eighths": {"close": "57/66", "free": "29/34"},"fifteen sixteenths": {"close": "61/64", "free": "31/32"}}


test_dict = {"brass":{"steel":"50"},
             "aluminum":{"brass":"30"}}
# Calculations
##############################



def speed_calc(drill_size, material):
    this_drill_size = drill_size
    if "inch" in drill_size:
        st_ind = drill_size.index("inch")
        #end_ind = st_ind + 4
        this_drill_size =  drill_size[0:st_ind]
    tool_diam = drill_decimal_eq[this_drill_size]
    surface_sp = material_chart[material]
    spindle_sp = surface_sp / (0.262 * tool_diam)
    #fin_sp = (math.floor(spindle_sp * 100))/ 100.0 #floor to 2 decimcal places
    #fin_sp = int(spindle_sp) #floor to one's place
    fin_sp = int((math.floor(spindle_sp / 100)) * 100)  # floor to 2 decimcal places
    return str(fin_sp)

def get_tap_hole_size(bolt_diam, pitch, material):
    #drill_size = tap_chart[bolt_diam][pitch][material]
    #drill_size = clear_chart[bolt_diam]["free"]
    this_bolt = bolt_diam
    if "inch" in bolt_diam:
        ind = bolt_diam.index("inch") - 1
        this_bolt = bolt_diam[0:ind]
    drill_size = tap_chart[this_bolt][pitch][material]
    ans = str(drill_size)
    return str(ans)

def size_tap_hole(bolt_diam, material):
    #drill_size = tap_chart[bolt_diam][pitch][material]
    #drill_size = clear_chart[bolt_diam]["free"]
    this_bolt = bolt_diam
    if "inch" in bolt_diam:
        ind = bolt_diam.index("inch") - 1
        this_bolt = bolt_diam[0:ind]
    drill_size = simple_tap_chart[this_bolt][material]
    ans = str(drill_size)
    return str(ans)

def get_clear_hole_size(bolt_diam, fit):
    this_fit = fit
    #remove trailing fit
    if "fit" in fit:
        fit_ind = fit.index("fit")
        this_fit = fit[0:fit_ind]
    #remove other trailing words
    if " " in fit:
        sp_ind = fit.index(" ")
        this_fit = fit[0:sp_ind]
    this_bolt = bolt_diam
    if "inch" in bolt_diam:
        ind = bolt_diam.index("inch") - 1
        this_bolt = bolt_diam[0:ind]

    drill_size = clear_chart[this_bolt][this_fit]
    ans = str(drill_size)
    return str(ans)

def test_ans(t_key, key_2):
    ans = test_dict[t_key][key_2]
    #ans = test_dict[t_key]
    #ans = str(clear_chart[t_key][key_2])

    return str(ans)

##############################
# Custom Intents
##############################

def test_intent(event, context):
    dialog_state = event['request']['dialogState']

    if dialog_state in ("STARTED", "IN_PROGRESS"):
        return continue_dialog()

    elif dialog_state == "COMPLETED":
        test_key = event["request"]["intent"]["slots"]["response"]["value"]
        test_key_2 = event["request"]["intent"]["slots"]["response_two"]["value"]
        resp = ""
        res_msg = ""

        try:
            resp = test_ans(test_key, test_key_2)
            res_msg = "The test answer is " + resp +". Is there anything else I can help you with?"
        except:
            res_msg = "Sorry I don't yet have information on " + test_key + " and " + test_key_2 +\
                      ". Is there anything else I can help you with?"
        #resp = test_ans(test_key)

        reprompt = "Sorry, what size drill are you using? Please respond with a letter, number, or fractional drill size"
        #return convo_and_reprompt("SpeedCalc", res_msg, reprompt, {})
        return conversation("Testing" + test_key, res_msg, {})

    else:
        return conversation("SpeedCalc", "No dialog", {})


def speed_intent(event, context):
    dialog_state = event['request']['dialogState']

    if dialog_state in ("STARTED", "IN_PROGRESS"):
        return continue_dialog()

    elif dialog_state == "COMPLETED":
        drill_size = event["request"]["intent"]["slots"]["drillsize"]["value"]
        material = event["request"]["intent"]["slots"]["material"]["value"]
        sp_res = ""
        res_msg = ""
        try:
            sp_res = speed_calc(drill_size, material)
            res_msg = "You will need a spindle speed of " + sp_res + " RPM " + \
                      "for drilling " + material + " with a size " + drill_size + " drill" \
                      ". Is there anything else I can help you with?"
                     # ". Let me know if there's anything else I can help you with, like Tap holes, clearance holes, or spindle speed."
        except:
            res_msg = "Sorry I don't yet have information on " + drill_size + " and " + material +\
                      ". Is there anything else I can help you with?"
                     # ". Let me know if there's anything else I can help you with, like Tap holes, clearance holes, or spindle speed."
        reprompt = "Please tell me what drill size and material you are using."
        #return convo_and_reprompt("SpeedCalc", res_msg, reprompt, {})
        return conversation("SpeedCalc", res_msg, {})

    else:
        return conversation("SpeedCalc", "No dialog", {})


def hole_size_intent(event, context):
    #Just used to guide the user to say the right utterance
    msg = "To size a tap hole, say tap hole, to drill a clearance hole, say clearance hole"
    return conversation("HoleSizing", msg, {})



def tap_hole_intent(event, context):
    dialog_state = event['request']['dialogState']

    if dialog_state in ("STARTED", "IN_PROGRESS"):
        return continue_dialog()

    elif dialog_state == "COMPLETED":
        bolt_d = event["request"]["intent"]["slots"]["boltdiameter"]["value"]
        #pitch = event["request"]["intent"]["slots"]["pitch"]["value"]
        material = event["request"]["intent"]["slots"]["tapmaterial"]["value"]
        resp = ""
        res_msg = ""
        try:
            #resp = get_tap_hole_size(bolt_d, pitch, material)
            resp = size_tap_hole(bolt_d, material)
            res_msg = "You will need a size " +resp + " drill for drilling a tap hole for a size " + bolt_d + " bolt in " + material + \
                      ". Is there anything else I can help you with?"
                      #". Let me know if there's anything else I can help you with, like Tap holes, clearance holes, or spindle speed."
            reprompt = "Sorry, I can help you with sizing a clearance hole, sizing a tap hole and choosing a spindle speed. What can I help you with?"
        except:
            res_msg = "Sorry I don't yet have information on size " + bolt_d +" bolts in " + material + \
                      ". Is there anything else I can help you with?"
                      #". Let me know if there's anything else I can help you with, like Tap holes, clearance holes, or spindle speed."

        #return convo_and_reprompt("TapHoleSize", res_msg, reprompt, {})
        return conversation("TapHoleSize " + material, res_msg, {})

    else:
        #need to debug to find out when this happens
        return statement("TapHoleSize", "No dialog")

def clear_hole_intent(event, context):
    dialog_state = event['request']['dialogState']

    if dialog_state in ("STARTED", "IN_PROGRESS"):
        return continue_dialog()

    elif dialog_state == "COMPLETED":
        bolt_d = event["request"]["intent"]["slots"]["boltdiameter"]["value"]
        fit = event["request"]["intent"]["slots"]["fittype"]["value"]
        this_fit = fit
        if "fit" in fit:
            fit_ind = fit.index("fit")
            this_fit = fit[0:fit_ind]
        #fit = event["request"]["intent"]["slots"]["fittype"]["resolutions"]["resolutionsPerAuthority"]["values"]["id"]
        resp = ""
        res_msg = ""
        try:
            resp = get_clear_hole_size(bolt_d, fit)
            #res_msg = "You need a drill size" + resp + "other words"
            res_msg = "You will need a size " +resp + " drill for drilling a " + this_fit + " fit hole for a size "+ bolt_d + " bolt" + \
                      ". Is there anything else I can help you with?"
                      #". Let me know if there's anything else I can help you with, like Tap holes, clearance holes, or spindle speed."
        except:
            res_msg = "Sorry I don't yet have information on " + this_fit + " fit for a size " + bolt_d + " bolts " +\
                      ". Is there anything else I can help you with?"
                      #". Let me know if there's anything else I can help you with, like Tap holes, clearance holes, or spindle speed."

        reprompt = "Sorry, I can help you with sizing a clearance hole, sizing a tap hole and choosing a spindle speed. What can I help you with?"
        #return convo_and_reprompt("ClearHoleSize", res_msg, reprompt, {})
        return conversation("ClearHoleSize", res_msg, {})

    else:
        return statement("ClearHoleSize", "No dialog")

def slow_tap_hole_intent(event, context):
    dialog_state = event['request']['dialogState']

    if dialog_state in ("STARTED", "IN_PROGRESS"):
        return continue_dialog()

    elif dialog_state == "COMPLETED":
        bolt_d = event["request"]["intent"]["slots"]["boltdiameter"]["value"]
        #pitch = event["request"]["intent"]["slots"]["pitch"]["value"]
        material = event["request"]["intent"]["slots"]["tapmaterial"]["value"]
        resp = ""
        res_msg = ""
        try:
            #resp = get_tap_hole_size(bolt_d, pitch, material)
            #Help me drill a tap hole for a size 4 bolt in aluminum
            resp = size_tap_hole(bolt_d, material)
            res_msg = "You will need a size " + resp + " drill for drilling a tap hole for a size " + bolt_d + " bolt in " + material + \
                      ". For a faster response next time, answer my welcome message with, " +\
                      "Help me drill a Tap Hole for a size " + bolt_d + " bolt in " + material +\
                      ". Is there anything else I can help you with?"
            reprompt = "Sorry, I can help you with sizing a clearance hole, sizing a tap hole and choosing a spindle speed. What can I help you with?"
        except:
            res_msg = "Sorry I don't yet have information on size " + bolt_d + " bolts with " + material + \
                      ". Is there anything else I can help you with?"

        # return convo_and_reprompt("TapHoleSize", res_msg, reprompt, {})
        return conversation("TapHoleSize " + material, res_msg, {})

    else:
        # need to debug to find out when this happens
        return statement("TapHoleSize", "No dialog")

def slow_clear_hole_intent(event, context):
    dialog_state = event['request']['dialogState']

    if dialog_state in ("STARTED", "IN_PROGRESS"):
        return continue_dialog()

    elif dialog_state == "COMPLETED":
        bolt_d = event["request"]["intent"]["slots"]["boltdiameter"]["value"]
        fit = event["request"]["intent"]["slots"]["fittype"]["value"]
        this_fit = fit
        if "fit" in fit:
            fit_ind = fit.index("fit")
            this_fit = fit[0:fit_ind]
        # fit = event["request"]["intent"]["slots"]["fittype"]["resolutions"]["resolutionsPerAuthority"]["values"]["id"]
        resp = ""
        res_msg = ""
        try:
            resp = get_clear_hole_size(bolt_d, fit)
            # res_msg = "You need a drill size" + resp + "other words"
            #For a faster response next time, answer my welcome message with: Help me drill a free fit clearance hole for a size 10 bolt
            res_msg = "You will need a size " + resp + " drill for drilling a " + this_fit + " fit hole for a size " + bolt_d + " bolt" + \
                      ". For a faster response next time, answer my welcome message with, " +\
                      "Help me drill a " + this_fit + " fit Clearance Hole for a size" + bolt_d + " bolt" + \
                      ". Is there anything else I can help you with?"
        except:
            res_msg = "Sorry I don't yet have information on " + this_fit + " fit for a " + bolt_d + " bolts " + \
                      ". Is there anything else I can help you with?"

        reprompt = "Sorry, I can help you with sizing a clearance hole, sizing a tap hole and choosing a spindle speed. What can I help you with?"
        # return convo_and_reprompt("ClearHoleSize", res_msg, reprompt, {})
        return conversation("ClearHoleSize", res_msg, {})

    else:
        return statement("ClearHoleSize", "No dialog")

# def tutorial_intent(event, context):
#     #TODO
#     #type out samlpe interaction
#     #not using
#     return


##############################
# Required Intents
##############################

#Fill in what we want to say for each of these
def cancel_intent():
    close_msg = "Thank you for using the drill helper."
    return statement("CancelIntent", close_msg)


def help_intent():
    help_msg = "I can help you with sizing a close clearance hole, sizing a free clearance hole,\
                sizing a tap hole and choosing a spindle speed. \
                What can I help you with?"
    return conversation("HelpIntent", help_msg, {})


def stop_intent():
    close_msg = "Thank you for using the drill helper."
    return statement("StopIntent", close_msg)

def yes_intent():
    msg = "Would you like help with clearance holes, tap holes, or spindle speed?"
    return conversation("Continue Conversation", msg, {})

##############################
# On Launch
##############################


def on_launch(event, context):
    welcome_msg = "Welcome to Drill Helper. Would you like help with clearance holes, tap holes, or spindle speed?"

    reprompt = "I can help you with sizing a clearance hole,\
               sizing a tap hole, and choosing a spindle speed"\
               ". To stop say exit Drill helper. "
    return convo_and_reprompt("Welcome", welcome_msg, reprompt, {})
    #return conversation("Welcome", welcome_msg, {})

##############################
# On Session Ended
##############################


def on_session_ended(event, context):
    goodbye_msg = "Thank you for using the drill helper."
    #return convo_and_reprompt("Welcome", welcome_msg, reprompt, {})
    #return conversation("Welcome", welcome_msg, {})
    return statement("Session Ended", goodbye_msg)


##############################
# Routing
##############################


def intent_router(event, context):
    intent = event['request']['intent']['name']

    # Custom Intents

    if intent == "SpeedCalc":
        return speed_intent(event, context)

    elif intent == "HoleSizing":
        return hole_size_intent(event, context)

    elif intent == "TapHoleSize":
        return tap_hole_intent(event, context)

    elif intent == "ClearHoleSize":
        return clear_hole_intent(event, context)

    elif intent == "SlowTapHoleSize":
        return slow_tap_hole_intent(event, context)

    elif intent == "SlowClearHoleSize":
        return slow_clear_hole_intent(event, context)

    # elif intent == "Tutorial":
    #     return tutorial_intent(event, context)

    elif intent == "test":
        return test_intent(event, context)
    # Required Intents

    elif intent == "YesIntent":
        return yes_intent()

    elif intent == "AMAZON.CancelIntent":
        return cancel_intent()

    elif intent == "AMAZON.HelpIntent":
        return help_intent()

    elif intent == "AMAZON.StopIntent":
        return stop_intent()

    elif intent == "NoIntent":
        return stop_intent()



    else:
        return cancel_intent()


##############################
# Program Entry
##############################


def lambda_handler(event, context):
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event, context)

    elif event['request']['type'] == "IntentRequest":
        return intent_router(event, context)

    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event, context)


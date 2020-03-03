import re
import fractions


def mixed_to_float(x):
    return float(sum(fractions.Fraction(term) for term in x.split()))

def recipe_parser(recipe):
    dic = {}

    for i in (recipe['ingredients']):
        dic[i] = {}
        x = re.findall('\w+ed |\w+ed$', i)
        if x != []:
            dic[i] = {'Preparation': x}

    for i in (recipe['ingredients']):
        if 'egg' in i:
            pass
        # print(i)
        else:
            if '(' in i and '%' not in i:
                x = re.findall('\(\d+ (\w+)\)', i)
                if x != []:
                    dic[i]['Measurement'] = x
            elif '%' in i:
                x = re.findall('\d+ (\w+)', i)
                if x != []:
                    dic[i]['Measurement'] = x
            else:
                x = re.findall('\d+ (\w+) \w+', i)
                if x != []:
                    dic[i]['Measurement'] = x

    for i in (recipe['ingredients']):
        if '(' in i and '%' not in i:
            x = re.findall('\((\d+) \w+\)', i)
            if x != []:
                dic[i]['Quantity'] = mixed_to_float(x[0])
        elif '%' in i:
            x = re.findall('(\d+) \w+', i)
            if x != []:
                dic[i]['Quantity'] = mixed_to_float(x[0])
        else:
            if '/' in i:
                x = re.findall('(\d*\s*\d\/\d)+', i)
                if x != []:
                    dic[i]['Quantity'] = mixed_to_float(x[0])

            else:
                x = re.findall('(\d+) \w', i)
                if x != []:
                    dic[i]['Quantity'] = mixed_to_float(x[0])

    for i in (recipe['ingredients']):
        if 'egg' in i:
            x = re.findall('\d+ (.*)', i)
            dic[i]['Ingredient Name'] = x[0]
        else:
            x = i
            if ')' in i:
                x = re.sub('.*\(.*\) \w+', '', x)
            #         if x!=[]:
            #             dic[i]['Quantity'] = x
            if '/' in i:
                x = re.sub('\/', '', x)
            #             if x!=[]:
            #                 dic[i]['Quantity'] = mixed_to_float(x[0])
            x = re.sub('\d+', '', x)
            try:
                x = re.sub(dic[i]['Measurement'][0], '', x)
                x = re.sub(dic[i]['Preparation'][0], '', x)
            except:
                x = x
            x = re.sub('\,.*|to taste', '', x).lstrip(' ')
            dic[i]['Ingredient Name'] = x
    return dic
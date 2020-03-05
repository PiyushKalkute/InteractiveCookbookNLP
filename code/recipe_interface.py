import fractions
import json
import re
import random
import numpy as np
from reci_scraper import RecipeFetcher
import reci_parser as p

path = 'collectionDB.json'
with open(path) as f:
    # load the data
    json_data = json.load(f)

indian_dict = json_data["anyToIndian"]
style_dict = json_data["styles"]
health_dict = json_data["healthyToUnhealthy"]
tools_db = json_data["tools"]
primary_cooking = json_data["methods"]["primary"]
secondary_cooking = json_data["methods"]["secondary"]
healthy = ['wheat', 'cottage','sauce']
meat_dict = json_data["nonvegToVeg"]
veg_dict = json_data["vegetables"]
def to_Healthy(recipe_dic):
    arr = []
    arr2 = []
    transformed_directions = []
    print("=============================================================================================================")
    print("========================================TRANSFORMATION LOG===================================================")
    for i in recipe_dic:
        curr = recipe_dic[i]['Ingredient Name'].lower()

        for j in health_dict:
            if (j['unhealthy']) in curr and not (any(substring in curr for substring in healthy)):
                recipe_dic[i]['Ingredient Name'] = j['healthy']
                arr.append(curr)
                arr2.append(j['healthy'])
                print("- ",curr,"was replaced with ",j['healthy'])
    for k in recipe['directions']:
        for i in range(len(arr)):
            j = k.lower()
            if arr[i] in j:
                k = j.replace(arr[i], arr2[i])
        transformed_directions.append(k)
    return transformed_directions


def to_Unhealthy(recipe_dic):
    arr = []
    arr2 = []
    transformed_directions = []
    print(
        "=============================================================================================================")
    print(
        "========================================TRANSFORMATION LOG===================================================")

    for i in recipe_dic:
        curr = recipe_dic[i]['Ingredient Name'].lower()
        for j in health_dict:
            if (j['healthy']) in curr:
                recipe_dic[i]['Ingredient Name'] = j['unhealthy']
                arr.append(curr)
                arr2.append(j['unhealthy'])
                print("- ", curr, "was replaced with ", j['unhealthy'])
    for k in recipe['directions']:
        for i in range(len(arr)):
            j = k.lower()
            if arr[i] in j:
                k = j.replace(arr[i], arr2[i])
        transformed_directions.append(k)
    return transformed_directions

def to_Indian(recipe_dic):
    arr = []
    steps = []
    transformed_directions = []
    print(
        "=============================================================================================================")
    print(
        "========================================TRANSFORMATION LOG===================================================")

    for i in recipe_dic:
        curr = recipe_dic[i]['Ingredient Name'].lower()
        for a in style_dict:
            if a in curr:
                k = curr.replace(a, 'indian')
                curr = k
        for j in indian_dict:
            if (j['other']) in curr:
                curr = curr.replace(j['other'], j['indian'])
                print("- ", j['other'], "was replaced with ", j['indian'])
        recipe_dic[i]['Ingredient Name'] = curr
        arr.append(curr)

    while '' in arr: arr.remove('')
    for k in recipe['directions']:
        j = k.lower()
        for a in style_dict:
            if a in j:
                k = j.replace(a, 'indian')
                j = k
        for a in indian_dict:
            if a['other'] in j:
                k = j.replace(a['other'], a['indian'])
                j = k
        transformed_directions.append(k)
    for k in transformed_directions:
        j = k.lower()
        for a in indian_dict:
            for word in a['other'].split():
                if word in j:
                    k = j.replace(word, a['indian'])
                    j = k
        steps.append(k)
    return steps


def cut_or_double(direction,n):
    updated_direc =[]
    for i in direction:
            x=re.findall('(\d+) \w*\s*minutes',i)
            if x!=[]:
                for j in x:
                    k = float(j)
                    k = k*n
                    k = str(k)
                    k = re.sub('\.\d+','',k)
                    i=re.sub(j,k,i)
            updated_direc.append(i)
    return updated_direc

def to_double(recipe_dic):
    print(
        "=============================================================================================================")
    print(
        "========================================TRANSFORMATION LOG===================================================")
    for i in recipe_dic:
        try:
            recipe_dic[i]['Quantity'] = 2*recipe_dic[i]['Quantity']

        except:
            pass
    update_dir1 = cut_or_double(recipe['directions'],1.5)
    return update_dir1


def to_half(recipe_dic):
    print(
        "=============================================================================================================")
    print(
        "========================================TRANSFORMATION LOG===================================================")
    for i in recipe_dic:
        try:

            recipe_dic[i]['Quantity'] = 0.5*recipe_dic[i]['Quantity']
        except:
            pass
    update_dir1 = cut_or_double(recipe['directions'],0.75)
    return update_dir1


def toVeg(nv_recipe):
    arr = []
    steps = []
    transformed_directions = []
    print(
        "=============================================================================================================")
    print(
        "========================================TRANSFORMATION LOG===================================================")
    for i in nv_recipe:
        curr = nv_recipe[i]['Ingredient Name'].lower()
        # print(curr)

        for j in meat_dict:
            if (j['nonveg']) in curr:

                curr = curr.replace(j['nonveg'], j['veg'])
                print("- ", j['nonveg'], "was replaced with ", j['veg'])
                nv_recipe[i]['Ingredient Name'] = curr
        arr.append(curr)

    for k in recipe['directions']:

        j = k.lower()
        for a in meat_dict:
            if a['nonveg'] in j:
                k = j.replace(a['nonveg'], a['veg'])
                j = k

        transformed_directions.append(k)

    for k in transformed_directions:
        j = k.lower()
        for a in meat_dict:
            for word in a['nonveg'].split():
                if word in j:
                    k = j.replace(word, a['veg'])
                    j = k
        steps.append(k)
    return steps


def toNonVeg(nv_recipe):
    veg_ing = []
    nv_ing = []

    transformed_directions = []
    print(
        "=============================================================================================================")
    print(
        "========================================TRANSFORMATION LOG===================================================")

    for i in nv_recipe:
        curr = nv_recipe[i]['Ingredient Name'].lower()
        n_veg_flag =0

        if (n_veg_flag<2):
            br_flag = False
            for j in meat_dict:
                if br_flag:
                    break
                if (j['veg']) in curr:
                    veg_ing.append(j['veg'])
                    nv_ing.append(j['nonveg'])
                    curr = curr.replace(j['veg'], j['nonveg'])
                    print("- ", j['veg'], "was replaced with ", j['nonveg'])
                    nv_recipe[i]['Ingredient Name'] = curr
                    br_flag = True
                    n_veg_flag+=1
                    if n_veg_flag == 2:
                        break
            if curr in veg_dict:  # and not (any(substring in curr for substring in spices)):
                veg_ing.append(curr)
                nv_sub = meat_dict[random.randint(0, len(meat_dict))]['nonveg']
                nv_ing.append(nv_sub)
                print("- ", curr, "was replaced with ", nv_sub)
                curr = curr.replace(curr, nv_sub)
                nv_recipe[i]['Ingredient Name'] = curr
                n_veg_flag += 1
                if n_veg_flag == 2:
                    break

    for k in recipe['directions']:
        j = k.lower()
        for a in range(0, len(nv_ing)):
            if veg_ing[a] in j:
                k = j.replace(veg_ing[a], nv_ing[a])
                j = k
        transformed_directions.append(k)
    return transformed_directions


print("Welcome to Hell's Kitchen. Provide a valid Allrecipes.com url of recipe of your choice or type 'exit' to cancel. ")
req_url = (input("Enter recipe URL : "))

rf = RecipeFetcher()

recipe = (rf.scrape_recipe(req_url))


primary_methods = []
for k in recipe['directions']:
    fl = False
    j = k.lower()
    for a in primary_cooking:
        if a in j:
            primary_methods.append(a)
secondary_methods = []
for k in recipe['directions']:
    fl = False
    j = k.lower()
    for a in secondary_cooking:
        if a in j:
            secondary_methods.append(a)
tools = []
for k in recipe['directions']:
    j = k.lower()
    for a in tools_db:
        if a in j:
            tools.append(a)
recipe['tools'] = np.unique(tools)
recipe['primary methods'] = np.unique(primary_methods)
recipe['secondary methods'] = np.unique(secondary_methods)

print(recipe)
initial_dic= p.recipe_parser(recipe)


#WRITE CODE FOR GETTING DIC FROM THE SCRAPED AND PARSED DATA
def display_recipe_info():
    print("==============================================================")
    print('Ingredient Name')
    for i in initial_dic:
        print('-',initial_dic[i]['Ingredient Name'])

    print('Quantity:')
    for i in initial_dic:
        try:
            print('-',initial_dic[i]['Quantity'])
        except:
            pass
    print('Measurement:')
    for i in initial_dic:
        try:
            print('-',initial_dic[i]['Measurement'])
        except:
            pass
    print('Preparation:')
    for i in initial_dic:
        try:
            print('-', initial_dic[i]['Preparation'])
        except:
            pass
    print('Tools used:')
    for j  in recipe['tools']:
        print('-', j)
    print("=============================================================================================================")
    print('Primary Cooking methods used:')
    for j  in recipe['primary methods']:
        print('-', j)
    print("=============================================================================================================")
    print('Secondary Cooking methods used:')
    for j  in recipe['secondary methods']:
        print('-', j)

    print("=============================================================================================================")
    print('Steps:')
    for j  in recipe['directions']:
        print('-', j)
display_recipe_info()

def display_transform_info():
    print(
        "=============================================================================================================")
    print("Ingredients used: ")
    for i in initial_dic:
        try:
            print(initial_dic[i]['Quantity'], " ", end="")
        except:
            pass
        try:
            print(initial_dic[i]['Measurement'][0] + " ", end="")
        except:
            pass
        try:
            for j in range(0, len(initial_dic[i]['Preparation'])):
                print(initial_dic[i]['Preparation'][j] + ",", end="")
        except:
            pass
        print(initial_dic[i]['Ingredient Name'])
    print("=============================================================================================================")
    i = 1
    print('Steps used:')
    for j in recipe['directions']:
        print('Step',i,':', j)
        i+=1

fl = True
while(fl == True):
    print("=============================================================================================================")

    print("What transformation would you like to apply now to the recipe: ")
    print('1. To Healthy')
    print('2. To Unhealthy')
    print('3. To Vegetarian')
    print('4. To Non-vegetarian')
    print('5. To Indian cuisine')
    print('6. Double the quantity')
    print('7. Half the quantity')
    print('8. Exit')
    inp = int(input('Enter your choice: '))
    print(inp)
    if inp == 1:
        recipe['directions'] = to_Healthy(initial_dic)
        display_transform_info()
    elif inp == 2:
        recipe['directions'] = to_Unhealthy(initial_dic)
        display_transform_info()
    elif inp == 3:
        recipe['directions'] = toVeg(initial_dic)
        display_transform_info()
    elif inp == 4:
        recipe['directions'] = toNonVeg(initial_dic)
        display_transform_info()
    elif inp == 5:
        recipe['directions'] = to_Indian(initial_dic)
        display_transform_info()
    elif inp ==6:
        recipe['directions'] = to_double(initial_dic)
        display_transform_info()
    elif inp ==7:
        recipe['directions'] = to_half(initial_dic)
        display_transform_info()
    else:
        fl = False
        print("Bye... Hope to see you soon... Until next time...")
        break



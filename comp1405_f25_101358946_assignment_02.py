# Name: Carmen Vacchio
# Student Number: 101358946

import portfolio_game_base_module_for_101358946 as base

def main():

    # -------------------------- INTERFACE --------------------------

    # --- Open window with background and title ---
    base.open_surf('The Hunger Trail')

    # Background with the 'sea' colour
    base.fill_surf(18, 83, 89)

    # Colours
    colour = (209, 255, 241) 
    colour2 = (142, 255, 221)
    colour3 = (65, 249, 194)

    # Title text, centered horizontally at y=190
    base.draw_text(190, 'The Hunger Trail', colour)

    # --- Main border frame ---
    w = 3 # line width
    cut = 9  # how much to chop off each corner

    # Main border frame coordinates---
    left, top = 130, 160
    right, bottom = 510, 260

    # Top edge (shortened: leave gaps at both ends)---
    base.draw_line((left + cut, top), (right - cut, top), colour, w)
    # Bottom edge
    base.draw_line((left + cut, bottom), (right - cut, bottom), colour, w)
    # Left edge
    base.draw_line((left, top + cut), (left, bottom - cut), colour, w)
    # Right edge
    base.draw_line((right, top + cut), (right, bottom - cut), colour, w)

    # --- Corner accents (little ticks) ---

    # Top-left---
    # outer (horizontal then vertical)
    base.draw_line((left + 3, top + 2), (left - cut + 1.5, top + 2), colour3, w)
    base.draw_line((left + 2, top - cut), (left + 2, top), colour3, w)
    # inner (horizontal then vertical)
    base.draw_line((left - 3, top + cut), (left + cut + 1.5, top + cut), colour2, w)
    base.draw_line((left + cut, top - 3), (left + cut, top + cut + 1.5), colour2, w)

    # Top-right---
    # outer (horizontal then vertical)
    base.draw_line((right - 3, top + 2), (right + cut, top + 2), colour3, w) 
    base.draw_line((right - 2, top - cut), (right - 2, top), colour3, w)   
    # inner (horizontal then vertical)
    base.draw_line((right + 3, top + cut), (right - cut , top + cut), colour2, w) 
    base.draw_line((right - cut, top - 3), (right - cut, top + cut + 1.5), colour2, w) 

    # Bottom-left---
    # outer (horizontal then vertical)
    base.draw_line((left + 3, bottom - 2), (left - cut, bottom - 2), colour3, w)
    base.draw_line((left + 2, bottom + cut), (left + 2, bottom), colour3, w)
    # inner (horizontal then vertical)
    base.draw_line((left - 3, bottom - cut), (left + cut, bottom - cut), colour2, w) 
    base.draw_line((left + cut, bottom + 3), (left + cut, bottom - cut - .5), colour2, w) 

    # Bottom-right---
    # outer (horizontal then vertical)
    base.draw_line((right - 3, bottom - 2), (right + cut, bottom - 2), colour3, w)
    base.draw_line((right - 2, bottom + cut), (right - 2, bottom), colour3, w)
    # inner (horizontal then vertical)
    base.draw_line((right + 3, bottom - cut), (right - cut, bottom - cut), colour2, w)
    base.draw_line((right - cut, bottom + 3), (right - cut, bottom - cut - .5), colour2, w)

    # --- Hold window open for 5 seconds ---
    base.hold_surf(500)

 
    # ---------------------- TERMINAL GAMEPLAY ----------------------

    # --- Intro text ---
    print('\nWelcome to The Hunger Trail!\n')
    print('In this game you will lead a group of travelers on a difficult journey.')
    print('You will need to make important decisions about food, supplies,')
    print('and survival as you face challenges along the way...\n')

    # --- Narrative/Learn more ---
    res = input('Would you like to learn more (y/n)? ').lower()
    if res == 'yes' or res == 'y':
        print("\nIn The Hunger Trail, you take on the role of a traveling vendor navigating a difficult trade route during a food shortage. Along the way, you'll gather, prepare, and manage supplies to keep your caravan alive. Every decision — from how you ration ingredients to how you prepare meals — affects your success. The journey will test not just your survival instincts, but your understanding of proper food preparation and planning.\n")

    # --- Starting location & sub routes ---
    print('\n----- STARTING LOCATION -----')
    print('1. Harveston Village\n2. Port Umber\n3. Stoneveil Crossing\n4. Learn more...\n')
    location = input('Where would you like to start? ').strip()

    if location == '4':
        print('\n1. Harveston Village: fertile farmlands known for grain and produce.\n2. Port Umber: a coastal trade hub famous for spices and salted meat.\n3. Stoneveil Crossing: a mountain pass settlement that trades in dried goods and cooking oil.\n')
        location = input('Where will it be traveller? ').strip()
    
    # Harveston Village branching control structure
    if location == '1':
        print('\n1. Millford Fields\n2. Oakbarrel Market\n3. Learn more...\n')
        location = input('From Harveston, you can venture north to Millford or east to Oakbarrel? ').strip()
        if location == '3':
            print('1. Millford Fields: open farmland where you can stock up on grain and flour. Prices are lower, but weather exposure increases travel time.\n2. Oakbarrel Market: a rural trading post known for dairy and fresh produce. Offers better quality goods, but stock is limited.\n')
            location = input('Where will it be traveller? ').strip()
            if location == '1':
                location = 'Harveston Village: Millford Fields'
            else:
                location = 'Harveston Village: Oakbarrel Market'
    
    # Port Umber branching control structure
    elif location == '2':
        print('\n1. Saltmar Wharf\n2. Old Bazaar District\n3. Learn more...\n')
        location = input('Would you like to set course for Saltmar or inland toward the Old Bazzar District? ').strip()
        if location == '3':
            print('1. Saltmar Wharf: docks lined with fishermen and spice vendors. Great deals on meat and salt, but storage risk is high due to humidity.\n2. Old Bazaar District: a crowded marketplace with exotic ingredients and cooking oils. Prices fluctuate daily, but rare items can appear.\n')
            location = input('Where will it be traveller? ').strip()
            if location == '1':
                location = 'Port Umber: Saltmar Wharf'
            else:
                location = 'Port Umber: Old Bazaar District'

    # Stoneveil Crossing
    else:
        location = 'Stoneveil Crossing'

    # --- Departure Date ---
    print('\n----- DEPARTURE DATE -----')
    print('1. March\n2. April\n3. June\n4. September\n5. November\n6. Learn more...\n')
    date = input('Which date would you like to hit the trail? ').strip()
    if date == '6':
        print('\n1. March: early spring; mild weather, but few fresh supplies available.\n2. April: balanced season, average food spoilage rate.\n3. June: summer heat increases water loss and food spoilage.\n4. September: harvest season; abundant crops, but colder nights.\n5. November: early winter; limited produce but safer meat storage.\n')
        date = input('Which date would you like? ').strip()
    if date == '1':
        date = 'March'
    elif date == '2':
        date = 'April'
    elif date == '3':
        date = 'June'
    elif date == '4':
        date = 'September'
    else:
        date = 'November'

    # --- Character Selection ---
    print('\n----- CHARACTER CLASSES -----')
    print('1. Chef: expert in food preservation and efficient ingredient use.\n2. Merchant: skilled trader, negotiates better prices and inventory bonuses.\n3. Forager: gathers wild foods and finds water more easily on the trail.\n')
    character = input('Which character class would you like? ').strip()
    if character == '1':
        character = 'Chef'
    elif character == '2':
        character = 'Merchant'
    else:
        character = 'Forager'

    # --- Buff/Debuff Stat ---
    if character == 'Chef' or date == 'November':
        stat = 'Buff: Food spoilage reduced by 30%'
        stat_description = 'A skilled Chef knows how to cure, salt, and preserve ingredients, while the cold air of late November naturally slows decay. Either way, your supplies stay fresher for longer on the trail.\n'
    elif character == 'Merchant' and date == 'March':
        stat = 'Buff: +15% starting funds'
        stat_description = 'Early spring is the start of the trading season — prices are low, and Merchants profit from offseason bulk deals.\n'
    elif character == 'Forager' and date == 'September':
        stat = 'Buff: +20% materials gathered'
        stat_description = "Late-harvest season means wild fruits, mushrooms, and roots are plentiful, making it ideal for a Forager's skillset.\n"
    elif character == 'Merchant' and date == 'June':
        stat = 'Debuff: Water costs +25%'
        stat_description = "Hot summer routes make water scarce and expensive, cutting into a Merchant's profit margins.\n"
    if stat:
        print(f'\n{stat_description}\n    • {stat}\n')

    # --- Party names ---
    leader = input('What is the first name of the party leader? ')
    print('\nWhat are the first names of the four other members in your party?')
    print(f'  1. {leader}')
    member2 = input('  2. ')
    member3 = input('  3. ')
    member4 = input('  4. ')
    member5 = input('  5. ')

    # --- Arithmetic pipeline for supplies ---
    total_currency = 101358946  # starting money = student number
    running_total = 0
    print(f"\nBefore leaving you should buy equipment and supplies. You have ${total_currency:.2f} in cash, but you don't have to spend it all now.\n")

    # Flour
    flour_cost = 3.00
    print(f'I charge ${flour_cost:.2f} for a sack of Flour. I recommend you buy at least 10 sacks so you can bake enough bread.\n')
    flour_qty = int(input('How many sacks of Flour do you want to buy? '))
    if flour_cost * flour_qty <= total_currency:
        running_total += flour_cost * flour_qty
        print(f'\nYour bill so far is: ${running_total:.2f}\n')
    else:
        print('\nInsufficient funds.\n')

    # Meat
    meat_cost = 8.00
    print(f'I charge ${meat_cost:.2f} for a portion of Meat. I recommend you buy at least 5 portions for protein.\n')
    meat_qty = int(input('How many portions of Meat do you want to buy? '))
    if meat_cost * meat_qty <= total_currency:
        running_total += meat_cost * meat_qty
        print(f'\nYour bill so far is: ${running_total:.2f}\n')
    else:
        print('\nInsufficient funds.\n')

    # Vegetables
    veg_cost = 4.00
    print(f'I charge ${veg_cost:.2f} for a bundle of Vegetables. I recommend you buy at least 8 bundles for a balanced diet.\n')
    veg_qty = int(input('How many bundles of Vegetables do you want to buy? '))
    if veg_cost * veg_qty <= total_currency:
        running_total += veg_cost * veg_qty
        print(f'\nYour bill so far is: ${running_total:.2f}\n')
    else:
        print('\nInsufficient funds.\n')

    # Cooking Oil
    oil_cost = 5.00
    print(f'I charge ${oil_cost:.2f} for a jar of Cooking Oil. I recommend you buy at least 3 jars for meal preparation.\n')
    oil_qty = int(input('How many jars of Cooking Oil do you want to buy? '))
    if oil_cost * oil_qty <= total_currency:
        running_total += oil_cost * oil_qty
        print(f'\nYour bill so far is: ${running_total:.2f}\n')
    else:
        print('\nInsufficient funds.\n')

    # Water Barrels
    water_cost = 2.00
    print(f'I charge ${water_cost:.2f} for a Water Barrel. I recommend you buy at least 10 barrels to keep your party hydrated.\n')
    water_qty = int(input('How many Water Barrels do you want to buy? '))
    if water_cost * water_qty <= total_currency:
        running_total += water_cost * water_qty
        print(f'\nYour bill so far is: ${running_total:.2f}\n')
    else:
        print('\nInsufficient funds.\n')

    # Total cost
    print(f'Your total bill is: ${running_total:.2f}\n')
    print(f'\nYou have ${total_currency - running_total:.2f} left to spend.\n')
    print("\nLet's get started!\n")

main()
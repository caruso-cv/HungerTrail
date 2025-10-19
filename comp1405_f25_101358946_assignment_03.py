# Name: Carmen Vacchio
# Student Number: 101358946

import updated_base_module_for_101358946 as base
import random

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

    # --- Draw everything to the display ---
    base.display_update()

    # --- Hold window open for 5 seconds ---
    base.hold_surf(500)

 
    # ---------------------- TERMINAL GAMEPLAY ----------------------

    # --- Intro text ---
    print('\nWelcome to The Hunger Trail!\n')
    print('In this game you will lead a group of travelers on a difficult journey.')
    print('You will need to make important decisions about food, supplies,')
    print('and survival as you face challenges along the way...\n')

    # --- Narrative/Learn more ---
    while True:
        res = input('Would you like to learn more (y/n)? ').lower()
        if res == 'yes' or res == 'y':
            print("\nIn The Hunger Trail, you take on the role of a traveling vendor navigating a difficult trade route during a food shortage. Along the way, you'll gather, prepare, and manage supplies to keep your caravan alive. Every decision — from how you ration ingredients to how you prepare meals — affects your success. The journey will test not just your survival instincts, but your understanding of proper food preparation and planning.")
            res = ''
            break
        elif res == 'no' or res == 'n':
            res = ''
            break
        else:
            print('\nInvalid entry\n')

    # --- Starting location & sub routes ---
    print('\n\n----- STARTING LOCATION -----\n')
    location_flag = True # boolean flag for validation loop

    # Post-condition, event controlled input validation loop
    while location_flag:
        location_sub_flag = True # boolean flag for validation loop
        print('1. Harveston Village\n2. Port Umber\n3. Stoneveil Crossing\n4. Learn more...\n')
        location_choice = input('Where would you like to start? ').strip()

        if location_choice == '4': # Learn more
            print('\n1. Harveston Village: fertile farmlands known for grain and produce.\n2. Port Umber: a coastal trade hub famous for spices and salted meat.\n3. Stoneveil Crossing: a mountain pass settlement that trades in dried goods and cooking oil.\n')
            location_choice = input('Where will it be traveller? ').strip()
        
        # Harveston Village branching control structure
        if location_choice == '1':
            while location_sub_flag:
                print('\n1. Millford Fields\n2. Oakbarrel Market\n3. Learn more...\n')
                sub_location = input('From Harveston, you can venture north to Millford or east to Oakbarrel? ').strip()

                if sub_location == '3': # learn more
                    print('\n1. Millford Fields: open farmland where you can stock up on grain and flour. Prices are lower, but weather exposure increases travel time.\n2. Oakbarrel Market: a rural trading post known for dairy and fresh produce. Offers better quality goods, but stock is limited.\n')
                    sub_location = input('Where will it be traveller? ').strip()

                if sub_location == '1': # sub-route chosen
                    starting_location = 'Harveston Village: Millford Fields'
                    location_flag = False
                    location_sub_flag = False

                elif sub_location == '2': # sub-route chosen
                    starting_location = 'Harveston Village: Oakbarrel Market'
                    location_flag = False
                    location_sub_flag = False
                
                else: # invalid sub-route, restart sub-loop
                    print('\nInvalid entry')
        
        # Port Umber branching control structure
        elif location_choice == '2':
            while location_sub_flag:
                print('\n1. Saltmar Wharf\n2. Old Bazaar District\n3. Learn more...\n')
                sub_location = input('Would you like to set course for Saltmar or inland toward the Old Bazaar District? ').strip()

                if sub_location == '3': # learn more
                    print('\n1. Saltmar Wharf: docks lined with fishermen and spice vendors. Great deals on meat and salt, but storage risk is high due to humidity.\n2. Old Bazaar District: a crowded marketplace with exotic ingredients and cooking oils. Prices fluctuate daily, but rare items can appear.\n')
                    sub_location = input('Where will it be traveller? ').strip()
                
                if sub_location == '1': # sub-route chosen
                    starting_location = 'Port Umber: Saltmar Wharf'
                    location_flag = False
                    location_sub_flag = False

                elif sub_location == '2': # sub-route chosen
                    starting_location = 'Port Umber: Old Bazaar District'
                    location_flag = False
                    location_sub_flag = False
                
                else: # invalid sub-route, restart sub-loop
                    print('\nInvalid entry')

        # Stoneveil Crossing
        elif location_choice == '3':
            starting_location = 'Stoneveil Crossing'
            location_flag = False
        
        # If invalid entry, restart the loop
        else:
            print('\nPlease enter a valid starting location.\n')

    # --- Departure Date ---
    print('\n\n----- DEPARTURE DATE -----\n')

    # Post-condition, event controlled input validation loop
    while True:
        print('1. March\n2. April\n3. June\n4. September\n5. November\n6. Learn more...\n')
        date_choice = input('Which date would you like to hit the trail? ').strip()

        if date_choice == '6': # Learn more
            print('\n1. March: early spring; mild weather, but few fresh supplies available.\n2. April: balanced season, average food spoilage rate.\n3. June: summer heat increases water loss and food spoilage.\n4. September: harvest season; abundant crops, but colder nights.\n5. November: early winter; limited produce but safer meat storage.\n')
            date_choice = input('Which date would you like? ').strip()

        # Branching control structure to determine valid departure date
        if date_choice == '1':
            departure_date = 'March'
            break
        elif date_choice == '2':
            departure_date = 'April'
            break
        elif date_choice == '3':
            departure_date = 'June'
            break
        elif date_choice == '4':
            departure_date = 'September'
            break
        elif date_choice == '5':
            departure_date = 'November'
            break
        else: 
            print('\nPlease enter a valid departure date.\n')

    print(f"\nYou'll be heading to {starting_location} on {departure_date} 1st")

    # --- Character Selection ---
    print('\n\n----- CHARACTER CLASSES -----\n')
    character_flag = True # boolean flag for validation loop

    # Post-condition, event controlled input validation loop
    while character_flag:
        print('1. Chef: expert in food preservation and efficient ingredient use.\n2. Merchant: skilled trader, negotiates better prices and inventory bonuses.\n3. Forager: gathers wild foods and finds water more easily on the trail.\n')
        character = input('Which character class would you like? ').strip()

        if character == '1':
            character = 'Chef'
            character_flag = False
        elif character == '2':
            character = 'Merchant'
            character_flag = False
        elif character == '3':
            character = 'Forager'
            character_flag = False
        else:
            print('\nPlease enter a valid character class.\n')

    print(f'\nYour character class is: {character}\n')

    # --- Buff/Debuff Stat ---
    stat = ''
    if character == 'Chef' or departure_date == 'November':
        stat = 'Buff: Food spoilage reduced by 30%'
        chef_stat_description = 'A skilled Chef knows how to cure, salt, and preserve ingredients. Your supplies will stay fresher for longer on the trail.\n'
        stat_description = 'The cold air of late November naturally slows decay. Your supplies will stay fresher for longer on the trail.\n'
    elif character == 'Merchant' and departure_date == 'March':
        stat = 'Buff: +15% starting funds'
        stat_description = 'Early spring is the start of the trading season — prices are low, and Merchants profit from offseason bulk deals.\n'
    elif character == 'Forager' and departure_date == 'September':
        stat = 'Buff: +20% materials gathered'
        stat_description = "Late-harvest season means wild fruits, mushrooms, and roots are plentiful, making it ideal for a Forager's skillset.\n"
    elif character == 'Merchant' and departure_date == 'June':
        stat = 'Debuff: Water costs +25%'
        stat_description = "Hot summer routes make water scarce and expensive, cutting into a Merchant's profit margins.\n"
    
    if stat:
        print('\n----- CHARACTER STAT -----\n')
        if character == 'Chef':
            print(f'{chef_stat_description}\n    • {stat}\n')
        else:
            print(f'{stat_description}\n    • {stat}\n')

    # --- Party names ---
    print('\n----- PARTY -----\n')
    while True:
        players = [] # init list (clear list if loop reset)
        leader = input('What is the first name of the party leader? ') # get leaders name
        players.append(leader)

        print('\nWhat are the first names of the four other members in your party?\n')
        print(f'  1. {leader}')
        
        # For loop to display/store players
        for i in range(2,6):
            players.append(input(f'  {i}. '))
        res = input('\nAre the names entered correct (y/n)?: ').strip().lower()
        if res == 'y' or res == 'yes':
            break

        print('') # empty space

    # --- Arithmetic pipeline for supplies ---
    print('\n\n----- SUPPLIES -----\n')
    total_currency = 101358946  # starting money = student number
    running_total = 0
    supplies_flag = True

    # Post condition input validation loop
    while supplies_flag:
        print(f"Before leaving you should buy equipment and supplies. You have ${total_currency:.2f} in cash, but you don't have to spend it all now.\n")

        # Flour
        print('\nSTACKS OF FLOUR\n')
        flour_cost = 3.00
        print(f'I charge ${flour_cost:.2f} for a sack of Flour. I recommend you buy at least 10 sacks so you can bake enough bread.\n')
        flour_qty = int(input('How many sacks of Flour do you want to buy? '))
        total_flour = flour_cost * flour_qty
        if total_flour <= total_currency - running_total :
            running_total += total_flour
            print(f'\nYour bill so far is: ${running_total:.2f}\n')
        else:
            print('\nInsufficient funds.\n')

        # Meat
        print('\nPORTIONS OF MEAT\n')
        meat_cost = 8.00
        print(f'I charge ${meat_cost:.2f} for a portion of Meat. I recommend you buy at least 5 portions for protein.\n')
        meat_qty = int(input('How many portions of Meat do you want to buy? '))
        total_meat = meat_cost * meat_qty
        if total_meat <= total_currency - running_total:
            running_total += total_meat
            print(f'\nYour bill so far is: ${running_total:.2f}\n')
        else:
            print('\nInsufficient funds.\n')

        # Vegetables
        print('\nBUNDLES OF VEGETABLES\n')
        veg_cost = 4.00
        print(f'I charge ${veg_cost:.2f} for a bundle of Vegetables. I recommend you buy at least 8 bundles for a balanced diet.\n')
        veg_qty = int(input('How many bundles of Vegetables do you want to buy? '))
        total_veg = veg_cost * veg_qty
        if total_veg <= total_currency - running_total:
            running_total += total_veg
            print(f'\nYour bill so far is: ${running_total:.2f}\n')
        else:
            print('\nInsufficient funds.\n')

        # Cooking Oil
        print('\nJARS OF COOKING OIL\n')
        oil_cost = 5.00
        print(f'I charge ${oil_cost:.2f} for a jar of Cooking Oil. I recommend you buy at least 3 jars for meal preparation.\n')
        oil_qty = int(input('How many jars of Cooking Oil do you want to buy? '))
        total_oil = oil_cost * oil_qty
        if total_oil <= total_currency - running_total:
            running_total += total_oil
            print(f'\nYour bill so far is: ${running_total:.2f}')
        else:
            print('\nInsufficient funds.')

        # Water Barrels
        print('\n\nBARRELS OF WATER\n')
        water_cost = 2.00
        print(f'I charge ${water_cost:.2f} for a Water Barrel. I recommend you buy at least 10 barrels to keep your party hydrated.\n')
        water_qty = int(input('How many Water Barrels do you want to buy? '))
        total_water = water_cost * water_qty
        if total_water <= total_currency - running_total:
            running_total += total_water
            print(f'\nYour bill so far is: ${running_total:.2f}\n')
        else:
            print('\nInsufficient funds.\n')

        # Transaction input validation
        while True:
            # Running total
            print('\nYOUR BASKET\n')
            print(f'The items in your basket are:\n\n{flour_qty}x Stacks of flour: ${total_flour:.2f}\n{meat_qty}x Portions of meat: ${total_meat:.2f}\n{veg_qty}x Bundles of vegetables: ${total_veg:.2f}\n{oil_qty}x Jars of cooking oil: ${total_oil:.2f}\n{water_qty}x Barrels of water: ${total_water:.2f}\n')

            print(f'Your total bill is: ${running_total:.2f} which will leave you with ${total_currency - running_total:.2f} left to spend.\n')
            transaction_validation = input('Do you wish to proceed with this transaction (y/n)? ').strip().lower()

            if transaction_validation == 'y' or transaction_validation == 'yes':
                supplies_flag = False
                break

            elif transaction_validation == 'n' or transaction_validation == 'no':
                running_total = 0
                break

            else:
                print('\nInvalid entry\n')

    print("\nLet's get started!\n")


    # ---------------------- MAIN GAME LOOP ----------------------
    # Open window
    base.open_surf('The Hunger Trail')

    # Load smaller in-game font
    base.set_smaller_text_font("Kenney Mini Square.ttf")

    # Load in the sprite
    wagon = base.read_sprite('wagon_sprite_for_101358946.png')

    # Distance and wagon position variables
    distance = 900
    wagon_x, wagon_y = 460, 290

    # Road colours
    road = (34, 114, 122)
    road2 = (54, 137, 145)

    while True:

        # Random step counter
        step = random.randint(3, 9)

        # Exit condition if user presses key
        if base.was_any_key_pressed():
            break

        # Gradual decrease to distance
        distance = distance - step
        if distance < 0:
            distance = 0

        # Move wagon gradually left as distance decreases
        wagon_x = 460 * (distance / 900)

        # Draw background and variable distance to landmark
        base.fill_surf(18, 83, 89)
        base.render_smaller_text((18, 83, 89), 10, 320, f"Distance to starting location: {distance}", 60, 24, colour)

        # -- Draw road -- 
        # Outer lines
        base.draw_line((0, 320), (640, 320), road, 4)
        base.draw_line((0, 400), (640, 400), road, 4)

        # Inner lines
        base.draw_line((0, 360), (20, 360), road2, 4)
        base.draw_line((40, 360), (60, 360), road2, 4)
        base.draw_line((80, 360), (100, 360), road2, 4)
        base.draw_line((120, 360), (140, 360), road2, 4)
        base.draw_line((160, 360), (180, 360), road2, 4)
        base.draw_line((200, 360), (220, 360), road2, 4)
        base.draw_line((240, 360), (260, 360), road2, 4)
        base.draw_line((280, 360), (300, 360), road2, 4)
        base.draw_line((320, 360), (340, 360), road2, 4)
        base.draw_line((360, 360), (380, 360), road2, 4)
        base.draw_line((400, 360), (420, 360), road2, 4)
        base.draw_line((440, 360), (460, 360), road2, 4)
        base.draw_line((480, 360), (500, 360), road2, 4)
        base.draw_line((520, 360), (540, 360), road2, 4)
        base.draw_line((560, 360), (580, 360), road2, 4)
        base.draw_line((600, 360), (620, 360), road2, 4)
        base.draw_line((640, 360), (660, 360), road2, 4)

        # Draw wagon
        base.blit_image(wagon, wagon_x, wagon_y)

        # Show frame then delay
        base.display_update()
        base.wait_pause(80)  

        # Exit loop when distance is 0
        if distance == 0:
            break

    print(f"Welcome to {starting_location}!")

main()
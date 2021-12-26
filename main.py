from numpy import true_divide
import pyautogui
import time
from position_parser import Parser
import map_finder
import keyboard

time.sleep(3)

game_counter = 0
map = None
finding_game = False
detected_map = False
p = Parser()

while True:
        # The variables and click function are seperated for readability
        battle_button_coords = pyautogui.locateOnScreen('data/images/buttons/battle-button.png', confidence = 0.6)
        hero_button_coords = pyautogui.locateOnScreen('data/images/buttons/hero-selection-button.png', confidence = 0.6)
        tower_button_coords = pyautogui.locateOnScreen('data/images/buttons/battle-button.png', confidence = 0.6)
        tower_screen_detect = pyautogui.locateOnScreen('data/images/buttons/tower-screen.png', confidence = 0.6)

        # Clicks the "Battle" button in the main menu
        if battle_button_coords != None and not finding_game:
            pyautogui.click(battle_button_coords)
            pyautogui.move(100, 100)
            finding_game = True
            print("Finding a game...")
            time.sleep(2)

        # Clicks the "Ready" button in hero selection
        elif hero_button_coords != None:
            pyautogui.click(hero_button_coords)
            print("Hero selected")
            time.sleep(2)

        # Clicks the "Battle" button in tower selection
        elif tower_screen_detect != None and not detected_map:
            map = map_finder.get_map()

            pyautogui.click(tower_button_coords)
            detected_map = True
            finding_game = False
            print("Ready for game!")
            print("Playing on: " + map)
            time.sleep(2)

        back_button_coords = pyautogui.locateOnScreen('data/images/buttons/back-button.png', confidence = 0.6)
        if back_button_coords != None:
            pyautogui.click(back_button_coords)
            print("back button")
            time.sleep(2)

        try_again_button_coords = pyautogui.locateOnScreen('data/images/buttons/try-again-button.png', confidence = 0.6)
        if try_again_button_coords != None:
            pyautogui.click(try_again_button_coords)
            print("try again button")
            time.sleep(2)

        quit_button_coords = pyautogui.locateOnScreen('data/images/buttons/quit-button.png', confidence = 0.6)
        if quit_button_coords != None:
            pyautogui.click(quit_button_coords)
            print("quit button")
            time.sleep(2)

        ok_button_coords = pyautogui.locateOnScreen('data/images/buttons/ok-button.png', confidence = 0.8)
        if ok_button_coords != None:
            pyautogui.click(ok_button_coords)
            game_counter += 1
            print("Game Finished")
            time.sleep(2)

        is_right_side = None

        while pyautogui.locateOnScreen('data/images/ingame/surrender-button.png', confidence = 0.7) != None:
            detected_map = False
            finding_game = False
            if is_right_side == None:
                while pyautogui.locateOnScreen('data/images/ingame/locked-bloon.png', confidence = 0.7) == None:
                    time.sleep(1)
                time.sleep(3)

                print(pyautogui.locateCenterOnScreen('data/images/ingame/locked-bloon.png', confidence = 0.7)[0])
                is_right_side = pyautogui.locateCenterOnScreen('data/images/ingame/locked-bloon.png', confidence = 0.7)[0] > 960

                print(is_right_side)
                offset = 0 if is_right_side else 800
                tower_slot_x = 1790 if is_right_side else 130
                print("Playing on the " + ("right" if is_right_side else "left") + " side")
                time.sleep(1)

            
            for pos in p.get_positions(map, 'right' if is_right_side else 'left'):
                pyautogui.moveTo(tower_slot_x, 230)
                time.sleep(0.2)
                pyautogui.dragTo(pos[0], pos[1], 0.8, button='left')
                
            blue_bloon_coords = pyautogui.locateOnScreen('data/images/ingame/blue-bloon.png', confidence = 0.7)
            purple_bloon_coords = pyautogui.locateOnScreen('data/images/ingame/purple-bloons.png', confidence = 0.7)
            

            if purple_bloon_coords != None:

                print("Round 11 - Attempting to rush with purples")

                # Activate Bloon boost
                bloon_boost_coords = pyautogui.locateOnScreen('data/images/ingame/bloon-boost.png', confidence = 0.7)
                pyautogui.click(bloon_boost_coords)
                time.sleep(0.4)

                # Click the purple bloons
                for _ in range(100):
                    pyautogui.click(purple_bloon_coords)
                    time.sleep(0.05)
            else:
                for _ in range(8):
                    pyautogui.click(blue_bloon_coords)
                    time.sleep(0.05)

            time.sleep(2)

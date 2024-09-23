# Imports...
import c
import g
import event as ev
import presentation as pres
import surface_sprites as sfsp
import detect as det
import os
import threading as th



# Basics...
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sc = g.play()
in_menu = True
in_credits = False
in_inst = False
in_scene = False
my_game_works = False

# Presentation...
pres.cap("Assassin")

# Time...
clock = g.pg.time.Clock()
last = 0
last_c1 = last
last_c2 = last
last_h = last
last_alm = last
last_s0 = last
last_s1 = last
last_s2 = last
last_s3 = last
last_sh = last
last_ch = last
fight_start = last

# Surfaces...
surf = sfsp.get()

# Mouse...
mouse_pressed = False
scroll_up = False
scroll_down = False

# Threading flag...
thread = [True]

# Custom events...
HEAR = g.pg.USEREVENT + 1
READ = g.pg.USEREVENT + 2
read_event = g.pg.event.Event(READ)
listening = [False]
thread_listen = th.Thread(target=det.listen, args=(HEAR, listening, thread))
reading = [False]
kyu = g.qu.Queue()
thread_read = th.Thread(target=det.read, args=(kyu, reading, thread,))
hearing = False

# Threading...
thread_listen.start()
thread_read.start()

# Static sprite sheets...
hand = g.pg.image.load('./assets/Hand.png')
for x in range(1, 15):
    globals()[f'hand{x}'] = sfsp.sp_get(hand, (0, 0), x-1, 1/(3*32)*g.np.mean([g.c.W, g.c.H]), (0, 0, 0))
hand_frames = [globals()[f'hand{x}'] for x in range(1, 15)]
hand_frame = 0

assasin_hand2hand = g.pg.image.load('./assets/Hand2handAssassin.png')
for x in range(1, 40):
    globals()[f'assasin_hand2hand{x}'] = sfsp.sp_get(assasin_hand2hand, (0, 0), x-1, 1/(3*32)*g.np.mean([g.c.W, g.c.H]), (0, 0, 0))
assasin_hand2hand_frames = [globals()[f'assasin_hand2hand{x}'] for x in range(1, 40)]
hand2hand_frame = 0
hand2hand_factor = 0

assasin_gun = g.pg.image.load('./assets/GunAssassin.png')
for x in range(1, 40):
    globals()[f'assasin_gun{x}'] = sfsp.sp_get(assasin_gun, (0, 0), x-1, 1/(3*32)*g.np.mean([g.c.W, g.c.H]), (0, 0, 0))
assasin_gun_frames = [globals()[f'assasin_gun{x}'] for x in range(1, 40)]
gun_frame = 0
gun_factor = 0

assasin_blade = g.pg.image.load("./assets/BladeAssassin.png")
for x in range(1, 40):
    globals()[f'assasin_blade{x}'] = sfsp.sp_get(assasin_blade, (0, 0), x-1, 1/(3*32)*g.np.mean([g.c.W, g.c.H]), (0, 0, 0))
assasin_blade_frames = [globals()[f'assasin_blade{x}'] for x in range(1, 40)]
blade_frame = 0
blade_factor = 0


assasin_choose = g.pg.image.load('./assets/ChooseAssassin.png')
for x in range(1, 19):
    globals()[f'assasin_choose{x}'] = sfsp.sp_get(assasin_choose, (0, 0), x-1, 1/(3*32)*g.np.mean([g.c.W, g.c.H]), (0, 0, 0))
assasin_choose_frames = [globals()[f'assasin_choose{x}'] for x in range(1, 19)]
choose_frame = 0

assasin_caught = g.pg.image.load('./assets/CaughtAssassin.png')
for x in range(1, 13):
    globals()[f'assasin_caught{x}'] = sfsp.sp_get(assasin_caught, (0, 0), x-1, 1/(3*32)*g.np.mean([g.c.W, g.c.H]), (0, 0, 0))
assasin_caught_frames = [globals()[f'assasin_caught{x}'] for x in range(1, 13)]
caught_frame = 0
caught_factor = 0

mob_death = g.pg.image.load('./assets/MobDies.png')
for x in range(1, 40):
    globals()[f'mob_death{x}'] = sfsp.sp_get(mob_death, (0, 0), x-1, 1/68*g.np.mean([g.c.W, g.c.H]), (0, 0, 0))
mob_death_frames = [globals()[f'mob_death{x}'] for x in range(1, 40)]
mob_death_frame = 0

mob_poisoned = g.pg.image.load('./assets/MobPoisoned.png')
for x in range(1, 30):
    globals()[f'mob_poisoned{x}'] = sfsp.sp_get(mob_poisoned, (0, 0), x-1, 1/68 *g.np.mean([g.c.W, g.c.H]), (0, 0, 0))
mob_poisoned_frames = [globals()[f'mob_poisoned{x}'] for x in range(1, 30)]
mob_poisoned_frame = 0

mob_catch = g.pg.image.load('./assets/MobAlert.png')
for x in range(1, 13):
    globals()[f'mob_catch{x}'] = sfsp.sp_get(mob_catch, (0, 0), x-1, 1/68 *g.np.mean([g.c.W, g.c.H]), (0, 0, 0))
mob_catch_frames = [globals()[f'mob_catch{x}'] for x in range(1, 13)]
catch_frame = 0
catch_factor = 0

# Static sprites...
cards = g.pg.sprite.Group()
cards2 = g.pg.sprite.Group()
letters = ['J', 'Q', 'K']
for i in range(2, 14):
    if i > 10:
        globals()[f'c_{letters[i - 11]}'] = sfsp.Card(f"./assets/PNG-cards-1.3/c_{letters[i - 11]}.png")
        globals()[f'd_{letters[i - 11]}'] = sfsp.Card(f"./assets/PNG-cards-1.3/d_{letters[i - 11]}.png")
        globals()[f'h_{letters[i - 11]}'] = sfsp.Card(f"./assets/PNG-cards-1.3/h_{letters[i - 11]}.png")
        globals()[f's_{letters[i - 11]}'] = sfsp.Card(f"./assets/PNG-cards-1.3/s_{letters[i - 11]}.png")
        globals()[f'c_{letters[i - 11]}2'] = sfsp.Card2(f"./assets/PNG-cards-1.3/c_{letters[i - 11]}.png")
        globals()[f'd_{letters[i - 11]}2'] = sfsp.Card2(f"./assets/PNG-cards-1.3/d_{letters[i - 11]}.png")
        globals()[f'h_{letters[i - 11]}2'] = sfsp.Card2(f"./assets/PNG-cards-1.3/h_{letters[i - 11]}.png")
        globals()[f's_{letters[i - 11]}2'] = sfsp.Card2(f"./assets/PNG-cards-1.3/s_{letters[i - 11]}.png")
        continue
    globals()[f'c_{i}'] = sfsp.Card(f"./assets/PNG-cards-1.3/c_{i}.png")
    globals()[f'd_{i}'] = sfsp.Card(f"./assets/PNG-cards-1.3/d_{i}.png")
    globals()[f'h_{i}'] = sfsp.Card(f"./assets/PNG-cards-1.3/h_{i}.png")
    globals()[f's_{i}'] = sfsp.Card(f"./assets/PNG-cards-1.3/s_{i}.png")
    globals()[f'c_{i}2'] = sfsp.Card2(f"./assets/PNG-cards-1.3/c_{i}.png")
    globals()[f'd_{i}2'] = sfsp.Card2(f"./assets/PNG-cards-1.3/d_{i}.png")
    globals()[f'h_{i}2'] = sfsp.Card2(f"./assets/PNG-cards-1.3/h_{i}.png")
    globals()[f's_{i}2'] = sfsp.Card2(f"./assets/PNG-cards-1.3/s_{i}.png")

twos, threes, fours, fives, sixes, sevens, eights, nines, tens, jacks, queens, kings = [c_2, d_2, h_2, s_2], [c_3, d_3, h_3, s_3], [c_4, d_4, h_4, s_4], [c_5, d_5, h_5, s_5], [c_6, d_6, h_6, s_6], [c_7, d_7, h_7, s_7], [c_8, d_8, h_8, s_8], [c_9, d_9, h_9, s_9], [c_10, d_10, h_10, s_10], [c_J, d_J, h_J, s_J], [c_Q, d_Q, h_Q, s_Q], [c_K, d_K, h_K, s_K]
temp = [twos, threes, fours, fives, sixes, sevens, eights, nines, tens, jacks, queens, kings]
clubs, diams, hears, spads = [], [], [], []
for group in temp:
    clubs.append(group[0])
    diams.append(group[1])
    hears.append(group[2])
    spads.append(group[3])
card_list = [clubs, diams, hears, spads]
twos2, threes2, fours2, fives2, sixes2, sevens2, eights2, nines2, tens2, jacks2, queens2, kings2 = [c_22, d_22, h_22, s_22], [c_32, d_32, h_32, s_32], [c_42, d_42, h_42, s_42], [c_52, d_52, h_52, s_52], [c_62, d_62, h_62, s_62], [c_72, d_72, h_72, s_72], [c_82, d_82, h_82, s_82], [c_92, d_92, h_92, s_92], [c_102, d_102, h_102, s_102], [c_J2, d_J2, h_J2, s_J2], [c_Q2, d_Q2, h_Q2, s_Q2], [c_K2, d_K2, h_K2, s_K2]
temp = [twos2, threes2, fours2, fives2, sixes2, sevens2, eights2, nines2, tens2, jacks2, queens2, kings2]
clubs2, diams2, hears2, spads2 = [], [], [], []
for group in temp:
    clubs2.append(group[0])
    diams2.append(group[1])
    hears2.append(group[2])
    spads2.append(group[3])
card_list2 = [clubs2, diams2, hears2, spads2]
symbol = None
num = 0
symbol2 = None
num2 = 0

# Gameplay and misc...
silence = True
almost = False
last_temp = last
read_animation = False

# MAIN LOOP...
while my_game_works or in_credits or in_menu or in_inst or in_scene:

    # Check events...
    for event in ev.get():
        if event.type == g.pg.KEYDOWN:
            if event.key == g.pg.K_z and g.c.z_rel:
                g.c.z = True
                g.c.z_rel = False
        elif event.type == g.pg.KEYUP:
            if event.key == g.pg.K_z:
                g.c.z = False
                g.c.z_rel = True

        if event.type == g.pg.KEYDOWN:
            if event.key == g.pg.K_x and g.c.x_rel:
                g.c.x = True
                g.c.x_rel = False
        elif event.type == g.pg.KEYUP:
            if event.key == g.pg.K_x:
                g.c.x = False
                g.c.x_rel = True

        if event.type == g.pg.KEYDOWN:
            if event.key == g.pg.K_n and g.c.n_rel:
                g.c.n = True
                g.c.n_rel = False
        elif event.type == g.pg.KEYUP:
            if event.key == g.pg.K_n:
                g.c.n = False
                g.c.n_rel = True

        if event.type == g.pg.QUIT:
            g.q()
            thread[0] = False
            my_game_works, in_menu, in_credits, in_inst, in_scene, fight_start = False, False, False, False, False, False

        if event.type == g.pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pressed = True
            elif event.button == 4:
                scroll_up = True
            elif event.button == 5:
                scroll_down = True
        elif event.type == g.pg.MOUSEBUTTONUP:
            if event.button == 1:
                mouse_pressed = False

        if event.type == HEAR:
            if my_game_works:
                hearing = True

        if event.type == READ:
            reading[0] = True

    # If we haven't quit...

    # Scene...
    if in_scene:
        listening[0] = False

        # Fill backgrounds...
        surf["Scene"]["Sky"].fill((75, 25, 100))
        surf["Scene"]["Floor"].fill((100, 100, 100))

        # Place static backgrounds...
        for bg in surf["Scene"]:
            # Place nested dictionaries...
            if type(surf["Scene"][bg]) == dict:
                for part in surf["Scene"][bg]:
                    if not part[:4] == 'loc_':
                        sc.blit(surf["Scene"][bg][part], surf["Scene"][bg]["loc_" + part])
            elif not bg[:4] == 'loc_':
                sc.blit(surf["Scene"][bg], surf["Scene"]["loc_" + bg])


        # Place dynamic backgrounds...
        if read_animation:
            sc.blit(assasin_choose_frames[choose_frame],
                    (2 * g.c.W / 3 - 32 - 170, 2 * g.c.H / 3 - 82))
            now = g.pg.time.get_ticks()
            if now - last_ch >= 3*g.c.SCENE/4:
                choose_frame += 1
                last_ch = now

            # Finding out if it's the end of the animation...
            if choose_frame == 18:
                in_scene = False
                my_game_works = True
                choose_frame = 0
                g.c.z_rel = True
                g.pg.event.post(read_event)
                read_animation = False

        elif not silence:
            sc.blit(assasin_caught_frames[caught_frame],
                    (2 * g.c.W / 3 - 32 - 170 + caught_factor * 10, 2 * g.c.H / 3 - 32))
            sc.blit(mob_catch_frames[catch_frame], (2 * g.c.W / 3 - 55, 2 * g.c.H / 3 - 125))
            now = g.pg.time.get_ticks()
            if now - last_sh >= g.c.SCENE:
                caught_frame += 1
                catch_frame += 1
                last_sh = now
                if caught_frame < 9:
                    caught_factor += 1
                else:
                    caught_factor = 9

            # Finding out if it's the end of the animation...
            if caught_frame == 12 or catch_frame == 12:
                in_scene = False
                my_game_works = True
                catch_frame = 0
                caught_frame = 0
                caught_factor = 0
                fight_start = g.pg.time.get_ticks()
                silence = True
                almost = False
                hearing = False
                reading[0] = False

        elif symbol == 0:
            sc.blit(assasin_gun_frames[gun_frame],
                    (2 * g.c.W / 3 - 32 - 170 + gun_factor * 10, 2 * g.c.H / 3 - 32))
            sc.blit(mob_death_frames[mob_death_frame], (2 * g.c.W / 3 - 55, 2 * g.c.H / 3 - 125))
            now = g.pg.time.get_ticks()
            if now - last_s0 >= g.c.SCENE:
                gun_frame += 1
            if now - last_s0 >= g.c.SCENE:
                mob_death_frame += 1
                last_s0 = now
            if gun_frame < 9:
                gun_factor = gun_frame
            else:
                gun_factor = 9

            # Finding out if it's the end of the animation...
            if gun_frame == 39 or mob_death_frame == 39:
                in_scene = False
                my_game_works = True
                mob_death_frame = 0
                gun_frame = 0
                last_s0 = 0

        elif symbol == 1:
            sc.blit(assasin_blade_frames[blade_frame],
                    (2 * g.c.W / 3 - 32 - 170 + blade_factor * 10, 2 * g.c.H / 3 - 32))
            sc.blit(mob_death_frames[mob_death_frame], (2 * g.c.W / 3 - 55, 2 * g.c.H / 3 - 125))
            now = g.pg.time.get_ticks()
            if now - last_s1 >= g.c.SCENE:
                blade_frame += 1
            if now - last_s1 >= g.c.SCENE:
                mob_death_frame += 1
                last_s1 = now
            if blade_frame < 18:
                blade_factor = blade_frame
            else:
                blade_factor = 18

            # Finding out if it's the end of the animation...
            if blade_frame == 39 or mob_death_frame == 39:
                in_scene = False
                my_game_works = True
                mob_death_frame = 0
                blade_frame = 0
                last_s1 = 0

        elif symbol == 2:
            sc.blit(assasin_hand2hand_frames[hand2hand_frame], (2 * g.c.W / 3 - 32 - 170 + hand2hand_factor * 10, 2 * g.c.H / 3 - 32))
            sc.blit(mob_death_frames[mob_death_frame], (2 * g.c.W / 3 - 55, 2 * g.c.H / 3 -125))
            now = g.pg.time.get_ticks()
            if now - last_s2 >= g.c.SCENE:
                hand2hand_frame += 1
            if now - last_s2 >= g.c.SCENE:
                mob_death_frame += 1
                last_s2 = now
            if hand2hand_frame < 18:
                hand2hand_factor = hand2hand_frame
            else:
                hand2hand_factor = 18

            # Finding out if it's the end of the animation...
            if hand2hand_frame == 39 or mob_death_frame == 39:
                in_scene = False
                my_game_works = True
                mob_death_frame = 0
                hand2hand_frame = 0
                last_s2 = 0

        elif symbol == 3:
            sc.blit(mob_poisoned_frames[mob_poisoned_frame], (2 * g.c.W / 3 - 55, 2 * g.c.H / 3 - 125))
            now = g.pg.time.get_ticks()
            if now - last_s3 >= g.c.SCENE:
                mob_poisoned_frame += 1
                last_s3 = now
            if mob_poisoned_frame == 29:
                in_scene = False
                my_game_works = True
                g.c.enter = False
                g.c.enter_rel = True
                mob_poisoned_frame = 0
                last_s3 = 0

        # Update screen and time...
        clock.tick(g.c.FR)
        g.upd()

    # Game...
    if my_game_works:
        if not silence:
            in_scene = True
            my_game_works = False
            continue
        # Fill backgrounds...
        surf["SBackground"]["Wall"].fill((25, 25, 25))
        surf["SBackground"]["Table"].fill((150, 75, 0))
        for item in surf["SBackground"]["Texture"]:
            if item[:4] == 'Slot':
                surf["SBackground"]["Texture"][item].fill('Black')

        # Place static backgrounds...
        for bg in surf["SBackground"]:
            # Place nested dictionaries...
            if type(surf["SBackground"][bg]) == dict:
                for part in surf["SBackground"][bg]:
                    if not part[:4] == 'loc_' and not part[:5] == 'rect_':
                        sc.blit(surf["SBackground"][bg][part], surf["SBackground"][bg]["loc_" + part])
            elif not bg[:4] == 'loc_' and not bg[:5] == 'rect_':
                sc.blit(surf["SBackground"][bg], surf["SBackground"]["loc_" + bg])

        # Place dynamic backgrounds...
        # Fight?
        now = g.pg.time.get_ticks()
        if fight_start:

            # Stop listening...
            listening[0] = False

            # Place dynamic backgrounds...
            sc.blit(sfsp.words(30, "Press x to ATTACK/DEFEND", "Green"), surf["DBackground"]["loc_Assassinate"])
            sc.blit(surf["DBackground"]["Detect"], surf["DBackground"]["loc_Detect"])
            sc.blit(surf["DBackground"]["Mob_Detect"], surf["DBackground"]["loc_Mob_Detect"])
            sc.blit(surf["DBackground"]["Mob_Attack"], surf["DBackground"]["loc_Mob_Attack"])

            # Assassin's attacks\defenses...
            if g.c.n:
                g.pg.event.post(read_event)
                g.c.n = False
                g.c.n_rel = True

                if not kyu.empty():
                    symbol2 = kyu.get_nowait()
                    num2 = kyu.get_nowait()
                    reading[0] = False

                if (symbol2 == 0 or symbol2 == 1 or symbol2 == 2 or symbol2 == 3):
                    cards2.empty()
                    cards2.add(card_list2[symbol2][num2])

            if g.c.z:
                g.pg.event.post(read_event)
                g.c.z = False
                g.c.z_rel = True

                if not kyu.empty():
                    symbol = kyu.get_nowait()
                    num = kyu.get_nowait()
                    reading[0] = False

                if (symbol == 0 or symbol == 1 or symbol == 2 or symbol == 3):
                    cards.empty()
                    cards.add(card_list[symbol][num])

            # Fight duration ends...
            if now - fight_start >= g.c.FIGHT:
                my_game_works = False
                in_menu = True
                continue
        else:
            # for now, we assume no time passes between two iterations, and last_h and last_alm are == now, even if now was updated and they were updated only last iteration of the game loop
            if not hearing and not almost:
                if (symbol == 0 or symbol == 1 or symbol == 2 or symbol == 3):
                    sc.blit(surf["DBackground"]["Assassinate"], surf["DBackground"]["loc_Assassinate"])
                sc.blit(surf["DBackground"]["Detect"], surf["DBackground"]["loc_Detect"])
                listening[0] = True
                last_h = now
            elif hearing and not almost:
                sc.blit(surf["DBackground"]["Alert"], surf["DBackground"]["loc_Alert"])
                listening[0] = False
                if now - last_h >= g.c.BACKSWING:
                    hearing = False
                    almost = True
                    last_alm = now
            elif not hearing and almost:
                listening[0] = True
                sc.blit(surf["DBackground"]["Alert"], surf["DBackground"]["loc_Alert"])
                if now - last_alm >= g.c.ALERT:
                    almost = False
                    hearing = False
            else:
                silence = False
        if now - last >= g.c.HAND:
            hand_frame += 1
            last = now
            if hand_frame > 13:
                hand_frame = 0
        sc.blit(hand_frames[hand_frame], (2*g.c.W/3, 2*g.c.H/3 - 30))

        # Place cards...
        now = g.pg.time.get_ticks()
        if g.c.z and not fight_start:
            kyu.queue.clear()
            in_scene = True
            my_game_works = False
            g.c.z = False
            g.c.z_rel = True
            read_animation = True
            continue

        if not kyu.empty() and not fight_start:
            symbol = kyu.get_nowait()
            num = kyu.get_nowait()
            reading[0] = False

        if (symbol == 0 or symbol == 1 or symbol == 2 or symbol == 3) and not fight_start:
            cards.empty()
            cards.add(card_list[symbol][num])

        if g.c.x and (symbol == 0 or symbol == 1 or symbol == 2 or symbol == 3) and not hearing and not almost and not fight_start:
            in_scene = True
            my_game_works = False
            start_s = now
            mouse_pressed = False
            continue

        cards.draw(sc)
        cards2.draw(sc)

        # Quitting?...
        now = g.pg.time.get_ticks()
        if surf["SBackground"]['rect_Quit'].collidepoint(g.pg.mouse.get_pos()) and mouse_pressed:
            my_game_works = False
            in_menu = True
            mouse_pressed = False
            symbol = None
            reading[0] = True
            num = 0
            cards.empty()

        # Update screen and time...
        clock.tick(g.c.FR)
        g.upd()


    # Credits...
    if in_credits:
        # Fill backgrounds...
        surf["Credits"]["Wall"].fill((25, 25, 25))

        # Place static backgrounds...
        for bg in surf["Credits"]:
            # Place nested dictionaries...
            if type(surf["Credits"][bg]) == dict:
                for part in surf["Credits"][bg]:
                    if not part[:4] == 'loc_':
                        sc.blit(surf["Credits"][bg][part], surf["Credits"][bg]["loc_" + part])
            elif not bg[:4] == 'loc_':
                sc.blit(surf["Credits"][bg], surf["Credits"]["loc_" + bg])

        # Out of credits...
        if mouse_pressed:
            g.c.enter_rel = False
            in_credits = False
            in_menu = True
            mouse_pressed = False

        # Update screen and time...
        clock.tick(g.c.FR)
        g.upd()

    # Menu...
    if in_menu:
        # Fill backgrounds...
        surf["Menu"]["Wall"].fill((25, 25, 25))

        # Place static backgrounds...
        for bg in surf["Menu"]:
            # Place nested dictionaries...
            if type(surf["Menu"][bg]) == dict:
                for part in surf["Menu"][bg]:
                    if not part[:4] == 'loc_' and not part[:5] == 'rect_':
                        sc.blit(surf["Menu"][bg][part], surf["Menu"][bg]["loc_" + part])
            elif not bg[:4] == 'loc_' and not bg[:5] == 'rect_':
                sc.blit(surf["Menu"][bg], surf["Menu"]["loc_" + bg])

        # Out of menu...
        if surf["Menu"]['rect_Play'].collidepoint(g.pg.mouse.get_pos()) and mouse_pressed:
            my_game_works = True
            in_menu = False
            mouse_pressed = False

        if surf["Menu"]['rect_Credits'].collidepoint(g.pg.mouse.get_pos()) and mouse_pressed:
            in_credits = True
            in_menu = False
            mouse_pressed = False

        # Update screen and time...
        clock.tick(g.c.FR)
        g.upd()


# Close threads...
thread_listen.join()
thread_read.join()
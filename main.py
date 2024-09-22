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
thread_listen = th.Thread(target=det.listen, args=(HEAR, in_scene, thread))
kyu = g.qu.Queue()
reading = False
thread_read = th.Thread(target=det.read, args=(kyu,reading,READ,))
hearing = False

# Threading...
thread_listen.start()

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
c_2 = sfsp.Card("./assets/PNG-cards-1.3/2_of_clubs.png")
d_2 = sfsp.Card("./assets/PNG-cards-1.3/2_of_diamonds.png")
h_2 = sfsp.Card("./assets/PNG-cards-1.3/2_of_hearts.png")
s_2 = sfsp.Card("./assets/PNG-cards-1.3/2_of_spades.png")
c_3 = sfsp.Card("./assets/PNG-cards-1.3/3_of_clubs.png")
d_3 = sfsp.Card("./assets/PNG-cards-1.3/3_of_diamonds.png")
h_3 = sfsp.Card("./assets/PNG-cards-1.3/3_of_hearts.png")
s_3 = sfsp.Card("./assets/PNG-cards-1.3/3_of_spades.png")
c_4 = sfsp.Card("./assets/PNG-cards-1.3/4_of_clubs.png")
d_4 = sfsp.Card("./assets/PNG-cards-1.3/4_of_diamonds.png")
h_4 = sfsp.Card("./assets/PNG-cards-1.3/4_of_hearts.png")
s_4 = sfsp.Card("./assets/PNG-cards-1.3/4_of_spades.png")
c_5 = sfsp.Card("./assets/PNG-cards-1.3/5_of_clubs.png")
d_5 = sfsp.Card("./assets/PNG-cards-1.3/5_of_diamonds.png")
h_5 = sfsp.Card("./assets/PNG-cards-1.3/5_of_hearts.png")
s_5 = sfsp.Card("./assets/PNG-cards-1.3/5_of_spades.png")
c_6 = sfsp.Card("./assets/PNG-cards-1.3/6_of_clubs.png")
d_6 = sfsp.Card("./assets/PNG-cards-1.3/6_of_diamonds.png")
h_6 = sfsp.Card("./assets/PNG-cards-1.3/6_of_hearts.png")
s_6 = sfsp.Card("./assets/PNG-cards-1.3/6_of_spades.png")
c_7 = sfsp.Card("./assets/PNG-cards-1.3/7_of_clubs.png")
d_7 = sfsp.Card("./assets/PNG-cards-1.3/7_of_diamonds.png")
h_7 = sfsp.Card("./assets/PNG-cards-1.3/7_of_hearts.png")
s_7 = sfsp.Card("./assets/PNG-cards-1.3/7_of_spades.png")
c_8 = sfsp.Card("./assets/PNG-cards-1.3/8_of_clubs.png")
d_8 = sfsp.Card("./assets/PNG-cards-1.3/8_of_diamonds.png")
h_8 = sfsp.Card("./assets/PNG-cards-1.3/8_of_hearts.png")
s_8 = sfsp.Card("./assets/PNG-cards-1.3/8_of_spades.png")
c_9 = sfsp.Card("./assets/PNG-cards-1.3/9_of_clubs.png")
d_9 = sfsp.Card("./assets/PNG-cards-1.3/9_of_diamonds.png")
h_9 = sfsp.Card("./assets/PNG-cards-1.3/9_of_hearts.png")
s_9 = sfsp.Card("./assets/PNG-cards-1.3/9_of_spades.png")
c_10 = sfsp.Card("./assets/PNG-cards-1.3/10_of_clubs.png")
d_10 = sfsp.Card("./assets/PNG-cards-1.3/10_of_diamonds.png")
h_10 = sfsp.Card("./assets/PNG-cards-1.3/10_of_hearts.png")
s_10 = sfsp.Card("./assets/PNG-cards-1.3/10_of_spades.png")
c_J = sfsp.Card("./assets/PNG-cards-1.3/jack_of_clubs.png")
d_J = sfsp.Card("./assets/PNG-cards-1.3/jack_of_diamonds.png")
h_J = sfsp.Card("./assets/PNG-cards-1.3/jack_of_hearts.png")
s_J = sfsp.Card("./assets/PNG-cards-1.3/jack_of_spades.png")
c_Q = sfsp.Card("./assets/PNG-cards-1.3/queen_of_clubs.png")
d_Q = sfsp.Card("./assets/PNG-cards-1.3/queen_of_diamonds.png")
h_Q = sfsp.Card("./assets/PNG-cards-1.3/queen_of_hearts.png")
s_Q = sfsp.Card("./assets/PNG-cards-1.3/queen_of_spades.png")
c_K = sfsp.Card("./assets/PNG-cards-1.3/king_of_clubs.png")
d_K = sfsp.Card("./assets/PNG-cards-1.3/king_of_diamonds.png")
h_K = sfsp.Card("./assets/PNG-cards-1.3/king_of_hearts.png")
s_K = sfsp.Card("./assets/PNG-cards-1.3/king_of_spades.png")
twos, threes, fours, fives, sixes, sevens, eights, nines, tens, jacks, queens, kings = [c_2, d_2, h_2, s_2], [c_3, d_3, h_3, s_3], [c_4, d_4, h_4, s_4], [c_5, d_5, h_5, s_5], [c_6, d_6, h_6, s_6], [c_7, d_7, h_7, s_7], [c_8, d_8, h_8, s_8], [c_9, d_9, h_9, s_9], [c_10, d_10, h_10, s_10], [c_J, d_J, h_J, s_J], [c_Q, d_Q, h_Q, s_Q], [c_K, d_K, h_K, s_K]
temp = [twos, threes, fours, fives, sixes, sevens, eights, nines, tens, jacks, queens, kings]
clubs, diams, hears, spads = [], [], [], []
for group in temp:
    clubs.append(group[0])
    diams.append(group[1])
    hears.append(group[2])
    spads.append(group[3])
card_list = [clubs, diams, hears, spads]
symbol = None
num = 0

# Gameplay...
silence = True
almost = False
last_temp = last
start_read_assassin_silent = False
start_read_assassin = False

# MAIN LOOP...
while my_game_works or in_credits or in_menu or in_inst or in_scene:
    print(symbol, num, start_read_assassin, start_read_assassin_silent, kyu)
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

        if event.type == g.pg.QUIT:
            g.q()
            thread[0] = False
            my_game_works, in_menu, in_credits, in_inst, in_scene = False, False, False, False, False

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
            if my_game_works:
                reading = True

    # If we haven't quit...

    # Scene...
    if in_scene:

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
        if start_read_assassin_silent:
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
                start_read_assassin_silent = False
                start_read_assassin = True
                g.c.z_rel = True

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
                g.c.enter = False
                g.c.enter_rel = True
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
                g.c.enter = False
                g.c.enter_rel = True
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
                g.c.enter = False
                g.c.enter_rel = True
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
                last_h = now
            elif hearing and not almost:
                sc.blit(surf["DBackground"]["Alert"], surf["DBackground"]["loc_Alert"])
                if now - last_h >= g.c.BACKSWING:
                    hearing = False
                    almost = True
                    last_alm = now
            elif not hearing and almost:
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
        if g.c.z and now - last_c1 >= g.c.SWAP:
            in_scene = True
            my_game_works = False
            g.c.z = False
            g.c.z_rel = True
            start_read_assassin_silent = True
            continue
        if not kyu.empty():
            symbol = kyu.get_nowait()
            num = kyu.get_nowait()
            cards.empty()
            cards.add(card_list[symbol][num])
            last_c1 = now + g.c.SWAP
            reading = False
        if g.c.x and now - last_c1 >= g.c.SWAP and (symbol == 0 or symbol == 1 or symbol == 2 or symbol == 3) and not hearing and not almost:
            in_scene = True
            my_game_works = False
            start_s = now
            mouse_pressed = False
            continue
        cards.draw(sc)

        # Quitting?...
        now = g.pg.time.get_ticks()
        if surf["SBackground"]['rect_Quit'].collidepoint(g.pg.mouse.get_pos()) and mouse_pressed:
            my_game_works = False
            in_menu = True
            mouse_pressed = False
            symbol = None
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
import g


# Create a surface...
def make(factorw=1.0, factorh=1.0, w=g.c.W, h=g.c.H):
    return g.pg.Surface((w * factorw, h * factorh))

def words(size, text, color="White"):
    g.pg.font.init()
    font = g.pg.font.Font(g.pg.font.match_font('Comic Sans MS'), size)
    return font.render(text, True, color)

# Getting a sprite-sheet image...
def sp_get(sheet, loc, index, scale, col, i=1):
    surf = make(1, 1, i*32, i*32)
    x = (index % (sheet.get_width() // (i*32))) * i*32
    y = (index // (sheet.get_width() // (i*32))) * i*32
    surf.blit(sheet, loc, (x, y, i*32, i*32))
    surf = g.pg.transform.scale(surf, (i*32 * scale, i*32 * scale))
    surf.set_colorkey(col)
    return surf


class Card(g.pg.sprite.Sprite):
    def __init__(self, im):
        super().__init__()
        self.image = g.pg.transform.scale(g.pg.image.load(im), (1/4*g.np.mean([g.c.W, g.c.H]), 1/3*g.np.mean([g.c.W, g.c.H])))
        self.rect = self.image.get_rect(midbottom=(g.c.W/2, 3*g.c.H/4))

def sprite_single():
    return g.pg.sprite.GroupSingle()

# Predefined sizes...
all = make()
half = make(1, 0.5)
texture = {"Slot1": g.pg.Surface((g.c.W, 5)), "loc_Slot1": (0, 0.5*g.c.H+0.5*1/4*g.c.H),
           "Slot2": g.pg.Surface((g.c.W, 5)), "loc_Slot2": (0, 0.5*g.c.H+0.5*2/4*g.c.H),
           "Slot3": g.pg.Surface((g.c.W, 5)), "loc_Slot3": (0, 0.5*g.c.H+0.5*3/4*g.c.H)}
title = words(100, "Assassin")
cre_button = words(30, "Credits")
cre_rect = cre_button.get_rect(center=(int(g.c.W/3 - 250), int(4 * g.c.H/5)))
cre_rect.normalize()
inst_button = words(30, "Instructions")
inst_rect = inst_button.get_rect(center=(int(2 * g.c.W/3 - 280), int(4 * g.c.H/5)))
inst_rect.normalize()
play_button = words(30, "Play")
play_rect = play_button.get_rect(center=(int(g.c.W - 250), int(4 * g.c.H/5)))
play_rect.normalize()
quit_button = words(30, "Quit", "Green")
quit_rect = quit_button.get_rect(center=(80, int(g.c.H - 80)))
quit_rect.normalize()
credit_myself = words(500, "a-Me")
current_card = words(30, "Current Card:")
assassinate_button = words(30, "Press x to ASSASSINATE", "Red") # unused
assassinate_rect = assassinate_button.get_rect(bottomleft=(1/4*g.np.mean([g.c.W, g.c.H])/2 + g.c.W/2 + 50, g.c.H/2 - 20)) # unused

# Dictionaries of surfaces...
static_background = {"Wall": all, "loc_Wall": (0, 0), "Table": half, "loc_Table": (0, 0.5*g.c.H), "Texture": texture, "Quit": quit_button, "loc_Quit": (80, int(g.c.H - 80)), "rect_Quit": quit_rect, "Current_card": current_card, "loc_Current_card": (g.c.W/2 - 1/4*g.np.mean([g.c.W, g.c.H]) + 60, 3*g.c.H/4 - 1/3*g.np.mean([g.c.W, g.c.H]) - 60)}
dynamic_background = {"Assassinate": assassinate_button, "loc_Assassinate": (1/4*g.np.mean([g.c.W, g.c.H])/2 + g.c.W/2 + 50, g.c.H/2 - 50), "rect_Assassinate": assassinate_rect}
scene = {"Sky": all, "loc_Sky": (0, 0), "Floor": half, "loc_Floor": (0, 0.5*g.c.H)}
menu = {"Wall": all, "loc_Wall": (0, 0), "Title": title, "loc_Title": (int(g.c.W/2 - 160), int(g.c.H/5)), "Credits": cre_button, "loc_Credits": (int(g.c.W/3 - 250), int(4 * g.c.H/5)), "Instructions": inst_button, "loc_Instructions": (int(2 * g.c.W/3 - 280), int(4 * g.c.H/5)), "Play": play_button, "loc_Play": (int(g.c.W - 250), int(4 * g.c.H/5)), "rect_Play": play_rect, "rect_Instruction": inst_rect, "rect_Credits": cre_rect}
credits = {"Wall": all, "loc_Wall": (0, 0), "Me": credit_myself, "loc_Me": (0, 0)}

# Load command...
def get():
    return {"SBackground": static_background, "DBackground": dynamic_background, "Menu": menu, "Credits": credits, "Scene": scene}

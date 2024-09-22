import g
import sounddevice as sd

def read(kyu, order, ev):
    while True:
        if not kyu.empty():
            pass
        else:
            if order:
                kyu.put(g.r.choice(range(0, 4)))
                kyu.put(g.r.choice(range(0, 12)))
                evi = g.pg.event.Event(ev)
                g.pg.event.post(evi)
            else:
                pass

def listen(ev, already, do):
    while do[0]:
        if not already:
            recording = sd.rec(int(g.c.DUR * g.c.SR), samplerate=g.c.SR, channels=2)
            sd.wait()
            fft_output = abs(g.np.fft.fft(recording[:,0]))
            for r in fft_output:
                if r > g.c.TH:
                    evi = g.pg.event.Event(ev)
                    g.pg.event.post(evi)
                    break
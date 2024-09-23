import g
import sounddevice as sd

def read(kyu, reading, do):
    while do[0]:
        if reading[0]:
            kyu.put(g.r.choice(range(4)))
            kyu.put(g.r.choice(range(12)))
            reading[0] = False

def listen(ev, hearing, do):
    while do[0]:
        if hearing[0]:
            recording = sd.rec(int(g.c.DUR * g.c.SR), samplerate=g.c.SR, channels=2)
            sd.wait()
            fft_output = abs(g.np.fft.fft(recording[:,0]))
            for r in fft_output:
                if r > g.c.TH:
                    evi = g.pg.event.Event(ev)
                    g.pg.event.post(evi)
                    break
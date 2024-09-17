import g
import sounddevice as sd

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
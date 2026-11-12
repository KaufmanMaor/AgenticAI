"""Synthesized 128 BPM track for the Masters Club promo. Output: music.wav"""
import numpy as np, wave
from scipy.signal import butter, lfilter

SR = 44100
BPM = 128
B = 60 / BPM
TOTAL_BEATS = 90
N = int(SR * B * TOTAL_BEATS)
rng = np.random.default_rng(7)
L = np.zeros(N); R = np.zeros(N)

def at(beat): return int(round(beat * B * SR))

def add(sig, beat, gain=1.0, pan=0.0):
    i = at(beat); j = min(N, i + len(sig))
    if i >= N: return
    s = sig[: j - i] * gain
    L[i:j] += s * (1 - max(0, pan)); R[i:j] += s * (1 + min(0, pan))

def lp(x, f):
    b, a = butter(2, min(f, SR / 2 - 100) / (SR / 2)); return lfilter(b, a, x)
def hp(x, f):
    b, a = butter(2, f / (SR / 2), 'high'); return lfilter(b, a, x)
def bp(x, lo, hi):
    b, a = butter(2, [lo / (SR / 2), hi / (SR / 2)], 'band'); return lfilter(b, a, x)

def kick(dur=0.45, big=False):
    t = np.arange(int(SR * dur)) / SR
    f = 48 + 140 * np.exp(-t * 32)
    ph = 2 * np.pi * np.cumsum(f) / SR
    s = np.sin(ph) * np.exp(-t * (5 if big else 8))
    click = rng.standard_normal(len(t)) * np.exp(-t * 400) * 0.3
    return np.tanh((s + click) * 1.8)

def clap():
    n = int(SR * 0.25); t = np.arange(n) / SR
    env = np.exp(-t * 22)
    for d in (0.0, 0.011, 0.022):
        env += np.where(t > d, np.exp(-(t - d) * 120), 0) * 0.6
    return bp(rng.standard_normal(n), 900, 6000) * env * 0.9

def hat(open_=False):
    n = int(SR * (0.18 if open_ else 0.05)); t = np.arange(n) / SR
    return hp(rng.standard_normal(n), 7000) * np.exp(-t * (18 if open_ else 90)) * 0.35

def saw(freq, dur, detune=(0, -0.11, 0.13, -0.23, 0.21)):
    t = np.arange(int(SR * dur)) / SR
    s = np.zeros_like(t)
    for d in detune:
        f = freq * 2 ** (d / 12)
        s += 2 * ((t * f + rng.random()) % 1) - 1
    return s / len(detune)

def note(n):  # midi -> hz
    return 440 * 2 ** ((n - 69) / 12)

# A minor: Am F C G (roots A2 F2 C3 G2)
prog = [(45, [57, 60, 64]), (41, [53, 57, 60]), (48, [55, 60, 64]), (43, [55, 59, 62])]

def chord_at(beat):
    return prog[int(beat // 4) % 4]

# ---------- sections ----------
# Intro 0-8: pad + text-hit kicks; riser 4-8
for bar in range(0, 8, 4):
    root, ch = chord_at(bar)
    pad = sum(saw(note(n), 4 * B) for n in ch) / 3
    t = np.arange(len(pad)) / SR
    pad = lp(pad, 900) * np.minimum(1, t * 3) * 0.35
    add(pad, bar, pan=0)
for b in (0, 2, 4, 6):
    add(kick(0.6, big=True), b, 0.9)
    add(lp(rng.standard_normal(int(SR * .5)), 3000) * np.exp(-np.arange(int(SR * .5)) / SR * 9) * .25, b)

def riser(beats, start):
    n = int(SR * beats * B); t = np.arange(n) / SR
    x = rng.standard_normal(n)
    out = np.zeros(n); seg = 2048
    for k in range(0, n, seg):
        fr = 300 + (k / n) ** 2 * 9000
        out[k:k + seg] = bp(x[k:k + seg], fr * 0.7, min(fr * 1.4, 19000))
    sweep = np.sin(2 * np.pi * np.cumsum(200 + 1400 * (t / t[-1]) ** 2) / SR) * 0.15
    add((out * 0.5 + sweep) * (t / t[-1]) ** 1.5, start, 0.7)
riser(4, 4)

def full_beat(b0, b1, stabs=True, intensity=1.0):
    for b in np.arange(b0, b1):
        add(kick(), b, 1.0)
        add(hat(), b + 0.5, 0.9 * intensity, pan=0.2)
        add(hat(), b + 0.25, 0.35 * intensity, pan=-0.2)
        add(hat(), b + 0.75, 0.35 * intensity, pan=-0.2)
        if int(b) % 2 == 1:
            add(clap(), b, 0.8)
        # sidechained bass on 8ths (offbeat-heavy)
        root, ch = chord_at(b)
        for off in (0.5,):
            bs = saw(note(root), B * 0.45, detune=(0, 0.06))
            tt = np.arange(len(bs)) / SR
            bs = lp(bs, 700) * np.exp(-tt * 3) * 0.55
            add(np.tanh(bs * 2) * 0.5, b + off)
        sub = np.sin(2 * np.pi * note(root - 12) * np.arange(int(SR * B)) / SR)
        env = np.clip((np.arange(len(sub)) / SR - 0.06) * 12, 0, 1) * 0.35
        add(sub * env, b)
        if stabs:
            for off in (0.5,) if int(b) % 4 != 3 else (0.5, 0.75):
                st = sum(saw(note(n + 12), B * 0.3) for n in ch) / 3
                tt = np.arange(len(st)) / SR
                st = lp(st, 3500) * np.exp(-tt * 9) * 0.28
                add(st, b + off, pan=0.3 if off == 0.5 else -0.3)
    # arp lead
    for b in np.arange(b0, b1, 0.25):
        root, ch = chord_at(b)
        seq = [ch[0] + 12, ch[1] + 12, ch[2] + 12, ch[1] + 24]
        n_ = seq[int(round(b * 4)) % 4]
        s = saw(note(n_), B * 0.22, detune=(0, 0.08))
        tt = np.arange(len(s)) / SR
        add(lp(s, 5000) * np.exp(-tt * 14) * 0.10 * intensity, b, pan=0.4 * (1 if int(b * 4) % 2 else -1))

# Main drop 8-40
full_beat(8, 40)
# Build 40-48: snare roll accelerating + riser, no kick in last 2 beats
for b in np.arange(40, 44, 0.5): add(clap(), b, 0.5)
for b in np.arange(44, 46, 0.25): add(clap(), b, 0.6)
for b in np.arange(46, 47.5, 0.125): add(clap(), b, 0.7)
for b in range(40, 46): add(kick(), b, 0.8)
riser(8, 40)
for bar in (40, 44):
    root, ch = chord_at(bar)
    pad = sum(saw(note(n + 12), 4 * B) for n in ch) / 3
    tt = np.arange(len(pad)) / SR
    pad = lp(pad, 1500 + 3000 * (bar - 40) / 4) * 0.25
    add(pad, bar)
# Drop 2 48-64 (biggest)
add(kick(1.2, big=True), 48, 1.0)
add(hp(rng.standard_normal(int(SR * 1.5)), 2000) * np.exp(-np.arange(int(SR * 1.5)) / SR * 3) * 0.3, 48)
full_beat(48, 64, intensity=1.2)
# 64-72: halftime hits, keep tension
for b in range(64, 72):
    add(kick(), b, 0.9)
    if b % 2 == 0: add(clap(), b, 0.8)
    add(hat(open_=True), b + 0.5, 0.6)
    root, ch = chord_at(b)
    st = sum(saw(note(n + 12), B * 0.9) for n in ch) / 3
    tt = np.arange(len(st)) / SR
    add(lp(st, 2500) * np.exp(-tt * 3) * 0.3, b)
# 72-76: breakdown - pad + riser, kick only on "LATER." (75)
riser(4, 72)
root, ch = chord_at(72)
pad = sum(saw(note(n), 4 * B) for n in ch) / 3
add(lp(pad, 1200) * 0.3, 72)
add(kick(0.8, big=True), 72, 0.9); add(kick(0.8, big=True), 75, 1.0)
# 76: impact + end pad tail
add(kick(2.5, big=True), 76, 1.1)
boom = lp(rng.standard_normal(int(SR * 3)), 400) * np.exp(-np.arange(int(SR * 3)) / SR * 1.5)
add(boom * 0.9, 76)
for i, bar in enumerate((76, 80, 84)):
    root, ch = chord_at(0)
    pad = sum(saw(note(n + 12), 4 * B) for n in ch + [ch[0] + 12]) / 4
    tt = np.arange(len(pad)) / SR
    add(lp(pad, 2200) * 0.22 * (1 - i * 0.3), bar)
full = TOTAL_BEATS * B
# master
mix = np.stack([L, R], 1)
t = np.arange(N) / SR
mix *= np.clip((full - t) / 2.5, 0, 1)[:, None]  # fade out
mix = np.tanh(mix * 1.4)
mix /= np.abs(mix).max() * 1.05
pcm = (mix * 32767).astype(np.int16)
with wave.open('music.wav', 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
print('ok', N / SR)

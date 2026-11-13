"""Masters Club Cohort 2 promo renderer: 1080x1920 @30fps, cuts synced to 128 BPM."""
import os, sys, math, glob, subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops, ImageOps, ImageEnhance

S = os.path.dirname(os.path.abspath(__file__))
A = f"{S}/assets"
W, H, FPS = 1080, 1920, 30
BPM = 128; B = 60 / BPM
TOTAL_BEATS = 88
NFRAMES = int(TOTAL_BEATS * B * FPS)
NAVY = (8, 22, 96); ACCENT = (64, 168, 255); WHITE = (255, 255, 255)
F_ANTON = f"{S}/fonts/fontsource-anton-5.3.0/files/anton-latin-400-normal.woff"
F_MONT = f"{S}/fonts/fontsource-montserrat-5.3.0/files/montserrat-latin-%d-normal.woff"
F_SERIF = f"{S}/fonts/fontsource-playfair-display-5.3.0/files/playfair-display-latin-700-normal.woff"

def img(name):
    m = glob.glob(f"{A}/img/*{name}*")
    assert m, name
    return m[0]

# ---------- clips ----------
CLIPS = {  # name: (file glob, start sec)
    'ming': ('4qjrgx', 0.8), 'speaker': ('6wqp67', 4.0), 'walk': ('hw49uj', 3.6),
    'circle': ('sqfkxf', 0.8), 'food': ('3ysl7w', 2.0),
}
def extract_clips():
    for k, (g, st) in CLIPS.items():
        d = f"{S}/clips/{k}"
        if os.path.isdir(d) and len(os.listdir(d)) > 30: continue
        os.makedirs(d, exist_ok=True)
        src = glob.glob(f"{A}/vid/*{g}*")[0]
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(st), '-i', src, '-t', '1.6',
                        '-vf', f'fps={FPS},scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}',
                        '-q:v', '3', f'{d}/%03d.jpg'], check=True)

# ---------- image prep ----------
_cache = {}
def grade(im, strength=1.0):
    im = ImageEnhance.Contrast(im).enhance(1.12)
    im = ImageEnhance.Color(im).enhance(1.08)
    arr = np.asarray(im).astype(np.float32)
    # cool shadows toward navy, keep highlights
    lum = arr.mean(2, keepdims=True) / 255
    tint = np.array([10, 25, 70], np.float32)
    arr = arr * (0.92) + tint * (1 - lum) * 0.35 * strength
    return Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))

def prep(path, mode='fill', pad=1.18):
    key = (path, mode)
    if key in _cache: return _cache[key]
    im = ImageOps.exif_transpose(Image.open(path)).convert('RGB')
    cw, ch = int(W * pad), int(H * pad)
    if mode == 'fill':
        out = ImageOps.fit(im, (cw, ch), Image.LANCZOS, centering=(0.5, 0.45))
    else:  # fit width on blurred background
        bg = ImageOps.fit(im, (cw, ch), Image.LANCZOS).filter(ImageFilter.GaussianBlur(40))
        bg = ImageEnhance.Brightness(bg).enhance(0.45)
        fg = im.copy(); fg.thumbnail((int(cw * 0.96), ch), Image.LANCZOS)
        bg.paste(fg, ((cw - fg.width) // 2, (ch - fg.height) // 2))
        out = bg
    out = grade(out)
    _cache[key] = out
    return out

def clip_frame(name, i):
    fs = sorted(glob.glob(f"{S}/clips/{name}/*.jpg"))
    im = Image.open(fs[min(i, len(fs) - 1)]).convert('RGB')
    im = grade(im)
    return im.resize((int(W * 1.08), int(H * 1.08)), Image.BILINEAR)

def zoom_crop(base, z, dx=0.0, dy=0.0):
    bw, bh = base.size
    # z=1 shows a W x H window from the center of the (padded) base
    vw = W / z; vh = H / z
    vw = min(vw, bw); vh = min(vh, bh)
    cx = bw / 2 + dx * (bw - vw) / 2; cy = bh / 2 + dy * (bh - vh) / 2
    box = (cx - vw / 2, cy - vh / 2, cx + vw / 2, cy + vh / 2)
    return base.resize((W, H), Image.BILINEAR, box=box)

# ---------- text ----------
_fonts = {}
def font(path, size):
    k = (path, size)
    if k not in _fonts: _fonts[k] = ImageFont.truetype(path, size)
    return _fonts[k]

_tcache = {}
def text_layer(lines, size=170, fpath=F_ANTON, color=WHITE, spacing=0.02, stroke=0, track=0):
    """lines: list of str or (str, color). Returns RGBA image of the block (centered lines)."""
    key = (tuple(map(str, lines)), size, fpath, color, track)
    if key in _tcache: return _tcache[key]
    f = font(fpath, size)
    rendered = []
    for ln in lines:
        txt, col = (ln if isinstance(ln, tuple) else (ln, color))
        if track:
            widths = [f.getlength(c) + track for c in txt]
            wv = int(sum(widths)) + 4
        else:
            wv = int(f.getlength(txt)) + 4
        asc, desc = f.getmetrics()
        hh = asc + desc
        im = Image.new('RGBA', (wv + 40, hh + 40), (0, 0, 0, 0))
        d = ImageDraw.Draw(im)
        if track:
            x = 20
            for c, w_ in zip(txt, widths):
                d.text((x, 20), c, font=f, fill=col); x += w_
        else:
            d.text((20, 20), txt, font=f, fill=col)
        im = im.crop(im.getbbox()) if im.getbbox() else im
        rendered.append(im)
    gap = int(size * 0.18)
    tw = max(r.width for r in rendered); th = sum(r.height for r in rendered) + gap * (len(rendered) - 1)
    block = Image.new('RGBA', (tw + 60, th + 60), (0, 0, 0, 0))
    y = 30
    for r in rendered:
        block.alpha_composite(r, ((block.width - r.width) // 2, y)); y += r.height + gap
    # drop shadow
    sh = Image.new('RGBA', block.size, (0, 0, 0, 0))
    alpha = block.split()[3].filter(ImageFilter.GaussianBlur(14))
    sh.putalpha(alpha.point(lambda a: int(a * 0.75)))
    out = Image.new('RGBA', block.size, (0, 0, 0, 0))
    out.alpha_composite(sh, (0, 6)); out.alpha_composite(block)
    _tcache[key] = out
    return out

def ease_out(x): x = max(0, min(1, x)); return 1 - (1 - x) ** 3

def put_text(frame, layer, t, cy=0.5, slam=True, maxw=0.9, rgbsplit=False):
    """t = seconds since text appeared."""
    scale = 1.0
    if slam:
        scale = 1 + 0.55 * math.exp(-t * 16)
    fitscale = min(1, W * maxw / layer.width)
    s = scale * fitscale
    lw, lh = int(layer.width * s), int(layer.height * s)
    if lw < 2 or lh < 2: return
    L_ = layer.resize((lw, lh), Image.BILINEAR)
    a = min(1, t * 14)
    if a < 1:
        L_.putalpha(L_.split()[3].point(lambda v: int(v * a)))
    x = (W - lw) // 2; y = int(H * cy - lh / 2)
    if rgbsplit and t < 0.25:
        off = int(18 * (1 - t / 0.25))
        r, g, b_, al = L_.split()
        red = Image.merge('RGBA', (r, Image.new('L', r.size, 0), Image.new('L', r.size, 0), al.point(lambda v: v // 2)))
        blu = Image.merge('RGBA', (Image.new('L', r.size, 0), Image.new('L', r.size, 0), b_, al.point(lambda v: v // 2)))
        frame.alpha_composite(red, (x - off, y)); frame.alpha_composite(blu, (x + off, y))
    frame.alpha_composite(L_, (x, y))

# ---------- fx ----------
def vignette():
    yy, xx = np.mgrid[0:H, 0:W]
    d = np.sqrt(((xx - W / 2) / (W * 0.75)) ** 2 + ((yy - H / 2) / (H * 0.7)) ** 2)
    v = np.clip(1 - (d - 0.45) * 0.9, 0.35, 1)
    return v[..., None].astype(np.float32)
VIG = vignette()
rng = np.random.default_rng(3)
GRAIN = [rng.normal(0, 7, (H // 2, W // 2, 1)).astype(np.float32).repeat(2, 0).repeat(2, 1) for _ in range(6)]

def finish(frame_rgb, fi, flash=0.0, darken=0.0, shake=(0, 0), split=0):
    arr = np.asarray(frame_rgb).astype(np.float32)
    if split:
        arr[..., 0] = np.roll(arr[..., 0], split, 1); arr[..., 2] = np.roll(arr[..., 2], -split, 1)
    arr *= VIG
    if darken: arr *= (1 - darken)
    arr += GRAIN[fi % len(GRAIN)]
    if flash: arr = arr * (1 - flash) + 255 * flash
    out = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))
    if shake != (0, 0):
        out = ImageChops.offset(out, int(shake[0]), int(shake[1]))
    return out

# ---------- timeline ----------
# shot: (start_beat, len_beats, kind, src, opts)
shots = []
def shot(b, n, kind, src, **o): shots.append((b, n, kind, src, o))
texts = []  # (start_beat, end_beat, lines, opts)
def txt(b, e, lines, **o): texts.append((b, e, lines, o))

# Intro 0-8 over dark moody circle clip -> photos
shot(0, 4, 'clip', 'circle', dark=0.6, blur=True)
shot(4, 4, 'img', ('IMG_1888', 'fill'), dark=0.6, blur=True)
txt(0, 2, ["WHILE YOU"], size=190)
txt(2, 4, ["WERE", ("SCROLLING...", ACCENT)], size=190)
txt(4, 6, ["40 PEOPLE"], size=210)
txt(6, 8, ["WERE BUILDING", ("SOMETHING.", ACCENT)], size=150)

main = [
    ('img', ('IMG_6532', 'fill'), None),
    ('clip', 'ming', ["NO SMALL TALK."]),
    ('img', ('IMG_6517', 'fill'), ["EXECUTIVES."]),
    ('img', ('35dgaq', 'fill'), ["FOUNDERS."]),
    ('clip', 'speaker', [("REAL TALK.", ACCENT)]),
    ('img', ('IMG_1906', 'fill'), ["DEEP", "CONVERSATIONS."]),
    ('img', ('u1j6db', 'fill'), ["THE SHARPEST", ("MINDS AT REICHMAN", ACCENT)]),
    ('img', ('IMG_6510', 'fill'), None),
    ('img', ('m1avpi', 'fill'), ["EXCLUSIVE", "DINNERS."]),
    ('img', ('nxqen6', 'fill'), [("LATE NIGHTS.", ACCENT)]),
    ('img', ('h1kkk1', 'fill'), None),
    ('img', ('n8c3je', 'fill'), ["ROOFTOPS."]),
    ('img', ('lnf8h2', 'fill'), ["REAL", ("FRIENDSHIPS.", ACCENT)]),
    ('clip', 'walk', ["ONE EVENING", "A MONTH."]),
    ('img', ('IMG_3314', 'fill'), ["A YEAR OF", ("TRANSFORMATION.", ACCENT)]),
    ('img', ('8nwzt1', 'fit'), ["THIS IS", ("THE CLUB.", ACCENT)]),
]
for i, (k, src, cap) in enumerate(main):
    b = 8 + i * 2
    shot(b, 2, k, src, punch=True)
    if cap: txt(b + (0 if i % 2 == 0 else 0.0), b + 2, cap, size=170, cy=0.72 if i == 15 else 0.5)

strobe = ['IMG_0300', 'IMG_2206', 'IMG_2262', 'IMG_2329', 'IMG_2333', 'tn7sys', 'dcupil', 'c8hdz2',
          'gyxbxs', 'agj6hd', 'IMG_6515', 'IMG_6535', 'f2j43j', 'IMG_3195', 'b45web', 'IMG_1478_2']
for i, s in enumerate(strobe[:12]):
    shot(40 + i * 0.5, 0.5, 'img', (s, 'fill'), punch=True, dark=0.25)
for i, s in enumerate(strobe[12:]):  # accelerate: quarter-beats
    shot(46 + i * 0.25, 0.25, 'img', (s, 'fill'), dark=0.25)
shot(47, 1, 'black', None)
txt(40, 42, ["COHORT #1"], size=230, rgb=True)
txt(42, 44, ["WAS"], size=260, rgb=True)
txt(44, 47, [("LEGENDARY.", ACCENT)], size=200, rgb=True)
txt(47, 48, ["AND NOW..."], size=150, slam=False)

drop2 = [
    ('img', ('IMG_3358', 'fit'), ["COHORT", ("#2", ACCENT)]),
    ('clip', 'circle', ["NEW FACES."]),
    ('img', ('IMG_2329', 'fill'), ["NEW SPEAKERS."]),
    ('img', ('IMG_6535', 'fill'), ["NEW NIGHTS."]),
    ('clip', 'food', None),
    ('img', ('b45web', 'fill'), ["SAME", ("STANDARD.", ACCENT)]),
    ('img', ('gyxbxs', 'fill'), None),
    ('img', ('IMG_0300', 'fill'), [("ARE YOU IN?", ACCENT)]),
]
for i, (k, src, cap) in enumerate(drop2):
    b = 48 + i * 2
    shot(b, 2, k, src, punch=True, flash=(i == 0))
    if cap: txt(b, b + 2, cap, size=230 if i == 0 else 170, cy=0.42, rgb=(i == 0))

# 64-72 brand cards
cards = [(["ONLY", ("50 SPOTS.", ACCENT)], 240), (["CV +", ("INTERVIEW.", ACCENT)], 220),
         (["NOT EVERYONE"], 180), ([("GETS IN.", NAVY)], 260)]
for i, (ln, sz) in enumerate(cards):
    b = 64 + i * 2
    shot(b, 2, 'card', None, inv=(i == 3))
    txt(b, b + 2, ln, size=sz, rgb=True, shake=(i == 3))
# 72-76 final push
shot(72, 4, 'img', ('8nwzt1', 'fill'), dark=0.65, blur=True, slowzoom=True)
txt(72, 73.5, ["DON'T BE THE ONE"], size=150)
txt(73.5, 75, ["WHO HEARD", "ABOUT IT"], size=170)
txt(75, 76, [("TOO LATE.", ACCENT)], size=280, rgb=True, shake=True)
# 76-88 end card
shot(76, 12, 'end', None)

LOGO = Image.open(img('fik98k')).convert('RGB')

_su = {}
def su_badge(alpha=1.0, logo_w=230):
    """Students Union logo recolored to soft white (no plate), for a subtle corner mark."""
    if logo_w not in _su:
        lg = Image.open(f"{S}/su/logo.png").convert('RGBA')
        lg = lg.crop(lg.getbbox())
        lh = int(lg.height * logo_w / lg.width)
        lg = lg.resize((logo_w, lh), Image.LANCZOS)
        a_ = lg.split()[3].point(lambda v: int(v * 0.88))
        wht = Image.new('RGBA', lg.size, WHITE + (255,)); wht.putalpha(a_)
        # faint shadow for legibility on bright shots
        sh = Image.new('RGBA', (lg.width + 30, lg.height + 30), (0, 0, 0, 0))
        sa = Image.new('L', sh.size, 0); sa.paste(a_, (15, 15))
        sa = sa.filter(ImageFilter.GaussianBlur(6)).point(lambda v: int(v * 0.45))
        sh.putalpha(sa)
        sh.alpha_composite(wht, (15, 15))
        _su[logo_w] = sh
    p = _su[logo_w]
    if alpha < 1:
        p = p.copy(); p.putalpha(p.split()[3].point(lambda v: int(v * alpha)))
    return p

def put_su(frame, alpha, cy=None):
    b = su_badge(alpha)
    frame.alpha_composite(b, (40, 110))

def end_card(t):
    fr = Image.new('RGBA', (W, H), NAVY + (255,))
    # radial glow
    yy, xx = np.mgrid[0:H:4, 0:W:4]
    g = np.exp(-(((xx - W / 2) / 600) ** 2 + ((yy - H * 0.38) / 700) ** 2))
    glow = Image.fromarray((g * 70).astype(np.uint8)).resize((W, H))
    fr = Image.composite(Image.new('RGBA', (W, H), (40, 90, 220, 255)), fr, glow)
    # logo crop: the MA + wordmark region of logo png (1024 square, navy bg) -> blend
    lg = LOGO.crop((90, 220, 934, 740))
    s = 0.92 + 0.08 * ease_out(t / 0.8)
    lw = int(W * 0.82 * s); lh = int(lg.height * lw / lg.width)
    lgr = lg.resize((lw, lh), Image.LANCZOS)
    # use luminance as alpha so only white logo shows
    alpha = ImageOps.grayscale(lgr).point(lambda v: max(0, min(255, (v - 60) * 2)))
    a = ease_out(t / 0.5)
    alpha = alpha.point(lambda v: int(v * a))
    white = Image.new('RGBA', lgr.size, WHITE + (255,)); white.putalpha(alpha)
    fr.alpha_composite(white, ((W - lw) // 2, int(H * 0.30 - lh / 2)))
    if t > 0.3:
        put_su(fr, ease_out((t - 0.3) / 0.4), cy=0.075)
    if t > 0.9:
        put_text(fr, text_layer([("COHORT 2", ACCENT)], 200), t - 0.9, cy=0.56, rgbsplit=True)
    if t > 1.4:
        put_text(fr, text_layer(["APPLICATIONS ARE OPEN"], 64, F_MONT % 800, track=4), t - 1.4, cy=0.645, slam=False)
    if t > 2.0:
        l = text_layer(["FOR PEOPLE WHO DO, NOT JUST TALK."], 46, F_MONT % 600, color=(200, 215, 255), track=3)
        put_text(fr, l, t - 2.0, cy=0.80, slam=False)
    if t > 2.6:
        # pulsing CTA pill
        pulse = 1 + 0.04 * math.sin((t - 2.6) * 2 * math.pi * BPM / 60)
        l = text_layer(["APPLY NOW  ·  LINK IN BIO"], 54, F_MONT % 800, color=NAVY, track=2)
        pw, ph = int((l.width + 60) * pulse), int((l.height + 30) * pulse)
        pill = Image.new('RGBA', (pw, ph), (0, 0, 0, 0))
        ImageDraw.Draw(pill).rounded_rectangle((0, 0, pw - 1, ph - 1), ph // 2, fill=WHITE + (255,))
        a = ease_out((t - 2.6) / 0.3)
        pill.putalpha(pill.split()[3].point(lambda v: int(v * a)))
        fr.alpha_composite(pill, ((W - pw) // 2, int(H * 0.735 - ph / 2)))
        ls = l.resize((int(l.width * pulse), int(l.height * pulse)))
        ls.putalpha(ls.split()[3].point(lambda v: int(v * a)))
        fr.alpha_composite(ls, ((W - ls.width) // 2, int(H * 0.735 - ls.height / 2)))
    return fr

def card_bg(inv):
    fr = Image.new('RGBA', (W, H), (WHITE if inv else NAVY) + (255,))
    d = ImageDraw.Draw(fr)
    for i in range(-H, W + H, 90):  # diagonal stripes
        d.line([(i, 0), (i + H * 0.6, H)], fill=((222, 232, 255) if inv else (14, 32, 120)) + (255,), width=18)
    return fr

def beat_punch(beat_pos):
    ph = beat_pos % 1.0
    return math.exp(-ph * 9)

def render_frame(fi):
    tsec = fi / FPS; beat = tsec / B
    cur = [s for s in shots if s[0] <= beat < s[0] + s[1]]
    sb, sn, kind, src, o = cur[-1] if cur else (0, 1, 'black', None, {})
    local = (beat - sb) * B  # sec into shot
    pr = beat_punch(beat) if beat >= 8 and beat < 64 else 0
    if kind == 'end':
        frame = end_card(local)
        rgb = frame.convert('RGB'); return finish(rgb, fi, flash=max(0, 1 - local * 5) * 0.9)
    if kind == 'black':
        frame = Image.new('RGBA', (W, H), (0, 0, 0, 255))
    elif kind == 'card':
        frame = card_bg(o.get('inv'))
    else:
        z = 1.0 + 0.06 * (local / (sn * B)) + (0.05 * pr if o.get('punch') else 0)
        if o.get('slowzoom'): z = 1 + 0.12 * local / (sn * B)
        if kind == 'img':
            base = prep(img(src[0]), src[1])
            dx = 0.25 * math.sin(sb * 1.7) * (local / (sn * B))
            fr = zoom_crop(base, z, dx=dx)
        else:
            fr = zoom_crop(clip_frame(src, int(local * FPS)), z)
        if o.get('blur'): fr = fr.filter(ImageFilter.GaussianBlur(6))
        if o.get('dark'): fr = ImageEnhance.Brightness(fr).enhance(1 - o['dark'])
        frame = fr.convert('RGBA')
    # text
    shake = (0, 0)
    for (tb, te, lines, to) in texts:
        if tb <= beat < te:
            tt = (beat - tb) * B
            lay = text_layer(lines, to.get('size', 170), color=WHITE)
            if kind in ('img', 'clip') and to.get('cy', 0.5) != 0.5 or True:
                pass
            put_text(frame, lay, tt, cy=to.get('cy', 0.5), slam=to.get('slam', True), rgbsplit=to.get('rgb', False))
            if to.get('shake') and tt < 0.35:
                k = (1 - tt / 0.35) * 26
                shake = (rng.uniform(-k, k), rng.uniform(-k, k))
    # progress bar during drop2
    if 48 <= beat < 64:
        p = (beat - 48) / 16
        pct = int(12 + 85 * ease_out(p * 1.05))
        bx, by, bw_, bh_ = 140, int(H * 0.86), W - 280, 26
        d = ImageDraw.Draw(frame)
        lab = text_layer([f"COHORT #2 LOADING...  {pct}%"], 44, F_MONT % 800, track=3)
        frame.alpha_composite(lab, ((W - lab.width) // 2, by - lab.height - 4))
        d.rounded_rectangle((bx, by, bx + bw_, by + bh_), 13, outline=WHITE + (255,), width=4)
        d.rounded_rectangle((bx + 6, by + 6, bx + 6 + int((bw_ - 12) * pct / 100), by + bh_ - 6), 8, fill=ACCENT + (255,))
    # Students Union logo during the intro (mandatory)
    if beat < 8:
        put_su(frame, min(1.0, 0.35 + tsec / 0.4))
    # brand bug
    if 8 <= beat < 76 and kind not in ('card',):
        bug = text_layer(["THE MASTERS CLUB · REICHMAN"], 30, F_MONT % 700, color=(235, 240, 255), track=4)
        frame.alpha_composite(bug, ((W - bug.width) // 2, 70))
    # flashes on cuts
    cut_age = local
    flash = 0
    if kind != 'card' and beat >= 8 and cut_age < 0.08: flash = 0.55 * (1 - cut_age / 0.08)
    if o.get('flash') and local < 0.3: flash = max(flash, 1 - local / 0.3)
    if kind == 'card' and local < 0.06: flash = 0.8
    split = int(10 * pr) if 40 <= beat < 64 else 0
    return finish(frame.convert('RGB'), fi, flash=flash, shake=shake, split=split)

if __name__ == '__main__':
    extract_clips()
    a, b_ = int(sys.argv[1]), int(sys.argv[2])
    os.makedirs(f"{S}/frames", exist_ok=True)
    for fi in range(a, min(b_, NFRAMES)):
        render_frame(fi).save(f"{S}/frames/{fi:05d}.jpg", quality=92)
    print('done', a, b_)

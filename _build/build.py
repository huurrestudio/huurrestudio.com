#!/usr/bin/env python3
"""Builds the Huurre Studio website.

Every page is generated from the templates and the GAMES list below, so the
header, footer and all game pages stay consistent. Edit this file, then run:
    python3 _build/build.py        (from the site folder)

Adding a game: add an entry to GAMES, put its images in assets/<slug>/ and
add a colour theme `.game--<slug>` in assets/site.css. The game then appears
in the header's Games menu, on the home page, gets its own page (with its
Help section), a line on the Support page, a row in the privacy policy's
table and a sitemap entry. Nothing else grows: the header, footer, support
page and privacy policy are written to scale to any number of games.
"""
import hashlib
from html import escape
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent
BASE = 'https://huurrestudio.com'
EMAIL = 'hello@huurrestudio.com'
UPDATED = '29 September 2026'
FONTS = ('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@1,9..144,400'
         '&family=Lilita+One&family=Manrope:wght@400;500;600;700;800&family=Space+Grotesk:wght@700&display=swap')


def asset(path):
    """An asset's address with a version code taken from its contents.
    GitHub Pages lets browsers keep files for 10 minutes, so without this a
    browser could pair a new page with the stylesheet it saved before an
    update (a broken header). A changed file gets a new address instead."""
    digest = hashlib.sha1((SITE / path.lstrip('/')).read_bytes()).hexdigest()[:10]
    return f'{path}?v={digest}'


# Who a game is made for decides which privacy rules apply to it.
AUDIENCES = {
    'all': {'label': 'All ages, including children', 'anchor': 'all-ages-games',
            'ads': 'Child-directed, never personalised', 'ad_id': 'Not used'},
    'teen': {'label': '13 and over', 'anchor': 'teen-games',
             'ads': 'Personalised only with your consent', 'ad_id': 'Only if you allow tracking'},
}

# ---------------------------------------------------------------------------
# The games. Text may contain simple HTML (<strong>, <a>).
# ---------------------------------------------------------------------------
GAMES = [
    {
        'slug': 'deep-signal',
        'name': 'Deep Signal',
        'title_html': 'Deep<br>Signal',
        'subtitle': 'Space Shooter',
        'audience': 'teen',
        'status': 'Coming soon · Android &amp; iOS',
        'store_note': 'on Google Play &amp; the App Store',
        'summary': 'A fast, one-thumb space shooter. Steer while your ship fires on its own, pick upgrades as you level up, and survive the bosses.',
        'chips': ['One-thumb controls', 'Quick runs', '12 languages'],
        'shots': 'portrait',      # the home page banner's screenshot layout
        'images': [               # banner screenshots (the gallery shows these, plus any extras)
            ('upgrade.jpg', 720, 1558, 'Deep Signal level-up screen: choose one of three upgrades — Rapid Fire, Vitality Cell or Swift Drive.'),
            ('menu.jpg', 720, 1558, 'Deep Signal main menu: the title above a glowing signal trace, a ship rising past a blue planet, and a Play button.'),
            ('gameplay.jpg', 720, 1558, "Deep Signal gameplay: the player's ship firing at purple and red enemy ships, with glowing pickups and a x16 combo."),
        ],
        'gallery_extra': [],
        'og_image': '/assets/og-image.png',
        'features': [
            ('One thumb', 'Steer with one thumb. Your ship aims and fires by itself.'),
            ('Quick runs', 'A run takes a few minutes. Beat your best time and wave, with a boss every third wave.'),
            ('Your music', 'Play the soundtrack, or your own music from any app.'),
        ],
        'details': [
            ('Genre', 'Arcade space shooter'),
            ('Age', '13 and over'),
            ('Price', 'Free, with ads between runs'),
            ('Languages', '12'),
            ('Account', 'None needed; progress stays on your device'),
        ],
        'faq': [
            ('How do I play?', '<p>Drag the control wheel to steer. Your ship fires by itself. Collect orbs to level up and pick an upgrade each time.</p>'),
            ('Can I play my own music?', '<p>Yes: <strong>Settings → Background Music → Your Music</strong>, then play music from any app.</p>'),
            ('How do I change my name?', '<p><strong>Settings → Change Name</strong>.</p>'),
            ('How do I change my ad choices?', '<p>In the game: <strong>Settings → Privacy Choices</strong> (where available). On iPhone: <strong>Settings → Privacy &amp; Security → Tracking</strong>. On Android: <strong>Settings → Google → Ads</strong>. See the <a href="/privacy/#teen-games">privacy policy</a>.</p>'),
        ],
    },
    {
        'slug': 'goat-bash',
        'name': 'Goat Bash',
        'title_html': 'Goat<br>Bash',
        'subtitle': 'Fjord Trolls',
        'audience': 'all',
        'status': 'Coming soon · Android &amp; iOS',
        'store_note': 'on Google Play, then the App Store',
        'summary': 'A physics puzzle game for the whole family. Pick your herd, then leap, head-butt and splash cheeky trolls into the fjord.',
        'chips': ['Physics puzzles', '30 levels', '12 languages'],
        'shots': 'landscape',
        'images': [
            ('action.jpg', 1280, 600, 'Goat Bash gameplay: Big Billy head-butts a troll with a BONK!, a barrel of troll potion explodes and trolls fly towards the water.'),
            ('herd.jpg', 1280, 600, 'The Pick your herd screen under the northern lights: two leaps for Pip, two for Bramble and one for Big Billy.'),
        ],
        'gallery_extra': [
            ('aim.jpg', 1280, 600, 'Goat Bash: Big Billy aims a leap at a wooden tower full of trolls, with a dotted arc showing the jump.'),
        ],
        'og_image': '/assets/goat-bash/og.jpg',
        'features': [
            ('Pick your herd', "Pip leaps the farthest and dashes mid-air, Bramble's bleat blows trolls away, and Big Billy hits the hardest."),
            ('Bonk! Boom! Splash!', 'Topple towers, set off barrels of troll potion and roll boulders down icy slopes.'),
            ('30 levels, 3 worlds', 'From the sunny Fjord Meadow through the Autumn Pines to the Frost Peaks under the northern lights.'),
        ],
        'details': [
            ('Genre', 'Physics puzzle'),
            ('Age', 'All ages'),
            ('Price', 'Free, with family-friendly ads between levels'),
            ('Languages', '12'),
            ('Account', 'None needed; progress stays on your device'),
        ],
        'faq': [
            ('How do I play?', "<p>Press anywhere, drag back and let go: the selected goat leaps the opposite way. Tap while it's in the air for its special move. Knock every troll into the water to clear the level.</p>"),
            ("Why can't I press Go?", '<p>Before a level you pick your herd, and every leap needs a goat. Tap the goats (or <strong>+</strong>) until all leaps are filled, then press <strong>Go!</strong></p>'),
            ('What do the goats do?', "<p><strong>Pip</strong> leaps the farthest and dashes to wherever you tap. <strong>Bramble</strong>'s bleat blows trolls away. <strong>Big Billy</strong> hits the hardest and slams down with a shockwave.</p>"),
            ('What about ads?', '<p>Goat Bash shows family-friendly ads between levels, and you can choose to watch a short video for 2 extra leaps. Ads are never personalised and the game doesn\'t use your advertising ID. Playing offline means no ads. See the <a href="/privacy/#all-ages-games">privacy policy</a>.</p>'),
        ],
    },
]

# ---------------------------------------------------------------------------
# Shared pieces
# ---------------------------------------------------------------------------
ICON_PHONE = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" '
              'stroke-linejoin="round" aria-hidden="true"><rect x="6" y="2.5" width="12" height="19" rx="2.5"/>'
              '<path d="M12 7.5v7M9 11.5l3 3 3-3"/></svg>')
ICON_ARROW = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" '
              'stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>')
ICON_CHEVRON = ('<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" '
                'stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>')
BRAND_MARK = ('<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="4.5" stroke-linecap="round" aria-hidden="true">'
              '<path d="M8 46H56M14 46 19 37M23 46 31.5 31.3M32 46 43 27M41 46 49 32.1M50 46 54 39.1"/></svg>')


def head(title, description, path, og_image='/assets/og-image.png'):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{escape(description)}">
<link rel="canonical" href="{BASE}{path}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{escape(description)}">
<meta property="og:image" content="{BASE}{og_image}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#F4F7F9" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0A111B" media="(prefers-color-scheme: dark)">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONTS}" rel="stylesheet">
<link rel="stylesheet" href="{asset('/assets/site.css')}">
<script src="{asset('/assets/site.js')}" defer></script>
</head>'''


def header(current):
    """Brand, then a Games menu (every game, on every page) and Support.
    The menu grows downwards as games are added, never sideways."""
    items = '\n'.join(
        f'''          <li><a href="/{g["slug"]}/"{' aria-current="page"' if current == g["slug"] else ''}>
            <img src="/assets/{g["slug"]}/icon.png" width="256" height="256" alt="">
            <span><strong>{g["name"]}</strong><small>{g["subtitle"]}</small></span>
          </a></li>''' for g in GAMES)
    games_current = ' class="is-current"' if current in [g['slug'] for g in GAMES] else ''
    support_current = ' aria-current="page"' if current == 'support' else ''
    return f'''<body>
<a class="skip" href="#main">Skip to content</a>

<header class="site-header">
  <div class="wrap">
    <a class="brand" href="/" aria-label="Huurre Studio, home">
      {BRAND_MARK}
      Huurre <span>Studio</span>
    </a>
    <nav class="nav" aria-label="Main">
      <details class="menu">
        <summary{games_current}>Games {ICON_CHEVRON}</summary>
        <ul class="menu-list">
{items}
          <li class="menu-all"><a href="/#games">All games</a></li>
        </ul>
      </details>
      <a href="/support/"{support_current}>Support</a>
    </nav>
  </div>
</header>
'''


def footer():
    return f'''
<footer class="site-footer">
  <div class="wrap">
    <p style="margin:0">© 2026 Huurre Studio · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
    <nav aria-label="Footer">
      <a href="/#games">Games</a>
      <a href="/support/">Support</a>
      <a href="/privacy/">Privacy Policy</a>
    </nav>
  </div>
</footer>
</body>
</html>
'''


def page(title, description, path, current, main, og_image='/assets/og-image.png'):
    return head(title, description, path, og_image) + header(current) + f'\n<main id="main">\n{main}\n</main>\n' + footer()


def badge(g, cls=''):
    return (f'<span class="badge-soon{cls}" role="note">{ICON_PHONE}'
            f'<span>Coming soon<small>{g["store_note"]}</small></span></span>')


def banner_shots(g):
    items = []
    for i, (file, w, h, alt) in enumerate(g['images']):
        lazy = ' loading="lazy"' if i else ''
        items.append(f'<div class="shot"><img src="/assets/{g["slug"]}/{file}" width="{w}" height="{h}" alt="{escape(alt)}"{lazy}></div>')
    return f'<div class="shots shots--{g["shots"]}">\n          ' + '\n          '.join(items) + '\n        </div>'


def banner(g):
    """The game banner on the home page."""
    chips = ''.join(f'<li>{c}</li>' for c in g['chips'])
    return f'''<article class="game game--{g["slug"]}" aria-labelledby="{g["slug"]}-title">
        <div class="game-text">
          <img class="game-icon" src="/assets/{g["slug"]}/icon.png" width="256" height="256" alt="">
          <p class="eyebrow">{g["status"]}</p>
          <h3 id="{g["slug"]}-title" class="game-title">{g["title_html"]}</h3>
          <p class="game-sub">{g["subtitle"]}</p>
          <p class="game-summary">{g["summary"]}</p>
          <ul class="chips" aria-label="Highlights">{chips}</ul>
          <div class="btns">
            <a class="btn btn-primary" href="/{g["slug"]}/">Learn more</a>
            {badge(g)}
          </div>
        </div>
        {banner_shots(g)}
      </article>'''


def faq(items):
    return '<div class="faq">\n' + '\n'.join(f'''        <details>
          <summary>{q}</summary>
          <div>{a}</div>
        </details>''' for q, a in items) + '\n      </div>'


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------
def home():
    banners = '\n\n      '.join(banner(g) for g in GAMES)
    main = f'''  <div class="hero">
    <div class="wrap">
      <div>
        <div class="definition">
          <div class="term">huurre <em>· noun · Finnish</em></div>
          <p>rime frost — the fine, feathered crystals that grow on every branch on the coldest, clearest mornings.</p>
        </div>
        <h1>Small games and apps, made with care.</h1>
        <p class="lede">An independent studio making games and apps for Android, iPhone and iPad.</p>
        <div class="btns">
          <a class="btn btn-primary" href="#games">See our games
            {ICON_ARROW}
          </a>
          <a class="btn btn-ghost" href="mailto:{EMAIL}">Say hello</a>
        </div>
      </div>
      <div class="hero-art" aria-hidden="true">
        <svg viewBox="2 16 60 33" fill="none" stroke-width="0.85" stroke-linecap="round">
          <path class="twig" stroke-width="1.2" d="M4 46H60"/>
          <path class="needle" d="M10 46 15.0 37.3M11.5 43.4 11.1 41.4M13.1 40.6 12.8 39.0"/>
          <path class="needle" d="M19 46 28.5 29.5M20.5 43.4 20.0 40.3M22.1 40.6 21.6 37.9M23.7 37.9 23.3 35.5M25.3 35.1 25.0 33.1M26.9 32.3 26.6 30.8"/>
          <path class="needle" d="M28 46 41.0 23.5M29.5 43.4 28.9 40.3M31.1 40.6 30.5 37.5M32.7 37.9 32.1 34.7M34.3 35.1 33.8 32.3M35.9 32.3 35.5 29.9M37.5 29.5 37.1 27.5M39.1 26.8 38.8 25.1"/>
          <path class="needle" d="M37 46 46.5 29.5M38.5 43.4 38.0 40.3M40.1 40.6 39.6 37.9M41.7 37.9 41.3 35.5M43.3 35.1 43.0 33.1M44.9 32.3 44.6 30.8"/>
          <path class="needle" d="M46 46 52.0 35.6M47.5 43.4 47.1 41.2M49.1 40.6 48.8 38.8M50.7 37.9 50.4 36.4"/>
          <path class="needle" d="M55 46 58.0 40.8M56.5 43.4 56.2 41.9"/>
          <circle class="crystal" cx="41" cy="23.5" r="1.1"/>
        </svg>
      </div>
    </div>
  </div>

  <hr class="rule">

  <section id="games" aria-labelledby="games-title">
    <div class="wrap">
      <div class="section-head">
        <h2 id="games-title">Games</h2>
      </div>
      <div class="game-list">
      {banners}
      </div>
    </div>
  </section>'''
    return page('Huurre Studio — small games and apps, made with care',
                'Huurre Studio is an independent studio making games and apps for Android, iPhone and iPad.',
                '/', None, main)


def game_page(g):
    """A game's page, in the same calm layout as the home page: a hero with
    text beside the game's icon, a compact screenshot gallery, features,
    details, the game's Help (FAQ) and the other games."""
    chips = ''.join(f'<li>{c}</li>' for c in g['chips'])
    gallery = ''.join(
        f'<li><img src="/assets/{g["slug"]}/{f}" width="{w}" height="{h}" alt="{escape(alt)}" loading="lazy"></li>'
        for f, w, h, alt in g['images'] + g['gallery_extra'])
    features = ''.join(f'<div class="card"><h3>{t}</h3><p>{d}</p></div>' for t, d in g['features'])
    details = ''.join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in g['details'])
    aud = AUDIENCES[g['audience']]
    others = [o for o in GAMES if o is not g]
    more = ''
    if others:
        cards = ''.join(f'''<a class="mini-game" href="/{o["slug"]}/">
          <img src="/assets/{o["slug"]}/icon.png" width="256" height="256" alt="" loading="lazy">
          <span><strong>{o["name"]}</strong><small>{o["subtitle"]}</small></span>
        </a>''' for o in others)
        more = f'''
  <section class="band" aria-labelledby="more-title">
    <div class="wrap">
      <h2 id="more-title">More games</h2>
      <div class="mini-games">{cards}</div>
    </div>
  </section>'''
    main = f'''  <div class="hero game-hero">
    <div class="wrap">
      <div>
        <p class="crumbs"><a href="/#games">Games</a> <span aria-hidden="true">/</span> {g["name"]}</p>
        <p class="eyebrow">{g["status"]}</p>
        <h1>{g["name"]}</h1>
        <p class="game-page-sub">{g["subtitle"]}</p>
        <p class="lede">{g["summary"]}</p>
        <ul class="chips chips--plain" aria-label="Highlights">{chips}</ul>
        <div class="btns">
          {badge(g, ' badge-soon--plain')}
          <a class="btn btn-ghost" href="#help">Help &amp; questions</a>
        </div>
      </div>
      <div class="game-art game--{g["slug"]}" aria-hidden="true">
        <img src="/assets/{g["slug"]}/icon.png" width="256" height="256" alt="">
      </div>
    </div>
  </div>

  <section class="band" aria-labelledby="shots-title">
    <div class="wrap">
      <h2 id="shots-title">Screenshots</h2>
    </div>
    <ul class="gallery" tabindex="0" aria-label="{g["name"]} screenshots, scroll sideways for more">{gallery}</ul>
  </section>

  <section class="band" aria-labelledby="about-title">
    <div class="wrap">
      <h2 id="about-title">About the game</h2>
      <div class="grid-3">{features}</div>
      <dl class="details" aria-label="Game details">{details}</dl>
    </div>
  </section>

  <section class="band" id="help" aria-labelledby="help-title">
    <div class="wrap narrow">
      <h2 id="help-title">Help &amp; questions</h2>
      {faq(g["faq"])}
      <p class="small-print">Still stuck? Email <a href="mailto:{EMAIL}?subject={g["name"].replace(" ", "%20")}">{EMAIL}</a>. Privacy: {g["name"]} is a game for <a href="/privacy/#{aud["anchor"]}">{aud["label"].lower()}</a>.</p>
    </div>
  </section>
{more}'''
    title = f'{g["name"]}: {g["subtitle"]} | Huurre Studio'
    desc = f'{g["name"]}: {g["subtitle"]}. ' + g['summary']
    return page(title, desc, f'/{g["slug"]}/', g['slug'], main, g['og_image'])


GENERAL_FAQ = [
    ('Where is my progress saved?', '<p>On your device. Our games have no accounts, so progress stays on the phone or tablet you play on, and deleting a game deletes it.</p>'),
    ('Can I play offline?', '<p>Yes. All our games work without an internet connection; ads just don\'t load while you\'re offline.</p>'),
    ('Why are there ads, and can I change them?', '<p>Ads keep our games free. Games for all ages only ever show family-friendly, non-personalised ads. In games for 13 and over, you choose whether ads are personalised: in the game under <strong>Settings → Privacy Choices</strong>, on iPhone under <strong>Settings → Privacy &amp; Security → Tracking</strong>, and on Android under <strong>Settings → Google → Ads</strong>. More in our <a href="/privacy/">privacy policy</a>.</p>'),
    ('Which languages are supported?', '<p>Our games are available in 12 languages and follow your device\'s language. You can also change it in the game\'s settings.</p>'),
    ('I found a bug. What should I send?', f'<p>Email <a href="mailto:{EMAIL}">{EMAIL}</a> with the game\'s name, your phone or tablet model, and what happened. A screenshot helps. We usually reply within a few days.</p>'),
]


def support():
    games = ''.join(f'''<li><a href="/{g["slug"]}/#help"><span><strong>{g["name"]}</strong><small>{g["subtitle"]}</small></span>{ICON_ARROW}</a></li>'''
                    for g in GAMES)
    main = f'''  <div class="doc">
    <div class="wrap">
      <article class="prose">
        <h1>Support</h1>
        <p class="lede">Questions or problems with one of our games? The answers below cover all our games, and each game's page has its own help section.</p>
        <div class="contact-card">
          <div><strong>Email us</strong><p>We read every message and usually reply within a few days.</p></div>
          <a class="btn btn-primary" href="mailto:{EMAIL}">{EMAIL}</a>
        </div>

        <h2 id="common">Common questions</h2>
        {faq(GENERAL_FAQ)}

        <h2 id="game-help">Help for a specific game</h2>
        <ul class="link-list">{games}</ul>
      </article>
    </div>
  </div>'''
    return page('Support | Huurre Studio', 'Help with Huurre Studio games: answers to common questions and how to contact us.',
                '/support/', 'support', main)


def privacy():
    rows = ''.join(f'<tr><th scope="row"><a href="/{g["slug"]}/">{g["name"]}</a></th><td><a href="#{AUDIENCES[g["audience"]]["anchor"]}">{AUDIENCES[g["audience"]]["label"]}</a></td>'
                   f'<td>{AUDIENCES[g["audience"]]["ads"]}</td><td>{AUDIENCES[g["audience"]]["ad_id"]}</td></tr>' for g in GAMES)
    main = f'''  <div class="doc">
    <div class="wrap">
      <article class="prose">
        <h1>Privacy Policy</h1>
        <p class="meta">Updated {UPDATED}</p>
        <p class="lede">The short version: no accounts, no personal information, your game data stays on your device, and ads come from Google AdMob. Games for all ages only show child-directed, non-personalised ads.</p>

        <h2 id="who-we-are">Who we are</h2>
        <p>Our games are made by Huurre Studio. This policy covers all of them. Contact: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

        <h2 id="games">Our games</h2>
        <p>Each game is made either for all ages, including children, or for players aged 13 and over. That decides how its ads work:</p>
        <div class="table-scroll">
        <table>
          <thead><tr><th scope="col">Game</th><th scope="col">Made for</th><th scope="col">Ads</th><th scope="col">Advertising ID</th></tr></thead>
          <tbody>{rows}</tbody>
        </table>
        </div>

        <h2 id="game-data">Your game data</h2>
        <p>Your progress, scores, names and settings are stored only on your device. We never receive them, and deleting a game deletes them. Our games have no accounts, chat or in-app purchases, and never ask for your name, email, photos or location.</p>

        <h2 id="ads">Ads</h2>
        <p>Our games are free and show ads from Google AdMob, for example between levels or runs, and some let you choose to watch a short video for a reward. To show and measure ads, Google's ad software sends Google some technical information: your IP address (used to estimate your general region), ad interactions such as an ad being shown or tapped, diagnostic information such as loading times, and a device identifier used to limit repeats and detect ad fraud. It is encrypted in transit and handled under the <a href="https://policies.google.com/privacy">Google Privacy Policy</a>; see also <a href="https://policies.google.com/technologies/partner-sites">how Google uses data from apps</a>. We never sell information.</p>

        <h3 id="all-ages-games">Games for all ages</h3>
        <p>These games are played by children, so every ad request is marked as <strong>child-directed</strong>: ads are never personalised and are limited to content suitable for all ages, and the games don't use your device's advertising ID (the permission is removed from the app). We follow the Google Play Families Policy and design these games to comply with children's privacy laws such as COPPA (USA) and the GDPR (EU/EEA). Google handles this information under its rules for <a href="https://support.google.com/admob/answer/6223431">child-directed ad requests</a>.</p>

        <h3 id="teen-games">Games for 13 and over</h3>
        <p>Ads may be personalised, but only with your consent. Your advertising identifier is used only if you allow tracking. In the EEA, UK and Switzerland, personalised ads are based on your consent; basic ads and fraud prevention on legitimate interest. These games are not directed at children under 13.</p>

        <h2 id="choices">Your choices</h2>
        <ul>
          <li>Play offline: without an internet connection, no ads load and no information is sent.</li>
          <li>In games for 13 and over, change your ad consent any time in the game: <strong>Settings → Privacy Choices</strong> (where available).</li>
          <li>iPhone and iPad: turn tracking off in <strong>Settings → Privacy &amp; Security → Tracking</strong>.</li>
          <li>Android: delete or reset your advertising ID in <strong>Settings → Google → Ads</strong> (on some phones <strong>Settings → Privacy → Ads</strong>).</li>
          <li>Uninstalling a game removes everything it stored on your device.</li>
        </ul>

        <h2 id="rights">Your rights</h2>
        <p>We don't hold personal information about you, so there is nothing for us to delete. You can ask us about your data any time, or contact your data protection authority. Parents with questions are welcome to <a href="mailto:{EMAIL}">email us</a>.</p>

        <h2 id="changes">Changes</h2>
        <p>If anything changes, we'll update this page and its date.</p>
      </article>
    </div>
  </div>'''
    return page('Privacy Policy | Huurre Studio', 'How Huurre Studio games handle your information.', '/privacy/', 'privacy', main)


def not_found():
    main = '''  <section>
    <div class="wrap">
      <h1>Page not found.</h1>
      <p class="lede">The page you were looking for isn't here.</p>
      <div class="btns"><a class="btn btn-primary" href="/">Back to home</a><a class="btn btn-ghost" href="/#games">See our games</a></div>
    </div>
  </section>'''
    return page('Page not found | Huurre Studio', 'This page does not exist.', '/404.html', None, main)


# Old addresses that moved: each becomes a tiny page that forwards visitors
# (a static site can't send real redirects). Uploading overwrites them.
REDIRECTS = {
    'goat-bash/privacy/index.html': '/privacy/#all-ages-games',
}


def redirect(to):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Moved | Huurre Studio</title>
<meta name="robots" content="noindex">
<link rel="canonical" href="{BASE}{to.split('#')[0]}">
<meta http-equiv="refresh" content="0; url={to}">
</head>
<body><p>This page has moved to <a href="{to}">{BASE}{to}</a>.</p></body>
</html>
'''


def sitemap():
    paths = ['/'] + [f'/{g["slug"]}/' for g in GAMES] + ['/support/', '/privacy/']
    urls = '\n'.join(f'  <url><loc>{BASE}{p}</loc></url>' for p in paths)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n'


def write(rel, text):
    path = SITE / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8')
    print('wrote', rel)


if __name__ == '__main__':
    write('index.html', home())
    for g in GAMES:
        write(f'{g["slug"]}/index.html', game_page(g))
    write('support/index.html', support())
    write('privacy/index.html', privacy())
    write('404.html', not_found())
    write('sitemap.xml', sitemap())
    for rel, to in REDIRECTS.items():
        write(rel, redirect(to))

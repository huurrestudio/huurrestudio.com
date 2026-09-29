#!/usr/bin/env python3
"""Builds the Huurre Studio website.

Every page is generated from the templates and the GAMES list below, so the
header, footer, game banners and per-game sections are always consistent.
Edit this file, then run:  python3 _build/build.py   (from the site folder)

Adding a game: add an entry to GAMES (plus its images in assets/<slug>/ and a
theme block `.game--<slug>` in assets/site.css). It then appears on the home
page, gets its own page, a support section, a privacy section, footer links
and a sitemap entry automatically.
"""
from html import escape
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent
BASE = 'https://huurrestudio.com'
EMAIL = 'hello@huurrestudio.com'
UPDATED = '29 September 2026'
FONTS = ('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@1,9..144,400'
         '&family=Lilita+One&family=Manrope:wght@400;500;600;700;800&family=Space+Grotesk:wght@700&display=swap')

# ---------------------------------------------------------------------------
# The games. Text may contain simple HTML (<strong>, <a>).
# ---------------------------------------------------------------------------
GAMES = [
    {
        'slug': 'deep-signal',
        'name': 'Deep Signal',
        'title_html': 'Deep<br>Signal',
        'subtitle': 'Space Shooter',
        'status': 'Coming soon · Android &amp; iOS',
        'store_note': 'on Google Play &amp; the App Store',
        'summary': 'A fast, one-thumb space shooter. Steer while your ship fires on its own, pick upgrades as you level up, and survive the bosses.',
        'chips': ['One-thumb controls', 'Quick runs', '12 languages'],
        'shots': 'portrait',
        'images': [
            ('upgrade.jpg', 720, 1558, 'Deep Signal level-up screen: choose one of three upgrades — Rapid Fire, Vitality Cell or Swift Drive.'),
            ('menu.jpg', 720, 1558, 'Deep Signal main menu: the title above a glowing signal trace, a ship rising past a blue planet, and a Play button.'),
            ('gameplay.jpg', 720, 1558, "Deep Signal gameplay: the player's ship firing at purple and red enemy ships, with glowing pickups and a x16 combo."),
        ],
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
            ('How do I change my ad choices?', '<p>In the game: <strong>Settings → Privacy Choices</strong> (where available). On iPhone: <strong>Settings → Privacy &amp; Security → Tracking</strong>. On Android: <strong>Settings → Google → Ads</strong>.</p>'),
        ],
        'privacy_summary': ('13 and over', 'Personalised only with your consent', 'Only if you allow it'),
        'privacy': '''
        <p>Deep Signal is free and shows ads from Google AdMob between runs. To show and measure ads, Google may process your IP address, device information, ad interactions and, <strong>only if you allow tracking</strong>, your advertising identifier. See <a href="https://policies.google.com/technologies/partner-sites">how Google uses this data</a>.</p>
        <h3>Your choices in Deep Signal</h3>
        <ul>
          <li>Change your ad consent any time in the game: <strong>Settings → Privacy Choices</strong> (where available).</li>
          <li>iPhone and iPad: turn tracking off in <strong>Settings → Privacy &amp; Security → Tracking</strong>.</li>
          <li>Android: delete or reset your advertising ID in <strong>Settings → Google → Ads</strong> (on some phones <strong>Settings → Privacy → Ads</strong>).</li>
        </ul>
        <p>In the EEA, UK and Switzerland, personalised ads are based on your consent; basic ads and fraud prevention on legitimate interest.</p>
        <p>Deep Signal is not directed at children under 13.</p>''',
    },
    {
        'slug': 'goat-bash',
        'name': 'Goat Bash',
        'title_html': 'Goat<br>Bash',
        'subtitle': 'Fjord Trolls',
        'status': 'Coming soon · Android &amp; iOS',
        'store_note': 'on Google Play, then the App Store',
        'summary': 'A physics puzzle game for the whole family. Pick your herd, then leap, head-butt and splash cheeky trolls into the fjord.',
        'chips': ['Physics puzzles', '30 levels', '12 languages'],
        'shots': 'landscape',
        'images': [
            ('action.jpg', 1280, 600, 'Goat Bash gameplay: Big Billy head-butts a troll with a BONK!, a barrel of troll potion explodes and trolls fly towards the water.'),
            ('herd.jpg', 1280, 600, 'The Pick your herd screen under the northern lights: two leaps for Pip, two for Bramble and one for Big Billy.'),
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
            ('What about ads?', "<p>Goat Bash shows family-friendly ads between levels, and you can choose to watch a short video for 2 extra leaps. Ads are never personalised and the game doesn't use your advertising ID. Playing offline means no ads. See the <a href=\"/privacy/#goat-bash\">Goat Bash privacy section</a>.</p>"),
        ],
        'privacy_summary': ('All ages, including children', 'Child-directed, never personalised', 'Not used'),
        'privacy': '''
        <p>Goat Bash is free and shows ads from Google AdMob between levels, and you can choose to watch a short video for extra leaps. Because the game is played by children, <strong>every ad request is marked as child-directed</strong>: ads are never personalised, are limited to content suitable for all ages, and the game does not use your device's advertising ID.</p>
        <p>To show and count ads, Google's ad software sends Google some technical information: your IP address (used to estimate your general region), ad interactions such as an ad being shown or tapped, diagnostic information such as loading times, and an app-specific device identifier used to limit repeats and detect ad fraud. It is encrypted in transit and handled under the <a href="https://policies.google.com/privacy">Google Privacy Policy</a> and Google's rules for <a href="https://support.google.com/admob/answer/6223431">child-directed ad requests</a>. It is not used to build a profile of you.</p>
        <h3>Made for all ages</h3>
        <p>We follow the Google Play Families Policy and designed Goat Bash to comply with children's privacy laws such as COPPA (USA) and the GDPR (EU/EEA):</p>
        <ul>
          <li>the game asks for no personal information: no name, email, photos or location permission;</li>
          <li>all ads are child-directed, non-personalised and limited to all-ages content;</li>
          <li>the advertising ID and similar tracking permissions are removed from the app.</li>
        </ul>
        <h3>Your choices in Goat Bash</h3>
        <ul>
          <li>Play offline: without an internet connection, no ads load and no information is sent.</li>
          <li>Parents with questions are welcome to <a href="mailto:hello@huurrestudio.com">email us</a>.</li>
        </ul>''',
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
BRAND_MARK = ('<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="4.5" stroke-linecap="round" aria-hidden="true">'
              '<path d="M8 46H56M14 46 19 37M23 46 31.5 31.3M32 46 43 27M41 46 49 32.1M50 46 54 39.1"/></svg>')

NAV = [('games', '/#games', 'Games'), ('support', '/support/', 'Support'), ('privacy', '/privacy/', 'Privacy')]


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
<link rel="stylesheet" href="/assets/site.css">
</head>'''


def header(current):
    links = '\n      '.join(
        f'<a href="{href}"' + (' aria-current="page"' if key == current else '') + f'>{label}</a>'
        for key, href, label in NAV)
    return f'''<body>
<a class="skip" href="#main">Skip to content</a>

<header class="site-header">
  <div class="wrap">
    <a class="brand" href="/" aria-label="Huurre Studio, home">
      {BRAND_MARK}
      Huurre <span>Studio</span>
    </a>
    <nav class="nav" aria-label="Main">
      {links}
    </nav>
  </div>
</header>
'''


def footer():
    games = '\n      '.join(f'<a href="/{g["slug"]}/">{g["name"]}</a>' for g in GAMES)
    return f'''
<footer class="site-footer">
  <div class="wrap">
    <p style="margin:0">© 2026 Huurre Studio · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
    <nav aria-label="Footer">
      {games}
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


def badge(g):
    return (f'<span class="badge-soon" role="note">{ICON_PHONE}'
            f'<span>Coming soon<small>{g["store_note"]}</small></span></span>')


def shots(g, lazy_from=1):
    items = []
    for i, (file, w, h, alt) in enumerate(g['images']):
        lazy = ' loading="lazy"' if i >= lazy_from else ''
        items.append(f'<div class="shot"><img src="/assets/{g["slug"]}/{file}" width="{w}" height="{h}" alt="{escape(alt)}"{lazy}></div>')
    return f'<div class="shots shots--{g["shots"]}">\n          ' + '\n          '.join(items) + '\n        </div>'


def banner(g, heading, with_link):
    """The one game banner, used on the home page and on the game's page."""
    tag = 'h1' if heading == 1 else 'h3'
    link = f'<a class="btn btn-primary" href="/{g["slug"]}/">Learn more</a>\n            ' if with_link else ''
    chips = ''.join(f'<li>{c}</li>' for c in g['chips'])
    return f'''<article class="game game--{g["slug"]}" aria-labelledby="{g["slug"]}-title">
        <div class="game-text">
          <img class="game-icon" src="/assets/{g["slug"]}/icon.png" width="256" height="256" alt="">
          <p class="eyebrow">{g["status"]}</p>
          <{tag} id="{g["slug"]}-title" class="game-title">{g["title_html"]}</{tag}>
          <p class="game-sub">{g["subtitle"]}</p>
          <p class="game-summary">{g["summary"]}</p>
          <ul class="chips" aria-label="Highlights">{chips}</ul>
          <div class="btns">
            {link}{badge(g)}
          </div>
        </div>
        {shots(g)}
      </article>'''


def mini_card(g):
    return f'''<a class="mini-game" href="/{g["slug"]}/">
          <img src="/assets/{g["slug"]}/icon.png" width="256" height="256" alt="" loading="lazy">
          <span><strong>{g["name"]}</strong><small>{g["subtitle"]}</small></span>
        </a>'''


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------
def home():
    banners = '\n\n      '.join(banner(g, 3, True) for g in GAMES)
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
    features = ''.join(f'<div class="card"><h3>{t}</h3><p>{d}</p></div>' for t, d in g['features'])
    details = ''.join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in g['details'])
    others = [o for o in GAMES if o is not g]
    more = ''
    if others:
        more = f'''
  <section class="flush-top" aria-labelledby="more-title">
    <div class="wrap">
      <h2 id="more-title" class="h3">More from Huurre Studio</h2>
      <div class="mini-games">
        {''.join(mini_card(o) for o in others)}
      </div>
    </div>
  </section>'''
    main = f'''  <section class="page-top">
    <div class="wrap">
      {banner(g, 1, False)}
    </div>
  </section>

  <section class="flush-top" aria-label="Features">
    <div class="wrap">
      <div class="grid-3">{features}</div>
      <div class="game-facts">
        <dl class="details" aria-label="Game details">{details}</dl>
        <div class="help-links">
          <a class="btn btn-ghost" href="/support/#{g["slug"]}">{g["name"]} support</a>
          <a class="btn btn-ghost" href="/privacy/#{g["slug"]}">{g["name"]} privacy</a>
        </div>
      </div>
    </div>
  </section>
{more}'''
    title = f'{g["name"]}: {g["subtitle"]} | Huurre Studio'
    desc = f'{g["name"]}: {g["subtitle"]} — ' + g['summary']
    return page(title, desc, f'/{g["slug"]}/', 'games', main, g['og_image'])


def game_switcher(prefix):
    return '<nav class="game-switch" aria-label="Games">' + ''.join(
        f'<a href="#{g["slug"]}"><img src="/assets/{g["slug"]}/icon.png" width="256" height="256" alt="">{g["name"]}</a>'
        for g in GAMES) + '</nav>'


def section_heading(g, suffix=''):
    return (f'<h2 id="{g["slug"]}" class="game-heading"><img src="/assets/{g["slug"]}/icon.png" width="256" height="256" alt="">'
            f'{g["name"]}{suffix}</h2>')


def support():
    blocks = []
    for g in GAMES:
        faq = '\n'.join(f'''        <details>
          <summary>{q}</summary>
          <div>{a}</div>
        </details>''' for q, a in g['faq'])
        blocks.append(f'''        {section_heading(g)}
        <div class="faq">
{faq}
        </div>
        <p class="section-links"><a href="/{g["slug"]}/">About {g["name"]}</a> · <a href="/privacy/#{g["slug"]}">{g["name"]} privacy</a></p>''')
    main = f'''  <div class="doc">
    <div class="wrap">
      <article class="prose">
        <h1>Support</h1>
        <p class="lede">Questions or problems with one of our games? Find your game below, or send us an email.</p>
        <div class="btns email-btn"><a class="btn btn-primary" href="mailto:{EMAIL}">{EMAIL}</a></div>
        {game_switcher('')}

{chr(10).join(blocks)}

        <h2 id="general">Something not working?</h2>
        <p>Email us at <a href="mailto:{EMAIL}">{EMAIL}</a> and tell us which game, your phone or tablet model, and what happened. A screenshot helps. We usually reply within a few days.</p>
      </article>
    </div>
  </div>'''
    return page('Support | Huurre Studio', 'Help with Huurre Studio games: answers to common questions and how to contact us.',
                '/support/', 'support', main)


def privacy():
    rows = ''.join(f'<tr><th scope="row"><a href="#{g["slug"]}">{g["name"]}</a></th>' + ''.join(f'<td>{c}</td>' for c in g['privacy_summary']) + '</tr>'
                   for g in GAMES)
    sections = '\n'.join(f'''        {section_heading(g)}
{g["privacy"]}''' for g in GAMES)
    main = f'''  <div class="doc">
    <div class="wrap">
      <article class="prose">
        <h1>Privacy Policy</h1>
        <p class="meta">Updated {UPDATED}</p>
        <p class="lede">One policy for all our games. The short version: no accounts, your game data stays on your device, and ads come from Google AdMob. Each game's section explains how its ads work.</p>
        {game_switcher('')}

        <h2 id="who-we-are">Who we are</h2>
        <p>Our games are made by Huurre Studio. Contact: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

        <h2 id="summary">Our games at a glance</h2>
        <div class="table-scroll">
        <table>
          <thead><tr><th scope="col">Game</th><th scope="col">Made for</th><th scope="col">Ads</th><th scope="col">Advertising ID</th></tr></thead>
          <tbody>{rows}</tbody>
        </table>
        </div>

        <h2 id="game-data">Your game data</h2>
        <p>Your progress, scores, names and settings are stored only on your device. We never receive them. Deleting a game deletes them. None of our games has accounts, chat or in-app purchases.</p>

{sections}

        <h2 id="your-rights">Your rights and choices</h2>
        <ul>
          <li>We don't hold personal information about you, so there is nothing for us to delete. For information handled by Google, see the <a href="https://policies.google.com/privacy">Google Privacy Policy</a>.</li>
          <li>Ask us about your data any time, or contact your data protection authority.</li>
          <li>We never sell information.</li>
        </ul>

        <h2 id="changes">Changes</h2>
        <p>If anything changes, we'll update this page and its date.</p>
      </article>
    </div>
  </div>'''
    return page('Privacy Policy | Huurre Studio', 'How Huurre Studio games handle your information, game by game.',
                '/privacy/', 'privacy', main)


def not_found():
    main = '''  <section>
    <div class="wrap">
      <h1>Page not found.</h1>
      <p class="lede">The page you were looking for isn't here.</p>
      <div class="btns"><a class="btn btn-primary" href="/">Back to home</a><a class="btn btn-ghost" href="/#games">See our games</a></div>
    </div>
  </section>'''
    return page('Page not found | Huurre Studio', 'This page does not exist.', '/404.html', None, main)


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

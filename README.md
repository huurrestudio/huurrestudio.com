# Huurre Studio website

A plain static site with no build step: HTML and CSS, plus images. Host it free on GitHub Pages under **huurrestudio.com**.

```
index.html              Home
deep-signal/index.html  Deep Signal page
goat-bash/index.html    Goat Bash page
goat-bash/privacy/      Goat Bash privacy policy (all ages, child-directed ads)
support/index.html      Support / FAQ
privacy/index.html      Privacy Policy
404.html                "Page not found"
app-ads.txt             AdMob seller declaration (pub-6257007554304023)
CNAME                   Tells GitHub Pages the custom domain
favicon.svg, apple-touch-icon.png, assets/…  Logo, styles, screenshots, share image
```

## 1. Fill in the placeholders (privacy page)

Open `privacy/index.html` and replace the three highlighted placeholders (`<mark class="todo">…</mark>`):

1. **Your full legal name.** Required: the policy has to name a real person or company as data controller.
2. **Your country**, and the matching data-protection authority. In Finland that's *Tietosuojavaltuutetun toimisto*, tietosuoja.fi.
3. **The age statement.** Make sure "not directed at children under 13" matches the age rating you pick in App Store Connect.

Remove the `<mark class="todo">` tags once you've filled them in.

## 2. Buy the domain and set up email (name.com)

1. Buy **huurrestudio.com**.
2. Under **Email Forwarding**, forward `hello@huurrestudio.com` to your personal inbox, so your own address never appears publicly.

## 3. Publish on GitHub Pages

1. Create a free account at github.com, if you don't have one.
2. Create a **public** repository called, for example, `huurrestudio.com`.
3. Click **Add file → Upload files** and drag in **everything inside this folder**. `.nojekyll` and `CNAME` are hidden files: in Finder, press ⌘⇧. to show them. Then click **Commit changes**.
4. Open **Settings → Pages**. Under Source, choose **Deploy from a branch**, branch **main**, folder **/ (root)**, and save.
5. **Custom domain** should already say `huurrestudio.com`, taken from the CNAME file.

## 4. Point the domain at GitHub (name.com → DNS records)

| Type | Host | Value |
|---|---|---|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | *your-github-username*.github.io |

Delete any default "parking" A records name.com created. After DNS updates (minutes to a few hours), go back to **Settings → Pages** and tick **Enforce HTTPS**.

## 5. Use the URLs

| Where | Field | URL |
|---|---|---|
| AdMob → Privacy & messaging | App privacy policy | https://huurrestudio.com/privacy/ |
| App Store Connect → App Information | Privacy Policy URL | https://huurrestudio.com/privacy/ |
| App Store Connect → Version | Support URL | https://huurrestudio.com/support/ |
| App Store Connect → Version | Marketing URL | https://huurrestudio.com/deep-signal/ |
| App Store Connect → Developer website (via your App Store listing) | Needed for app-ads.txt | https://huurrestudio.com |

AdMob checks `https://huurrestudio.com/app-ads.txt` on the domain listed as your developer website in the App Store, usually within 24 hours after the app goes live.

## 6. When Deep Signal launches

In `index.html` and `deep-signal/index.html`, replace the **"Coming soon · on the App Store"** badge with Apple's official "Download on the App Store" badge, linked to your App Store URL. Get the badge from developer.apple.com/app-store/marketing/guidelines.

## Editing later

- Colours and spacing: `assets/site.css`. The tokens at the top control light and dark mode.
- Header and footer are repeated in each page. If you add a link, update all seven HTML files.

"""Genuine patient reviews copied word for word from Dr. Vikeerna Bharti's public Google profile.

Owner decision (17 Oct 2026): show every review (not a selection), unedited, refreshed weekly.
Names are shortened to first name + initial. Dates are the month Google shows (relative dates converted
on the check date). Hindi reviews use Google's own English translation, labelled as such.
No AggregateRating or Review schema: the reviews are shown for patients, not marked up for search results.

To refresh: open the profile on Google Maps → Reviews → Newest, add new reviews at the top of REVIEWS,
update CHECKED, RATING and COUNT, then rebuild.
"""
from html import escape as e

PLACE_ID = 'ChIJxcKRJAbj9DkREUTv8FsVn08'
PROFILE_URL = 'https://www.google.com/maps/search/?api=1&amp;query=Dr.+Vikeerna+Bharti%2C+Bariatu+Road%2C+Ranchi&amp;query_place_id=' + PLACE_ID
WRITE_URL = 'https://search.google.com/local/writereview?placeid=' + PLACE_ID
CHECKED = '17 October 2026'
RATING = '4.9'
COUNT = 13

# Owner decision (17 Oct 2026, after Codex compliance review against the NMC 6 Oct 2026 advertising guidelines):
# no review cards and no rating figure on the site; link to the Google profile instead. True restores the cards.
SHOW_CARDS = False
CONTACT = 'contact@drbhartisurgery.com'

# (name, stars, approximate month, text, translated_from) — newest first as listed by Google on the check date.
# Months are approximate: converted from Google's relative ages (e.g. "3 months ago") on CHECKED.
REVIEWS = [
 ('Sunita D.', 5, 'October 2026', 'Best general and laproscopic surgeon, consult for my relative, almost all senior surgeon of Ranchi refused to treat as case is too critical,  but De Vikeerna Bharti treated , I must say life saving surgery. Thankyou sir  Will recommend for general surgery cases must concern once .', ''),
 ('Amanullah A.', 5, 'October 2026', 'He is the best doctor of surgery.', 'Hindi'),
 ('Jyoti M.', 5, 'October 2026', 'Best doctor for surgery', ''),
 ('Binita T.', 5, 'September 2026', 'Dr. Vikram Bharti Sir is a very good doctor, my patient recovered very quickly after the surgery...', 'Hindi'),
 ('Niket D.', 4, 'September 2026', 'Trusted Doctor', ''),
 ('Santosh K.', 5, 'September 2026', '', ''),
 ('Nishi N.', 5, 'September 2026', 'Had a great experience with Dr. Vikeerna Bharti sir,  there is lots of improvement with his treatment.', ''),
 ('Kumar V.', 5, 'September 2026', "Sir's behavior and treatment are both good, I would like to continue meeting him even if I am not sick.", 'Hindi'),
 ('Jai K.', 5, 'August 2026', 'Better', ''),
 ('Deepa T.', 5, 'July 2026', 'Had a great experience with Dr. Vikeerna Bharti sir,He listened patiently explained everything clearly and made feel very comfortable thoughtout the consultation', ''),
 ('Binod K.', 5, 'July 2026', 'Very nice and friendly doctor, there is lots of improvement in my stomach problems with his treatment.thank you so much doctor....', ''),
 ('Sanjeev K.', 5, 'July 2026', 'Visited Ranchi dental & polyclinic for my diagnosis of my appendix. Satisfied with the consultation, truly recommended to anyone looking for the best services provided here', ''),
 ('Purendra M.', 5, 'July 2026', '', ''),
]
assert len(REVIEWS) == COUNT


def _card(name, stars, month, text, translated):
    star_text = '★' * stars + '☆' * (5 - stars)
    body = f'<p>{e(text.strip())}</p>' if text.strip() else '<p class="review-empty">Rating only, no written comment.</p>'
    note = f'<p class="journey-small">Translated from {e(translated)} by Google</p>' if translated else ''
    return (f'<article class="review-card"><p class="review-stars" role="img" aria-label="{stars} out of 5 stars"><span aria-hidden="true">{star_text}</span></p>'
            f'{body}{note}<p class="review-meta">{e(name)} · Approx. {e(month)} · Google review</p></article>')


def review_cards(limit=None):
    """All reviews, newest first; with a limit, the rest sit behind a 'show all' toggle."""
    shown = REVIEWS if limit is None else REVIEWS[:limit]
    rest = [] if limit is None else REVIEWS[limit:]
    html = '<div class="review-grid">' + ''.join(_card(*r) for r in shown) + '</div>'
    if rest:
        html += (f'<details class="review-more"><summary>Show all {COUNT} reviews</summary><div class="review-grid">'
                 + ''.join(_card(*r) for r in rest) + '</div></details>')
    return html


def review_summary():
    if not SHOW_CARDS:
        return '<p class="review-summary">Dr. Bharti’s public listing and reviews are available on Google.</p>'
    return (f'<p class="review-summary"><strong>Google review snapshot.</strong> This snapshot contains {COUNT} reviews recorded from Dr. Bharti’s public Google profile, checked on {CHECKED}. '
            'Reviews are arranged newest first. Review text is reproduced as recorded; three reviews use Google’s English translation and are labelled. '
            'Names are abbreviated and month labels are approximate. These are reviewers’ personal opinions, not verified clinical outcomes or guarantees of treatment results. '
            f'Google’s current profile may differ. Google profile rating at the check: {RATING}/5 from {COUNT} reviews.</p>'
            f'<p class="journey-small">To ask for a review shown here to be corrected or removed, email <a href="mailto:{CONTACT}">{CONTACT}</a>.</p>')


def review_section_cards(limit):
    return review_cards(limit) if SHOW_CARDS else ''


def privacy_sentence():
    if SHOW_CARDS:
        return ('Review cards on the homepage and Bariatu clinic page are stored on this website, using text recorded from the public Google profile. '
                'Some cards use Google’s English translation and are labelled; names are abbreviated and month labels are approximate. '
                'The cards do not load a Google Maps iframe or retrieve reviews from Google when you view them. '
                'Google Analytics and any external font services may still contact their providers. Links to Google open Google’s own service.')
    return ('The homepage and Bariatu clinic page link to Dr. Bharti’s Google profile and reviews; '
            'they do not load a Google Maps iframe or retrieve reviews from Google when you view them. '
            'Google Analytics and any external font services may still contact their providers. Links to Google open Google’s own service.')


def review_actions():
    return (f'<div class="journey-actions"><a class="journey-button" href="{PROFILE_URL}" target="_blank" rel="noopener">{"See all reviews on Google" if SHOW_CARDS else "Open Google profile"} ↗</a>'
            f'<a class="journey-button secondary" href="{WRITE_URL}" target="_blank" rel="noopener">Write a review ↗</a></div>')

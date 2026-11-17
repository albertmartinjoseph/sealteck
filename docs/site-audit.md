# Sealteck website audit

Audit date: 17 November 2026. Scope: public, accessible content at https://sealteck.co.uk/ and design reference https://www.aramco.com/.

## Evidence and verification limits

The web reader could not access Sealteck, but direct HTTPS requests succeeded (HTTP 200). Saved homepage, all four linked inner pages, published-page API response, original page styles, and an original image under `docs/source/`. `content-inventory.json` preserves each published page's HTML and decoded text; `asset-urls.txt` records discovered uploaded assets. These are migration evidence, not application code.

Aramco's homepage was read through the web reader and downloaded separately. Its content hierarchy and responsive styling were inspected. No browser-rendered desktop/mobile screenshots or interactive browser tests have been performed. Visual conclusions are based on markup, CSS, and the user's reference brief; precise rendered appearance remains to be checked.

## Existing platform and navigation

WordPress, Twenty Twenty theme, Elementor and Elementor Pro. Other plugin assets include ElementsKit, Essential Addons and WPForms; the actual contact form is an Elementor form.

Primary navigation: Home, About Us, SERVICE, Sectors We Serve, Contact Us. Footer repeats these pages and adds company introduction, support details, office address and social labels.

| Page | Existing URL | Observed content |
| --- | --- | --- |
| Home | `/` | Hero, About introduction, enquiry CTA, six quality/service benefits, Latest Projects image gallery, three FAQs |
| About Us | `/?page_id=111` | Company background, engineering management, mission, four reasons to choose Sealteck, enquiry CTA |
| SERVICE | `/?page_id=158` | Installation introduction and four stages of service |
| Sectors We Serve | `/?page_id=169` | Introduction and six detailed industry groups |
| Contact Us | `/?page_id=143` | Phone/email/location panels and message form |
| Sample Page | `/?page_id=2` | Unlinked standard WordPress sample text, not Sealteck business content |

The public pages API returned these six published pages. No separate product, project-detail, certification, testimonial, privacy or news page was found in this response or business navigation. This does not prove that no other server resources exist. Do not create business claims from the sample page's fictional examples. Preserve its URL in a compatibility route pending an explicit content removal decision.

## Verified business identity and contact details

- Public brand: Sealteck; sectors page uses “Sealteck Sealing Solutions Limited”.
- Phone displayed in site header/footer: `+447776683424`.
- Email displayed in site header/footer and contact page: `info@sealteck.co.uk`.
- Address: Office 1111, 60 Tottenham Court Road, Fitzrovia, London W1T 2EW.
- Existing footer: Copyright © 2026 Sealteck. All rights reserved.
- Social labels include Facebook, X/Twitter, Instagram and LinkedIn. No verified external profile destinations were found in the homepage link inventory; `#` placeholders must not be represented as working profiles.

## Content inventory

Full original text is retained in `source/content-inventory.json`; the following is a structural index rather than replacement copy.

### Home

Hero headline: “Protecting Critical Infrastructure with Advanced Sealing Solutions”. Supporting copy describes professional mechanical seal installation for cable and pipe entries, protecting against fire, water, air and dust ingress. Actions lead to Services and Contact.

About introduction describes the company's response to inferior sealing products and substandard workmanship. “Need Reliable Sealing Solutions?” introduces the enquiry CTA.

Quality Services contains Industry Expertise, Complete Infrastructure Protection, High-Quality Installation Standards, Tailored Sealing Solutions, Reliable & Efficient Service, and Trusted Across Industries. Each has supporting copy preserved in the content inventory.

“Latest Projects” contains images without verified project names, locations or case-study descriptions. Do not imply these are independently verified completed Sealteck projects. Preserve the existing gallery and heading without adding factual captions; flag provenance for owner review.

FAQs cover services offered, industries served and the importance of mechanical sealing. The last answer ends with the apparent editing artifact “-answer for”; retain it in evidence and remove that fragment from presentation as a copy correction.

### About Us

Company narrative references Electronics and Mechanical Engineering experience, principal contractors, high-voltage substations, power plants, commercial construction and Oil & Gas. Mission and community/project value copy follow.

Reasons to choose Sealteck: Uncompromising Product Quality; Elite Workmanship; Bulletproof Documentation & Reporting; An Unrivalled Warranty. Existing superlative and warranty statements are source claims, not independently verified certifications. Preserve the original wording without inventing warranty duration or additional assurances.

### Services

1. Site Survey & Documentation: wall sleeve inner diameter, cable/pipe outer diameters, cable count and configuration.
2. Precision Installation: calibrated torque tools, alignment and manufacturer-approved methods.
3. Integrity & Tightness Testing: pressure/tightness testing and correction of gaps.
4. Warranty Certification: documentation certifying workmanship warranty after successful testing.

No standalone named product catalogue was discovered. Do not invent one.

### Sectors We Serve

| Group | Existing applications |
| --- | --- |
| Infrastructure | Advanced facilities/data centers; transport; construction/buildings; utilities/telecom |
| Manufacturing Industry | Food/beverage; robotics/automation; rolling stock; defense vehicles |
| Marine | Commercial shipping; passenger vessels; defense |
| Offshore Oil & Gas | Rigs/platforms; drill ships; support vessels; FPSOs |
| Power Generation & Distribution | Renewable energy; traditional power; transmission/distribution |
| Process Industries | Mining/metals; onshore oil/gas/petrochemical; pulp/paper |

Each group has original introduction, descriptive paragraph and application details in the archived inventory. Preserve them all.

### Contact functionality

Form fields: First Name, Last Name, Email Address (required in the original), Message; button: Send Message. Original form has `post_id=143`, `form_id=c0c2d6f` and uses Elementor's WordPress AJAX infrastructure at `/wp-admin/admin-ajax.php`. Markup is archived in `source/contact-form.html`.

Delivery, recipient configuration, anti-spam behavior, CORS support and success/error responses are unverified. No test enquiry was sent. A React front end cannot claim functional delivery merely by reproducing the fields or showing a success message.

Contact-page anchor targets include `tel:+91%209513939595` and `mailto:info@eleqtris.com`, which conflict with Sealteck's displayed UK phone/email. Correct the rebuilt contact links to the consistent displayed Sealteck details and retain this discrepancy as audit evidence.

## Branding and assets

The header's brand is an HTML `h2` containing “SEALTECK”, rather than an image logo in the inspected header. Preserve that wordmark treatment; do not invent an emblem. The homepage's `Image.png` is a construction/personnel composite, visually inspected and archived, not a logo.

Observed component styles use blue `#2E489E` extensively and orange `#F69220` as an accent. Supporting colors include white, black, `#565656` and pale gray. The global Elementor kit contains generic defaults (`#6EC1E4`, `#61CE70`); these must not be mistaken for the actively applied main brand palette. Existing fonts include Oswald, Roboto and Roboto Slab.

Original uploaded images include the construction composite, industrial/power imagery, installation imagery, a data-center infrastructure image and several stock-image filenames. Page styles also reference `pexels-photo-417273.jpeg`, `images.jpg` and `WhatsApp-Image-2026-07-17-at-14.21.14-_1_.jpg`. Asset URLs are archived; availability, actual subject, dimensions and suitability require individual verification before use. No image should be described as a particular customer/project without supporting source content.

## Aramco design reference

The homepage source establishes an image-led lead-story area, an introductory editorial statement, themed exploration links, further image/story modules and a substantial grouped footer. Styles contain responsive breakpoints and restrained transform-based link/icon transitions. This supports a design direction of strong editorial scale, generous space, image-led navigation and controlled motion.

Full-height industrial hero imagery, transparent navigation and minimal corporate composition are also explicit user requirements. They are proposed Sealteck design decisions; exact rendered parity with Aramco has not been verified. No Aramco imagery, brand, copy, metrics or source code will be reused.

## Risks and follow-up

- Verify all original images and their permitted reuse; avoid enlarging low-resolution thumbnails into hero images.
- Confirm a production form backend and perform an authorized delivery test before claiming form completion.
- Keep old query-string URLs working; React Router pathname matching alone will not handle them.
- Preserve unlinked sample-page compatibility without treating its fictional content as business identity.
- Verify actual rendered layout, mobile menu, contrast, focus, responsive crops and keyboard behavior during implementation QA.

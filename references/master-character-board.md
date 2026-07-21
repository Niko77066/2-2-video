# Master character board

Use this reference whenever GPT Image 2 creates or revises a recurring character asset. Treat the counts and panel hierarchy as production constraints, not suggestions.

## Selection rule

- Default to one unified 4:3 horizontal master board.
- Keep `MAIN IDENTITY + SCALE` visually dominant and large enough for facial, clothing, and proportion inspection.
- Use short English titles and labels. Keep the world note to one or two short sentences. Do not request paragraph-sized typography.
- If the first unified result makes faces, hands, labels, or materials too small or inconsistent, switch to the two-board fallback at the end of this file.

## Unified GPT Image 2 prompt

```text
Create a single unified MASTER CHARACTER REFERENCE SHEET for an AI video continuity pipeline.

STYLE
[STYLE: anime / stylized 3D / realistic 3D / live-action / cinematic realism / noir / stop-motion / other]
Apply this style only to the character, costume, prop, and visual render panels. Keep the board layout itself neutral, minimal, technical, and production-oriented.

SUBJECT
Name: [NAME]
Alias: [ALIAS OR NONE]
Role: [ROLE]
Age: [AGE OR RANGE]
Personality: [3-5 TRAITS]
Core theme: [THEME]
Speech accent: [ACCENT OR NEUTRAL]
World: [ONE OR TWO SHORT SENTENCES]

IDENTITY LOCK
- Build and proportions: [HEIGHT IMPRESSION, BODY TYPE, LIMB PROPORTIONS, POSTURE]
- Face: [FACE SHAPE, SKIN TONE, EYES, BROWS, NOSE, MOUTH, DISTINCTIVE MARK]
- Hair: [COLOR, LENGTH, SILHOUETTE, PARTING, TEXTURE, ORNAMENT]
- Wardrobe: [OUTERWEAR, INNER LAYERS, WAIST, LOWER BODY, FOOTWEAR]
- Materials: [FABRICS, LEATHER, METAL, WOOD, STONE]
- Accessories: [LIST]
- Movement quality: [RESTRAINED / PRECISE / FAST / HEAVY / ELASTIC]
- Action specialty: [SPECIALTY]
- Key prop: [PROP OR NONE]

BOARD FORMAT
4:3 horizontal. Pure white or clean warm off-white background. Clear grid, generous margins, readable English labels, balanced spacing, no clutter, no watermark, no logo. High resolution, premium official production visual bible, professional concept-art finish. Avoid tiny or dense text.

LAYOUT HIERARCHY
Top row: left = title and compact TOP INFO BLOCK; right = COLOR PALETTE.
Center-left and center = MAIN IDENTITY + SCALE, the largest and most prominent section.
Right column = EXPRESSION PROGRESSION, MICRO EXPRESSIONS, HEAD DETAIL, NEUTRAL BASELINE, POSTURE VARIATION, and one CLOSE-UP POSE.
Bottom row = WARDROBE / ACCESSORY DETAILS, optional PROP, and HAND GESTURES.

TITLE
Use the exact title: "CHARACTER REFERENCE SHEET"

1. TOP INFO BLOCK
Use short readable values only: Name, Alias, Role, Age, Personality, Core Theme, Speech Accent, World Note.

2. COLOR PALETTE
Place 6-8 clean unlabeled color swatches in the top-right header. Match skin, hair, wardrobe, materials, world, and mood.

3. MAIN IDENTITY + SCALE — DOMINANT SECTION
Show exactly four full-body neutral views of the same character: Front, 3/4 View, Side, Back.
Place all views on subtle height and proportion guide lines.
No handheld prop, bag, action pose, or item interaction in these four views.
Add exactly two small secondary silhouette thumbnails in one corner: Neutral Stance and Profile Silhouette.
Add only a few short callout notes for silhouette, posture, special traits, and visual identity.

4. EXPRESSION PROGRESSION
Show exactly eight face panels of the same character: Neutral, Curious, Worried, Surprised, Afraid, Sad, Determined, Relieved.

5. MICRO EXPRESSIONS
Show exactly five face panels: Subtle Eye Tension, Slight Smirk, Lip Tension, Micro Fear, Controlled Breath.

6. HEAD DETAIL SHEET
Show exactly five consistent head references: 3/4 Headshot, Side Headshot, Top Angle, Low Angle, Diagonal Angle.

7. NEUTRAL BASELINE
Show exactly one fully relaxed panel with no emotion.

8. POSTURE VARIATION
Show exactly three panels: Relaxed, Tense, Confident.

9. CLOSE-UP POSE
Show exactly one cinematic chest-up or shoulder-up pose that fits the character's personality and story tone. Preserve face, hair, expression, and upper-wardrobe identity.

10. WARDROBE / ACCESSORIES DETAILS
Show exactly four close-up callouts chosen from hairstyle, outerwear, footwear, accessory, fabric, material, fastener, embroidery, or armor construction. Make each useful for reconstruction.

11. PROP — OPTIONAL
Include only when the prop is important. Show exactly one isolated prop with a compact info block: Object Name, Type, Traits. Do not place the prop inside the four MAIN IDENTITY views.

12. HAND GESTURES
Show exactly five anatomically correct hands belonging to this character: Relaxed Hand, Tense Fingers, Pointing, Gripping, Subtle Gesture Near Face.

OPTIONAL HERO INSERT
Include one small cinematic hero illustration only when the user requests art direction or mood. Limit it to at most 20% of the board. Never reduce the MAIN IDENTITY, face, hand, or detail panels to make room for it.

CONSISTENCY
Every panel depicts one identical person. Preserve facial geometry, eye shape and spacing, hairstyle, body proportions, height, skin tone, outfit pattern placement, layer construction, materials, accessories, damage state, and palette. Preserve left/right orientation of asymmetric features. Use one neutral lens language for reference panels. Keep lighting even enough to read true colors and materials.

NEGATIVE
No second character, alternate outfit, hairstyle change, age change, body change, inconsistent face, mirrored asymmetric details, missing garment layers, merged panels, repeated panels, wrong panel counts, hidden hands, cropped feet, extra fingers, extra limbs, distorted anatomy, illegible tiny typography, dense paragraphs, decorative UI, logo, watermark, modern objects, or unrelated props.
```

## Art-direction insert

When the user supplies strong cinematic direction, append a short block without weakening the technical board:

```text
ART DIRECTION
- Genre and production level: [AAA game / feature animation / cinematic realism / other]
- Mood: [MOOD]
- Character lighting: [KEY, RIM, PRACTICALS]
- Character palette: [COLORS]
- Material rendering: [SILK, METAL, LEATHER, WOOD, ETC.]
- Optional hero insert environment: [SHORT SCENE]
Keep reference panels evenly lit; apply dramatic lighting only to the optional hero insert and cinematic close-up.
```

## Two-board fallback

Use this fallback after one unified board fails due to panel density, small faces, unreadable labels, or identity drift.

### Board A — Identity / Scale / Palette

Include the title, top info, 6-8 swatches, dominant four-view turnaround, measurement guides, two silhouettes, neutral baseline, and four wardrobe/accessory details. Use the exact same identity lock.

### Board B — Performance / Face / Hands / Prop

Include the eight expressions, five micro-expressions, five head angles, three posture variants, one cinematic close-up, five hand gestures, and one optional isolated prop. Repeat the exact identity lock, style, palette, and asymmetric-feature orientation from Board A.

Never invent a redesigned costume or face for Board B. Use Board A as the visual reference input when generating Board B.

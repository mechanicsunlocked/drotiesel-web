# drotiesel-web

Website of Drotiesel Wheelworks, wheel repair and wheelbuilding in Luxembourg.

## Preview

```bash
python3 -m http.server 8000
```

Then open http://localhost:8000.

## Publish

Push to `main`. GitHub Pages serves the repository root.

## Files

- `index.html`, `legal.html`: the pages
- `assets/site.css`, `assets/site.js`: styles and the light/dark switch
- `assets/fonts/`: Archivo and IBM Plex (SIL Open Font License), served from this site
- `assets/img/`: the Drotiesel donkey, icons and the link preview image

Text marked with `class="todo"` must be filled in before the domain goes live.

## Brand logos

Put the official logo files (from each brand's dealer or press kit, with their permission) in
`assets/partners/` as `hope.svg`, `dt-swiss.svg`, `sapim.svg`, `park-tool.svg`,
`abbey-bike-tools.svg`, `wheel-fanatyk.svg`. Until then the section shows the names as text.

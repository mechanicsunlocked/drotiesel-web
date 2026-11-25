"""Build .preview/ for the claude.ai artifact viewer: CSS and JS inlined, page without the html/head/body wrapper."""
import re
css=open('assets/site.css').read().replace('url(fonts/','url(assets/fonts/')
js=open('assets/site.js').read()
h=open('index.html').read()
body=re.search(r'<body>(.*)</body>',h,flags=re.S).group(1).replace('<script src="assets/site.js" defer></script>','<script>'+js+'</script>')
open('.preview/index.html','w').write('<title>Drotiesel Website Preview</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n<style>\n'+css+'\n</style>\n'+body)
l=open('legal.html').read().replace('<link rel="stylesheet" href="assets/site.css">','<style>\n'+css+'\n</style>').replace('<script src="assets/site.js" defer></script>','<script>'+js+'</script>')
open('.preview/legal.html','w').write(l)

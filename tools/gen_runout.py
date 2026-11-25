"""Scroll scene for the website: lower part of a 29" wheel in the truing stand, to scale in mm
(1 unit = 1 mm, axle at 0,0). Rim outer r 316, inner r 291 (25 deep), ERD 600, 32 spokes 3-cross,
Ø52 hub flange, 12 mm nipples, two rim decals. Dial indicator under the rim measures radial runout
from below: flat tip Ø12, spindle Ø4.8, stem Ø8 in a holder, dial Ø57 with 100 divisions, zero at 12.
site.js turns #rw-wheel with the scroll position and turns #rw-needle by reading * 3.6 deg.
Writes the SVG between the markers in index.html."""
import math,re
F=lambda v:f"{v:.2f}"
def P(r,a,cx=0,cy=0):
    t=math.radians(a-90); return cx+r*math.cos(t), cy+r*math.sin(t)
R_OUT,R_IN,R_ERD,R_HUB,N=316,291,300,26,32
CUT=R_OUT/3            # show the wheel below this line (lower third of its height)
o=[]
o.append('<defs><clipPath id="rw-clip"><rect x="-330" y="%s" width="660" height="400"/></clipPath>'%F(CUT))
# decal text path on the rim centre line
o.append('<path id="rw-decal" d="M %s 0 A 303.5 303.5 0 1 1 %s 0 A 303.5 303.5 0 1 1 %s 0" fill="none"/></defs>'%(F(-303.5),F(303.5),F(-303.5)))
o.append('<g clip-path="url(#rw-clip)"><g id="rw-wheel">')
sp=[];nip=[]
off=720*3/N
def at_r(h,e,r):
    (hx,hy),(ex,ey)=h,e; dx,dy=ex-hx,ey-hy; a=dx*dx+dy*dy; b=2*(hx*dx+hy*dy); c=hx*hx+hy*hy-r*r
    t=(-b+math.sqrt(b*b-4*a*c))/(2*a); return hx+t*dx,hy+t*dy
for i in range(N):
    a=i*360/N+360/N/2; j=i//2; s=1 if j%2==0 else -1
    if i%2: s=-s
    h=P(R_HUB,a+s*off); e=P(R_ERD,a)
    n0=at_r(h,e,R_IN-11); n1=at_r(h,e,R_IN)
    sp.append(f"M{F(h[0])} {F(h[1])}L{F(n0[0])} {F(n0[1])}"); nip.append(f"M{F(n0[0])} {F(n0[1])}L{F(n1[0])} {F(n1[1])}")
o.append(f'<path d="{"".join(sp)}" stroke="currentColor" stroke-width="2.2" fill="none"/>')
o.append(f'<path d="{"".join(nip)}" stroke="#C8962E" stroke-width="4" fill="none"/>')
o.append(f'<path d="M{R_OUT} 0A{R_OUT} {R_OUT} 0 1 1 {-R_OUT} 0A{R_OUT} {R_OUT} 0 1 1 {R_OUT} 0ZM{R_IN} 0A{R_IN} {R_IN} 0 1 0 {-R_IN} 0A{R_IN} {R_IN} 0 1 0 {R_IN} 0Z" fill="currentColor" fill-rule="evenodd"/>')
o.append('<circle r="311" fill="none" stroke="var(--bg)" stroke-width="1.2"/>')
# two decals, opposite each other (knocked out of the rim)
for start in ("12%","62%"):
    o.append(f'<text font-family="Archivo, Arial Black, sans-serif" font-weight="800" font-stretch="125%" font-size="11" letter-spacing="2.2" fill="var(--bg)" dominant-baseline="central"><textPath href="#rw-decal" startOffset="{start}">DROTIESEL · WHEELWORKS</textPath></text>')
o.append('</g></g>')
# ---- dial indicator under the rim ----
x0=0; y=R_OUT+0.6
o.append('<g id="rw-gauge">')
o.append(f'<rect x="-6" y="{F(y)}" width="12" height="2" rx="0.4" fill="currentColor"/>'); y+=2
o.append(f'<rect x="-2.4" y="{F(y-0.3)}" width="4.8" height="10.6" fill="currentColor"/>'); y+=10
o.append(f'<rect x="-4" y="{F(y)}" width="8" height="22" fill="currentColor"/>')
cy0=y+4; o.append(f'<rect x="-9" y="{F(cy0)}" width="18" height="11" rx="1" fill="currentColor"/><rect x="8.5" y="{F(cy0+2)}" width="16" height="7" fill="currentColor"/>')
y+=22
rb=28.5; ring=3.2; r=rb-ring/2; DY=y+rb
o.append(f'<circle cx="0" cy="{F(DY)}" r="{F(r)}" fill="var(--bg)" stroke="currentColor" stroke-width="{ring}"/>')
lines={1:[],5:[],10:[]}
for i in range(100):
    k=10 if i%10==0 else (5 if i%5==0 else 1); L={10:4.8,5:3.4,1:2.0}[k]; r0=r-ring/2-0.6
    p=P(r0,3.6*i,0,DY); q=P(r0-L,3.6*i,0,DY); lines[k].append(f"M{F(p[0])} {F(p[1])}L{F(q[0])} {F(q[1])}")
for k,w in ((1,0.4),(5,0.65),(10,1.0)):
    o.append(f'<path d="{"".join(lines[k])}" stroke="currentColor" stroke-width="{w}" fill="none"/>')
# tolerance marks at -15 and +15 (brass)
for d in (-15,15):
    p=P(r-ring/2-0.6,3.6*d,0,DY); q=P(r-ring/2-7.5,3.6*d,0,DY)
    o.append(f'<path d="M{F(p[0])} {F(p[1])}L{F(q[0])} {F(q[1])}" stroke="#C8962E" stroke-width="1.4"/>')
p=P(r-ring/2-5,0,0,DY); q=P(5,180,0,DY)
o.append(f'<g id="rw-needle" data-cx="0" data-cy="{F(DY)}"><path d="M{F(q[0])} {F(q[1])}L{F(p[0])} {F(p[1])}" stroke="#C8962E" stroke-width="1.7" stroke-linecap="round"/></g>')
o.append(f'<circle cx="0" cy="{F(DY)}" r="3" fill="currentColor"/>')
o.append('</g>')
bottom=DY+rb
x_half=math.sqrt(R_OUT**2-CUT**2)
vb=f"{F(-x_half-4)} {F(CUT-2)} {F(2*x_half+8)} {F(bottom-CUT+6)}"
svg=(f'<svg class="runout" viewBox="{vb}" role="img" aria-label="A wheel turns in the truing stand; a dial indicator under the rim reads its radial runout">'
     + "\n".join(o) + '</svg>')
h=open('index.html').read()
h=re.sub(r'<!-- runout:start -->.*?<!-- runout:end -->', lambda m:'<!-- runout:start -->'+svg+'<!-- runout:end -->', h, flags=re.S)
open('index.html','w').write(h)
print("viewBox",vb)

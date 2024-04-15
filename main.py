import vpython as vp
vp.scene.caption = """To rotate "camera", drag with right button or Ctrl-drag.
To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
  On a two-button mouse, middle is left + right.
To pan left/right and up/down, Shift-drag.
Touch screen: pinch/extend to zoom, swipe or two-finger rotate."""
vp.scene.forward = vp.vector(0,-.3,-1)

G = 6.7e-11 # Newton gravitational constant

giant = vp.sphere(pos=vp.vector(-1e11,0,0), radius=2e10, color=vp.color.red, 
                make_trail=True, trail_type='points', interval=10, retain=50)
giant.mass = 2e30
giant.p = vp.vector(0, 0, -1e4) * giant.mass

dwarf = vp.sphere(pos=vp.vector(1.5e11,0,0), radius=1e10, color=vp.color.yellow,
                make_trail=True, interval=10, retain=50)
dwarf.mass = 1e30
dwarf.p = -giant.p

dt = 1e5
while True:
    vp.rate(200)
    r = dwarf.pos - giant.pos
    F = G * giant.mass * dwarf.mass * r.hat / vp.mag(r)**2
    giant.p = giant.p + F*dt
    dwarf.p = dwarf.p - F*dt
    giant.pos = giant.pos + (giant.p/giant.mass) * dt
    dwarf.pos = dwarf.pos + (dwarf.p/dwarf.mass) * dt

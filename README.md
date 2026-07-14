# Bezel-Project-TV-Remover
Remove the ugly static TV from Bezel Project bezels so that you can enjoy the art, but also enjoy the nice shader effects of reflective TV frames which are available in MegaBezel or KokoAIO.

# What Does This Do
It calculates the volume of non-transparent pixels in a PNG image, and according to a very arbitrary range-picking ("it felt right!") determines roughly the aspect ratio of the transparent viewport:
* 3:4 (Standard CRT)
* 4:3 (vertical games, like PacMan and 1941)
* 2x3:4 (for games that have two side by side screens)
* 3x3:4 (for games that have three side by side screens)
* Abnormal - for games like After Burner 2, which is an arbitrary shape

For 3:4 and 4:3 - draw a transparent rectangle that deletes the ugly static TV frame. That way, when using MegaBezel with MAME and a viewport zoom of 115.00, you will have nice art sidebars, while still having a reflective CRT frame. Honestly? Looks great.

I didn't bother with anything but 3:4 and 4:3, but I'm sure it's just about finding the coordinates for the transparent rectangle you want to draw.

In my home arcade Batocera build I applied this to Bezel Project bezels for:
* MAME
* FBNeo
* NeoGeo
* Atomiswave
All look great so far.

# Caveats
I didn't go over all bezels to see if they all look perfect. I skimmed through a couple of hundred and they looked fine.
Take this as-is. Fix it, use it elsewhere, I don't care.

No AI was used in writing this code. I really wanted Opus 4.8 to do it for me but it shat the bed and ate all my tokens before I started from scratch.

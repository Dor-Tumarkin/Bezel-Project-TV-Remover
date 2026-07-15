# Bezel Project TV Frame  Remover
Remove the ugly static TV from Bezel Project bezels so that you can enjoy the art, but also enjoy the nice shader effects of reflective TV frames which are available in MegaBezel or KokoAIO.

See ga2_original.png with the TV frame vs. ga2.png.

Follow the guide below to achieve the results in ga2_photo.jpg with Bezel Project and MegaBezels on Batocera (tested on v43)

## What Does This Do
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
* Naomi

All look great so far.

## Caveats
I didn't go over all bezels to see if they all look perfect. I skimmed through a couple of hundred and they looked fine.
Take this as-is. Fix it, use it elsewhere, I don't care.

No AI was used in writing this code. I really wanted Opus 4.8 to do it for me but it shat the bed and ate all my tokens doing a terrible job, before I wrote this from scratch. 

## How to Use, For Real
1. Batocera v43
2. Get Mega Bezel from Content Store
3. Get Bezel Project from Content Store and metadata from Screenscraper
4. Recommended - create a base folder and copy your decorations to an external PC before running script, because changes are in-place and if you don't like the outcome you can roll it back without scraping gigabytes of art again
5. Place script in base folder and run (requires pip install pillow) - don't forget to modify `folder_paths` to suit your needs
6. Run script
7. Copy back into Batocera
8. Set Viewport Zoom in Shader Parameters to 115.0 to enjoy a full screen experience. For example, if you use the regular MegaBezel shader in Batocera, this can be done by adding the line `HSM_VIEWPORT_ZOOM = 115` to /usr/share/batocera/shaders/bezel/Mega_Bezel/Presets/BATOCERA__MBZ.slangp
9. Use the following settings: SHADER EST: MEGA-BEZEL, DECORATION SET: thebezelproject, GAME ASPECT RATIO: AUTO and ALLOW ROTATION: OFF (this is because Mega Bezel already rotates vertical games, so enabling it here causes it to get rotated twice and end up on its side)

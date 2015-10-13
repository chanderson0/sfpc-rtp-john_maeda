# Recreating the Past - John Maeda's _10 Morisawa Posters_

![ca-morisawa_8-animated](https://38.media.tumblr.com/0a8b2a94a072d6b202651ff601485bfe/tumblr_nw6bumsqyU1ui4qufo1_r1_400.gif)

_Morisawa 8, Animated_ ([see original](https://500px.com/photo/4813904/morisawa-8-by-john-maeda))

**_With upfront apologies for any spaghetti code! (especially the animation code, jeez)_**

### Requirements

- Ghostscript
- ImageMagick (for animation)
- Python 3 (for animation)

### Environment for development

1. `brew install entr`
2. Install [Skim](http://skim-app.sourceforge.net/)
3. Check "Check for file changes" in Skim -> Sync Preferences
4. `defaults write -app Skim SKAutoReloadFileUpdate -boolean true` so it doesn't bother you all the time
5. `ls *.ps | entr ps2pdf -sPAPERSIZE=a3 -dOptimize=true /_ output.pdf`
6. Keep Skim open on output.pdf for preview, and you can live edit any PS file in the working dir.

### Export

`convert -density 300 -background white -alpha remove -resize 1413x2000 -quality 80 output.pdf FILENAME.jpg`

### Animation

#### Generate

1. `python generate_morisawa.py`
2. `mkdir out_img`
3. `gs -r300 -dDownScaleFactor=6 -sDEVICE=pnggray -sOutputFile=out_img/out-%d.png -dBATCH -dNOPAUSE -sPAPERSIZE=a3 out_ps/*.ps`
4. Sometimes Ghostscript outputs bad frames, so go into `./out_img` and delete them. (brownie points if you figure out why!)
5. `convert out_img/*.png -reverse out_img/*.png -set delay 5 -loop 0 -filter LanczosRadius -distort Resize 60% animation.gif`

#### Edit

1. Edit the `morisawa_fun.ps.tpl` file, putting in `!!REPLACEMENT!!` strings where appropriate.
2. Edit `generate_morisawa.py` to replace the above strings as desired.
3. Probably clear the `./out_ps` directory

# Recreating the Past - John Maeda's _10 Morisawa Posters_

### Environment for development

1. `brew install entr`
2. Install [Skim](http://skim-app.sourceforge.net/)
3. Check "Check for file changes" in Skim -> Sync Preferences
4. `defaults write -app Skim SKAutoReloadFileUpdate -boolean true` so it doesn't bother you all the time
5. `ls *.ps | entr ps2pdf -sPAPERSIZE=a3 -dOptimize=true /_ output.pdf`
6. Keep Skim open on output.pdf for preview, and you can live edit any PS file in the working dir.

### Export

`convert -density 300 -background white -alpha remove -resize 1413x2000 -quality 80 output.pdf FILENAME.jpg`

# Recreating the Past - John Maeda's _10 Morisawa Posters_

![ca-morisawa_8-thumb](https://cloud.githubusercontent.com/assets/73099/10464187/7885d8d8-71b6-11e5-9a8b-3f03647733a2.jpg)

_Morisawa 8, Recreated_ ([see original](https://500px.com/photo/4813904/morisawa-8-by-john-maeda))

### Environment for development

1. `brew install entr`
2. Install [Skim](http://skim-app.sourceforge.net/)
3. Check "Check for file changes" in Skim -> Sync Preferences
4. `defaults write -app Skim SKAutoReloadFileUpdate -boolean true` so it doesn't bother you all the time
5. `ls *.ps | entr ps2pdf -sPAPERSIZE=a3 -dOptimize=true /_ output.pdf`
6. Keep Skim open on output.pdf for preview, and you can live edit any PS file in the working dir.

### Export

`convert -density 300 -background white -alpha remove -resize 1413x2000 -quality 80 output.pdf FILENAME.jpg`

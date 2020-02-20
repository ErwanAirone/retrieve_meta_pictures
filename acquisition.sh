idscene=0
libomx=omx
librasp=rasp
ext=.jpg
extdata=.xml
./jpeg
mv still-default-2592x1944.jpg "$idscene$libomx$ext"
sleep 1
raspistill -w 2592 -h 1944 -o "$idscene$librasp$ext"
echo "<TEST$idscene>" >> "$idscene$extdata"
echo "<Omxcam>" >> "$idscene$extdata"
echo -n "Exposure_Time=" >> "$idscene$extdata"
exif "$idscene$libomx$ext" | grep "Exposure Time" | cut -d"|" -f2 | cut -d" " -f1 >> "$idscene$extdata"
echo -n " Brightness=" >> "$idscene$extdata"
exif "$idscene$libomx$ext" | grep "Brightness"  | cut -d"|" -f2 | cut -d" " -f1 >> "$idscene$extdata"
echo -n " Shutter_Speed=" >> "$idscene$extdata"
exif "$idscene$libomx$ext" | grep "Shutter Speed"  | cut -d"|" -f2 | cut -d" " -f1 >> "$idscene$extdata"
echo -n " ISO=" >> "$idscene$extdata"
exif "$idscene$libomx$ext" | grep "ISO"  | cut -d"|" -f2 | cut -d" " -f1 >> "$idscene$extdata"
echo "<Omxcam\>" >> "$idscene$extdata"

echo "<Raspicam>" >> "$idscene$extdata"
echo -n "Exposure_Time=" >> "$idscene$extdata"
exif "$idscene$librasp$ext" | grep  "Exposure Time" | cut -d"|" -f2 | cut -d" " -f1 >> "$idscene$extdata"
echo -n " Brightness=" >> "$idscene$extdata"
exif "$idscene$librasp$ext" | grep "Brightness" | cut -d"|" -f2 | cut -d" " -f1 >> "$idscene$extdata"
echo -n " Shutter_Speed=" >> "$idscene$extdata"
exif "$idscene$librasp$ext" | grep "Shutter Speed" | cut -d"|" -f2 | cut -d" " -f1 >> "$idscene$extdata"
echo -n " ISO=" >> "$idscene$extdata"
exif "$idscene$librasp$ext" | grep "ISO" | cut -d"|" -f2 | cut -d" " -f1 >> "$idscene$extdata"
echo "<Raspicam\>" >> "$idscene$extdata"

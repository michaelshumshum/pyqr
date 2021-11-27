# pyqr
simple python script to make encode data into QR codes

## what
it uses google's chart api to make encode qr codes from pretty much any source data. supports some encoding schemes.

usage:
```
python3 qrcode.py -data <data> -directory <directory> [-optional]

required:
-data: data to encode.
-directory: directory to save qrcode image to.

optional:
-dimensions: custom dimensions of image. default is 200x200.
-encoding: custom encoding (UTF-8, Shift_JIS, ISO-8859-1). default is UTF-8.
-filename: custom image filename. default is "qr.png"
```

## requirements

`pip3 install requests`

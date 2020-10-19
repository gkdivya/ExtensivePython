## Modules

Below modules are created for
1. Converting a jpg/jpeg to png image (using PIL library) j2p
2. Converting a png to jpg image (using PIL library) p2j
3. Image resizer that can resize bulk images with these features:
    a. Resize by user determined percentage (say 50% for height and width) (proportional) res_p
    b. Resize by user determined width (proportional) res_w
    c. Resize by user determined height (proportional) res_h
4. Image cropper that can crop bulk images with these features:
    a. Center square/rectangle crop by user-determined pixels crp_px
    b. Centre square/rectangle crop by user-determined percentage (crop to 50%/70%) crp_p
In addition to this, it let the user know which all images were not cropped due to size mismatches

Main module is created as an zipped app, that exposes all of these features using argparse

## Testing:
Each module is tested independently from command line

Each feature is available via argument selection

## Test cases:
a. download 20 jpeg images of size more than 1000x1000
b. convert to png
c. convert to jpg
d. resize to 80%
e. resize to 500 width
f. resize to 500 height
g. Using the zipped app, center crop to 224x224

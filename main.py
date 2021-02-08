from PIL import Image, ImageStat, ImageEnhance, ImageFilter
from blend_modes import *
import numpy

def smart_darken(img_obj):
    # get avg pixel brightness
    brightness = ImageStat.Stat( img_obj.convert('L') ).mean[0]
    # only darken if brightness is above 50% grey
    if brightness > 128:
        # darken
        brightness_enhancer = ImageEnhance.Brightness(img_obj)
        factor = 0.5
        img_obj = brightness_enhancer.enhance(factor)
        # add contrast
        contrast_enhancer = ImageEnhance.Contrast(img_obj)
        factor = 1.5
        img_obj = contrast_enhancer.enhance(factor)
    return img_obj

def soft_glow(img_obj):
    light_blurred = img_obj.filter(ImageFilter.GaussianBlur(100))
    top_layer = numpy.array(light_blurred).astype(float)
    bottom_layer = numpy.array(img_obj).astype(float)
    return Image.fromarray( numpy.uint8( lighten_only(bottom_layer, top_layer, 0.25) ) )

if __name__ == "__main__":
    input_image = Image.open("input.jpg").convert("RGBA")
    input_image = smart_darken(input_image)
    input_image = soft_glow(input_image)
    input_image.show()
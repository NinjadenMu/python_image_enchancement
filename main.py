from PIL import Image, ImageStat, ImageEnhance, ImageFilter, ImageColor
from blend_modes import *
import numpy

def smart_darken(img_obj):
    # get avg pixel brightness
    brightness = ImageStat.Stat( img_obj.convert('L') ).mean[0]
    # only darken if brightness is above 50% grey
    if brightness > 128:
        # darken
        brightness_enhancer = ImageEnhance.Brightness(img_obj)
        factor = 0.69
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

def color_grade(img_obj):
    # create colored overlay to put on top of image
    blue_overlay = layer = Image.new("RGBA", img_obj.size, "#0071b2")
    top_layer = numpy.array(blue_overlay).astype(float)
    bottom_layer = numpy.array(img_obj).astype(float)
    return Image.fromarray( numpy.uint8( overlay(bottom_layer, top_layer, 0.25) ) )

# the main script
def get_output_img(imgobj):
    imgobj = imgobj.convert("RGBA")
    imgobj = smart_darken(imgobj)
    imgobj = color_grade(imgobj)
    #imgobj = soft_glow(imgobj)
    return imgobj

if __name__ == "__main__":
    input_image = Image.open("input.jpg")
    output_image = get_output_img(input_image)
    output_image.show()
    output_image.save("output.png")
from PIL import Image, ImageStat, ImageEnhance, ImageFilter, ImageColor
from blend_modes import *
import numpy

def smart_darken(img_obj):
    # get avg pixel brightness
    brightness = ImageStat.Stat( img_obj.convert('L') ).mean[0]
    # darken based on current brightness
    if brightness > 192:
        # darken
        brightness_enhancer = ImageEnhance.Brightness(img_obj)
        factor = 0.6
        img_obj = brightness_enhancer.enhance(factor)
        # add contrast
        contrast_enhancer = ImageEnhance.Contrast(img_obj)
        factor = 1.75
        img_obj = contrast_enhancer.enhance(factor)
    elif brightness > 128:
        # darken
        brightness_enhancer = ImageEnhance.Brightness(img_obj)
        factor = 0.69
        img_obj = brightness_enhancer.enhance(factor)
        # add contrast
        contrast_enhancer = ImageEnhance.Contrast(img_obj)
        factor = 1.5
        img_obj = contrast_enhancer.enhance(factor)
    elif brightness > 64:
        # darken
        brightness_enhancer = ImageEnhance.Brightness(img_obj)
        factor = 0.8
        img_obj = brightness_enhancer.enhance(factor)
        # add contrast
        contrast_enhancer = ImageEnhance.Contrast(img_obj)
        factor = 1.25
        img_obj = contrast_enhancer.enhance(factor)
    return img_obj

def soft_glow(img_obj):
    light_blurred = img_obj.filter(ImageFilter.GaussianBlur(100))
    top_layer = numpy.array(light_blurred).astype(float)
    bottom_layer = numpy.array(img_obj).astype(float)
    return Image.fromarray( numpy.uint8( lighten_only(bottom_layer, top_layer, 0.25) ) )

def color_grade(img_obj):
    # create colored overlay to put on top of image
    blue_overlay = layer = Image.new("RGBA", img_obj.size, "#3a6981")
    top_layer = numpy.array(blue_overlay).astype(float)
    bottom_layer = numpy.array(img_obj).astype(float)
    return Image.fromarray( numpy.uint8( soft_light(bottom_layer, top_layer, 0.69) ) )

# the main script
def get_output_img(img_obj):
    img_obj = img_obj.convert("RGBA")
    img_obj = smart_darken(img_obj)
    img_obj = color_grade(img_obj)
    #img_obj = soft_glow(img_obj)
    return img_obj

if __name__ == "__main__":
    input_image = Image.open("input.jpg")
    output_image = get_output_img(input_image)
    output_image.show()
    output_image.save("output.png")
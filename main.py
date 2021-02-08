from PIL import Image, ImageStat, ImageEnhance

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

if __name__ == "__main__":
    input_image = Image.open("input.jpg")
    input_image = smart_darken(input_image)
    input_image.show()
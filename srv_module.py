import glob
from PIL import Image


def resize_loop(directory, width, height):
    for infile in glob.glob(f"{directory}*.jpg"):
        try:
            resize_image(infile, width, height)
        except Exception as e:
            print(e)
       


def resize_image(ImageFilePath, width, height):
    '''
    Resize PIL image keeping ratio and using white background.
    '''
    image_pil = Image.open(ImageFilePath, 'r')
    ratio_w = width / image_pil.width
    ratio_h = height / image_pil.height
    if ratio_w < ratio_h:
        # It must be fixed by width
        resize_width = width
        resize_height = round(ratio_w * image_pil.height)
    else:
        # Fixed by height
        resize_width = round(ratio_h * image_pil.width)
        resize_height = height
    image_resize = image_pil.resize((resize_width, resize_height), Image.Resampling.LANCZOS)
    background = Image.new('RGBA', (width, height), (0, 0, 0, 255))
    offset = (round((width - resize_width) / 2), round((height - resize_height) / 2))
    background.paste(image_resize, offset)
    background.save(f'{ImageFilePath[:-4]}_resized.png')
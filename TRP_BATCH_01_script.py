import os
from PIL import Image
from PIL.ExifTags import TAGS

# print(os.path.normpath(os.getcwd()))
parent_folder = os.path.dirname(os.getcwd())
for root, dirs, files in os.walk(parent_folder):
    if not files:
        continue
    # prefix = os.path.basename(root)
    for f in files:
        #imagename = f
        print(os.path.abspath(f))

        # read the image data using PIL
        image = Image.open(f)

        # extract EXIF data
        exifdata = image.getexif()

        # iterating over all EXIF data fields
        for tag_id in exifdata:
            # get the tag name, instead of human unreadable tag id
            tag = TAGS.get(tag_id, tag_id)
            data = exifdata.get(tag_id)
            # decode bytes
            if isinstance(data, bytes):
                data = data.decode()
            print(f"{tag:25}: {data}")
        # os.rename(os.path.join(root, f), os.path.join(root, "{}_{}".format(prefix, f)))

# path to the image or video F:\TRP

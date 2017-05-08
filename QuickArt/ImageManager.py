from imager2 import Imager
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFilter


__author__ = "Martin Langmo Karlstrøm"
__project__ = "QuickArt"


class TheArtist:

    def __init__(self):
        self.n = int(input('One or two img?\n>> '))
        while self.n not in (1, 2):
            self.n = int(input('I said ONE or TWO img?!\n>> '))
        fid1 = input('Paste img1 path:\n>> ')
        self.img1_er = Imager(fid1)
        self.img1 = Image.open(fid1)
        if self.n == 2:
            fid2 = input('Paste img2 file path:\n>> ')
            self.img2_er = Imager(fid2)
            self.img2 = Image.open(fid2)

    def resize(self, newxsize=250, newysize=250):
        self.img1_er = self.img1_er.resize(newxsize, newysize)
        if self.n == 2:
            self.img2_er = self.img2_er.resize(newxsize, newysize)

    def scale_colors(self):
        imer = self.img1_er.scale_colors()
        imer.display()

    def wta(self):
        imer = self.img1_er.map_color_wta()
        imer.display()

    def greyscale(self):
        imer = self.img1_er.gen_grayscale()
        imer.display()

    def tunnel(self):
        imer = self.img1_er.tunnel()
        imer.display()

    def morph_roll(self):
        self.resize()
        imer = self.img1_er.morphroll(self.img2_er)
        imer.display()

    def emboss(self):
        im = self.img1.filter(ImageFilter.EMBOSS)
        im.show()

    def blur(self):
        im = self.img1.filter(ImageFilter.BLUR)
        im.show()

    def contrast(self, factor=100):
        enh = ImageEnhance.Contrast(self.img1)
        enh.enhance(factor).show()


def main():
    a = TheArtist()
    a.emboss()


if __name__ == '__main__':
    main()

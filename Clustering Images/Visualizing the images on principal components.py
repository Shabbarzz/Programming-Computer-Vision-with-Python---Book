from PIL import Image, ImageDraw
# height and width
h,w = 1200,1200
# create a new image with a white background
img = Image.new(’RGB’,(w,h),(255,255,255))
draw = ImageDraw.Draw(img)
# draw axis
draw.line((0,h/2,w,h/2),fill=(255,0,0))
draw.line((w/2,0,w/2,h),fill=(255,0,0))
# scale coordinates to fit
scale = abs(projected).max(0)
scaled = floor(array([ (p / scale) * (w/2-20,h/2-20) +
(w/2,h/2) for p in projected]))
# paste thumbnail of each image
for i in range(imnbr):
    nodeim = Image.open(imlist[i])
    nodeim.thumbnail((25,25))
    ns = nodeim.size
    img.paste(nodeim,(scaled[i][0]-ns[0]//2,scaled[i][1]-
    ns[1]//2,scaled[i][0]+ns[0]//2+1,scaled[i][1]+ns[1]//2+1))
img.save(’pca_font.jpg’)

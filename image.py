from PIL import Image, ImageDraw, ImageFont, ImageFilter

im = Image.open('5.png')
# 转换图片的模式为RGBA
image = im.convert('RGB')
# 获得文字图片的每个像素点
src_strlist = image.load()
# # 100,100 是像素点的坐标
# data = src_strlist[100, 100]


#选色器
def pickColor(p,q):
    return src_strlist[p,q]

image1 = Image.open('1.png')
width, height = image1.size
# 创建Draw对象:
draw = ImageDraw.Draw(image1)

i=1
for x in range(int(width/9)):
    for y in range(int(height/9)):
        draw.point((x*9+4, y*9+4), fill=pickColor(x*7,y*7))
        i=i+1
print(i)
image1.save('code.png', 'png')
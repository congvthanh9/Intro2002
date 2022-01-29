import cv2
import ascii_magic
import imgkit
import os
os.mkdir("images")
os.mkdir("ascii")
os.mkdir("html")
vidObj = cv2.VideoCapture("newproject.mp4")
count = 0
flag = 1
while flag:
    flag, image = vidObj.read()
    try:
        cv2.imwrite("images/frame%d.jpg"%count, image)
    except:
        break
    count+=1

for i in range(count):
    s = "images/frame"+str(i)+".jpg"
    output = ascii_magic.from_image_file(
        s,
        columns = 250,
        width_ratio = 2,
        mode = ascii_magic.Modes.HTML,
    )
    ascii_magic.to_html_file("html/frame"+str(i)+".html", output, additional_styles='background: #222;')
path = r'C:\Program Files\wkhtmltox\bin\wkhtmltoimage.exe'
config = imgkit.config(wkhtmltoimage=path)
for i in range(count):
    imgkit.from_file('html/frame'+str(i)+'.html', 'ascii/frame'+str(i)+'.jpg', config=config)

frame= cv2.imread("ascii/frame0.jpg")
ih, iw, il = frame.shape
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter("asciiVideo.mp4", fourcc, 30.00, (iw, ih))
for i in range(count):
    image="ascii/frame"+str(i)+".jpg"
    video.write(cv2.imread(image))
cv2.destroyAllWindows()
video.release()


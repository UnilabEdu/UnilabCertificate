from PIL import Image, ImageDraw, ImageFont


def certificate_text(subject, course_type):
    cert_text = f"მასზეთ რომ გაიარე  {subject} ის {course_type}\n ილიაუნის კიბერლაბორატორიაში\n ამიტომ იმიტომ"
    return cert_text

def certificate_2d(username,type,subject,date):
    image = Image.open('images/Certificate_blank.png')

    draw = ImageDraw.Draw(image)

    font_path = "alk-sanet.ttf"

    font = ImageFont.truetype(font_path, 25)

    sign = Image.open("images/xelmowera.jpg")
    sign = sign.resize((200, 70))

    sign2 = Image.open("images/xelmowera.jpg")
    sign2 = sign.resize((200, 70))



    draw.text((580, 540), certificate_text(type, subject), fill=(0, 0, 0), font=font)

    draw.text((800, 380), username, fill=(0, 0, 0), font=font)
    #
    draw.text((800, 655), date, fill=(0, 0, 0), font=font)
    #
    image.paste(sign, (930, 710))
    image.paste(sign, (930, 790))


    image.save(f"certificate_images/{str(username)}_certificate.jpg")


certificate_2d("test","test","test","test")


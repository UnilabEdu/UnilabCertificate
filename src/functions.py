from PIL import Image, ImageDraw, ImageFont


def certificate_text(subject, course_type):
    cert_text = f"მასზეთ რომ გაიარე  {subject} ის {course_type}\n ილიაუნის კიბერლაბორატორიაში\n ამიტომ იმიტომ"
    return cert_text


def certificate_2d(username, course_type, subject, date):
    image = Image.open('src/images/Certificate_blank.png')

    draw = ImageDraw.Draw(image)

    font_path = "src/alk-sanet.ttf"

    font = ImageFont.truetype(font_path, 25)

    sign = Image.open("src/images/xelmowera.jpg")
    sign = sign.resize((200, 70))

    sign2 = Image.open("src/images/xelmowera.jpg")
    sign2 = sign.resize((200, 70))

    draw.text((580, 540), certificate_text(course_type, subject), fill=(0, 0, 0), font=font)

    draw.text((800, 380), username, fill=(0, 0, 0), font=font)
    #
    draw.text((800, 655), date, fill=(0, 0, 0), font=font)
    #
    image.paste(sign, (930, 710))
    image.paste(sign, (930, 790))

    image.save(f"src/created_certificates_img/{str(username)}_certificate.jpg")



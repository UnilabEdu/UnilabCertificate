from PIL import Image, ImageDraw, ImageFont


def certificate_text(subject, course_type):
    cert_text = f"მასზეთ რომ გაიარa კურსი  {subject} ის\n {course_type} ილიაუნის კიბერლაბორატორიაში\n ამიტომ იმიტომ"
    return cert_text


def certificate_2d(username, course_type, subject, date,signature_path):
    image = Image.open('src/assets/images/Certificate_blank.png')

    draw = ImageDraw.Draw(image)

    font_path = "src/assets/fonts/alk-sanet.ttf"

    font = ImageFont.truetype(font_path, 25)

    sign = Image.open(signature_path)
    sign = sign.resize((200, 70))

    sign2 = Image.open(signature_path)
    sign2 = sign.resize((200, 70))

    draw.text((585, 540), certificate_text(course_type, subject), fill=(0, 0, 0), font=font)

    draw.text((800, 380), username, fill=(0, 0, 0), font=font)
    #
    draw.text((750, 647), date, fill=(0, 0, 0), font=font)
    #
    image.paste(sign, (930, 710))
    image.paste(sign, (930, 790))

    image.save(f"src/assets/images/created_certificates_img/{str(username)}_certificate.jpg")



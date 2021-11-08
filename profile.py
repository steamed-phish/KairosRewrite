from PIL import Image, ImageFont, ImageDraw
# Load a OpenFont format font from a local directory as an ImageFont object
# In this case, a TrueType font using the truetype method.
font = ImageFont.truetype(font='VT323-Regular.ttf', size=81)
# Create a new image onto which the text will be added

def make_profile(user):
  im = Image.open("Profile.png")
  draw = ImageDraw.Draw(im)
  draw.text(xy=(300, 290), text=str(user["money"]) + " Credits", font=font, fill='white')
  draw.text(xy=(300, 435), text=str(user["bank"]) + " Credits", font=font, fill='white')
  draw.text(xy=(429, 590), text=str(user["bank"] + user["money"]) + " Credits", font=font, fill='white')
  draw.text(xy=(332, 733), text=str(user["class"]), font=font, fill='white')
  draw.text(xy=(1139, 290), text=str(user["stats"]["attack"]), font=font, fill='white')
  draw.text(xy=(1172, 433), text=str(user["stats"]["defence"]), font=font, fill='white')
  draw.text(xy=(1107, 587), text=str(user["stats"]["speed"]), font=font, fill='white')
  draw.text(xy=(1139, 737), text=str(user["stats"]["health"]), font=font, fill='white')
  im.save('profile_out.png')
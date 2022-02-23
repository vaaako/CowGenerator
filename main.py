import os, random, time, pathlib
from PIL import Image

directory = pathlib.Path(__file__).parent.resolve() # Get actual directory

def getRarity():
    rand = random.randint(1, 100)

    if(rand<=10): # 10
        return "legendary"
    if(rand<=25): # 20
        return "rare"
    else: # 70
        return "normal"
        # return "legendary"

def countFiles(folder):
    return len(os.listdir(folder))


def main():
    # try:

    # width, height = img.size
    # img = img.resize((width*2, height*2))

    # Background > Base > Skin > Acessory > Hat 

    # Background
    folder = f"{directory}/elements/background/{getRarity()}"
    img = Image.open(f"{folder}/{random.choice(os.listdir(folder))}") # Get random rarity and get random file from folder

    # Base
    base = Image.open(f"{directory}/bases/vacona.png")
    img.paste(base, (0, 0), base) # Paste on background

    # Skin
    folder = f"{directory}/elements/skin/{getRarity()}"
    skin = Image.open(f"{folder}/{random.choice(os.listdir(folder))}")

    img = Image.alpha_composite(img, skin) 
    # img.paste(skin, (0, 0), skin) # Se fizer desse jeito fica bugado, já que é uma imagem translucida e não totalmente transparente

    # Accessory
    folder = f"{directory}/elements/accessory/{getRarity()}"
    accessory = Image.open(f"{folder}/{random.choice(os.listdir(folder))}")

    img = Image.alpha_composite(img, accessory) # One of the accessories is translucent
    
    # Hat
    folder = f"{directory}/elements/hat/{getRarity()}"
    hat = Image.open(f"{folder}/{random.choice(os.listdir(folder))}")

    img.paste(hat, (0, 0), hat)

    # Save
    img.save(f"{directory}/generated/"+time.strftime("%Y-%m-%d")+"_"+str(time.time()).split(".")[0]+".png") # Date format and Timestamp
          
    # except IOError:
    #     pass              
                                        
if __name__ == "__main__":
    main()       
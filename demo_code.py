import dropbox
from dropbox.exceptions import AuthError, ApiError
import zipfile
from dropbox import DropboxOAuth2FlowNoRedirect

def get_client_2():
    dbx = dropbox.Dropbox(
                app_key = '9yejxp2a6q0qud6',
                app_secret = 'j36gxdlvvj8ghm6',
                oauth2_refresh_token = "RxC_s7yxq8wAAAAAAAAAATZPIMiZvxKBAb2rMt_hWQZ1RBWOc_wZMXSbjJagIX0S"
            )
    return dbx

def dropbox_download_file(dbx, dropbox_file_path, local_file_path):
  """Download a file from Dropbox to the local machine."""
  with open(local_file_path, 'wb') as f:
      metadata, result = dbx.files_download(path=dropbox_file_path)
      f.write(result.content)

dbx = get_client_2()
filename = '/lookingglass_dalle_90000.pt.zip'
files = dropbox_download_file(dbx, filename, 'data_content.zip')

import zipfile
with zipfile.ZipFile('data_content.zip', 'r') as zip_ref:
    zip_ref.extractall('model_file')

import time
from IPython.display import display, clear_output, Image
import ipywidgets as widgets
import os
from ipywidgets import Layout

import warnings
warnings.filterwarnings('ignore')

import subprocess

#subprocess.run(['wget',"https://logic-ai.ricerca.di.unimi.it:8080/demo/files?key=n5i47V8DeH9nt2&file=../../VA-design-generator/training-data.zip", '-P', 'content_zipped', '--no-check-certificate'],stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

#with zipfile.ZipFile('files?key=n5i47V8DeH9nt2&file=..%2F..%2FVA-design-generator%2Ftraining-data.zip', 'r') as zip_ref:
#    zip_ref.extractall('training_data')


ceramic_artist_desc = {'Delft': {'description': ', also known as Delft Blue is a general term now used for Dutch tin-glazed earthenware, a form of faience. Most of it is blue and white pottery, and the city of Delft in the Netherlands was the major centre of production. Delftware includes pottery objects of all descriptions such plates, vases, figurines and other ornamental forms and tiles. The start of the style was around 1600, and the most highly regarded period of production is about 1640–1740, but Delftware continues to be produced. In the 17th and 18th centuries Delftware was a major industry, exporting all over Europe.',
                                'source': 'Wikipedia', 'url':'https://en.wikipedia.org/wiki/Delft'},
                        'Lucie Rie': {'description': ' was an Austrian-born British ceramics artist. Rie’s works, usually consisting of hand-thrown pots, bottles, and bowl forms, are noteworthy for their Modernist forms and her use of bright colors.',
                                    'source': 'ArtNet', 'url':'http://www.artnet.com/artists/lucie-rie/'},
                        'Johann Kandler': {'description': ' was a German sculptor who became the most important modeller of the Meissen porcelain manufactury, and arguably of all European porcelain. Meissen pieces of all sorts were normally made with moulds, whose designs Kändler mostly created, supervising the production of the moulds, and checking the quality of the many examples cast. He was often not involved with their painting, which can vary between examples.',
                                            'source':'Wikipedia', 'url':'https://en.wikipedia.org/wiki/Johann_Joachim_K%C3%A4ndler'},
                        'Martin Hunt': {'description': ', who has died aged 75, was one of Britain’s most distinguished designers. Although Hunt designed for glass and lighting, he will be remembered for the pure form of his ceramic work, characterised by an absence of surface decoration.',
                                        'source': 'The Guardian', 'url':'https://www.theguardian.com/artanddesign/2018/jun/25/martin-hunt-obituary'},
                        'Iznik': {'description':' pottery, or Iznik ware, named after the town of İznik in western Anatolia where it was made, is a decorated ceramic that was produced from the last quarter of the 15th century until the end of the 17th century. İznik was an established centre for the production of simple earthenware pottery with an underglaze decoration when, in the last quarter of the 15th century, craftsmen in the town began to manufacture high quality pottery with a fritware body painted with cobalt blue under a colourless transparent lead glaze. The designs combined traditional Ottoman arabesque patterns with Chinese elements. The change was almost certainly a result of active intervention and patronage by the recently established Ottoman court in Istanbul who greatly valued Chinese blue-and-white porcelain.',
                                'source': 'Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Iznik_pottery'},
                        'Wedgwood': {'description': 'Wedgwood is an English fine china, porcelain and luxury accessories manufacturer that was founded on 1 May 1759[1] by the potter and entrepreneur Josiah Wedgwood and was first incorporated in 1895 as Josiah Wedgwood and Sons Ltd. Wedgwood is especially associated with the "dry-bodied" (unglazed) stoneware Jasperware in contrasting colours, and in particular that in "Wedgwood blue" and white, always much the most popular colours, though there are several others.',
                                    'source': 'Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Wedgwood'},
                        'Keith Murray': {'description': ' (5 July 1892 – 16 May 1981) was a New-Zealand-born British architect and industrial designer, known for ceramic, silver and glass designs. He is considered to be one of the most influential designers of the Art Deco / Modern age.', 
                                        'source': 'Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Keith_Murray_(ceramic_artist)'},
                        'Susie Cooper': {'description': ' was a household name in the Potteries during the 1920s through to the 1980s. She is known for bright art deco pieces and fine bone china tea sets, mixed with distinctively shaped tea and coffee pots, all decorated with beautifully crafted designs – lithograph pictures, floral patterns or clean lines.',
                                        'source': 'Potteries Auction', 'url':'https://www.potteriesauctions.com/news/susie-cooper-pottery-markings-guide'}
                        }


fashion_artist_desc = {'Barbara Brown': {'description': ' was a British designer, best known for her Op Art designs in the 60s and early 70s, although her career continued beyond that point. She began supplying Heals in 1958, and became their most high profile designer. Heals was one of the leading suppliers of quality fabrics (and still is). Decor is one of Brown’s most famous designs. Her work is characterised by bold designs, large geometric shapes – a sign of the exuberance, confidence and optimism of the decade, and the ascendency of youth',
                                'source': 'Jules Tern', 'url':'https://juliennedickey.wordpress.com/archive-2015/pattern-universe-research/4-barbara-brown-textile-designer/'},
                        'William Morris': {'description': '(24 March 1834 – 3 October 1896) was a British textile designer, poet, artist, novelist, architectural conservationist, printer, translator and socialist activist associated with the British Arts and Crafts Movement. Morris studied many examples of early woven textiles in the collections of the South Kensington Museum (later to become the V&A). Many of his designs were inspired by 16th- and 17th-century Italian silks, and Peacock and Dragon, an imposing yet popular design from 1878, used striking, medieval-style figuration.',
                                    'source': 'Victoria and Albert', 'url':'https://www.vam.ac.uk/articles/willam-morris-textiles'},
                        'Balenciaga': {'description': ' is a luxury fashion house founded in 1919 by the Spanish designer Cristóbal Balenciaga in San Sebastian, Spain and later acquired by French luxury group Kering. Balenciaga had a reputation as a couturier of uncompromising standards and was called "the master of us all" by Christian Dior. His bubble skirts and odd, feminine, yet "modernistic" silhouettes became the trademarks of the house. Balenciaga closed in 1972 and was reopened under new ownership in 1986. Owned by Kering, Balenciaga headquarters are in Paris. ',
                                            'source':'Wikipedia', 'url':'https://en.wikipedia.org/wiki/Balenciaga'},
                        'Versace': {'description': ' is an Italian luxury fashion company and trade name founded by Gianni Versace in 1978. The company produces upmarket Italian-made ready-to-wear and accessories, as well as haute couture pieces under the Atelier Versace brand.',
                                        'source': 'Wikipedia', 'url':'https://en.wikipedia.org/wiki/Versace'},
                        'Vivienne Westwood': {'description':' is an English fashion designer and businesswoman, largely responsible for bringing modern punk and new wave fashions into the mainstream.[1]Westwood came to public notice when she made clothes for Malcolm McLaren and her boutique in the Kings Road, which became known as SEX. Their ability to synthesise clothing and music shaped the 1970s UK punk scene which was dominated by McLarens band, the Sex Pistols. She viewed punk as a way of "seeing if one could put a spoke in the system".',
                                'source': 'Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Vivienne_Westwood'},
                        'Yves Saint Laurent': {'description': 'Yves Saint Lauren is a French luxury fashion house founded by Yves Saint Laurent and his partner, Pierre Bergé. Founded in 1962, today Saint Laurent markets a range of womens and mens ready-to-wear products, leather goods, shoes and jewellery. Yves Saint Laurent Beauté also has a presence in the beauty and fragrance market, although this is owned by LOréal, which holds exclusive licenses for the name. ',
                                    'source': 'Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Yves_Saint_Laurent_(brand)'},

                        'Yoruba Women': {'description': ': Adire is the name given to indigo dyed cloth produced by Yoruba women of south western Nigeria using a variety of resist dye techniques. Adire translates as tie and dye, and the earliest cloths were probably simple tied designs on locally-woven hand-spun cotton cloth much like those still produced in Mali. In the early decades of the twentieth century however, the new access to large quantities of imported shirting material made possible by the spread of European textile merchants in certain Yoruba towns, notably Abeokuta, enabled women dyers to become both artists and entrepreneurs in a booming new medium.', 
                                        'source': 'Adire African Textiles', 'url': 'https://www.adireafricantextiles.com/textiles-resources-sub-saharan-africa/some-major-west-african-textile-traditions/adire-cloth-of-the-yorubas/'},
                        }



furniture_artist_desc = {'Paul Storr': {'description': ' was an English goldsmith and silversmith working in the Neoclassical and other styles during the late eighteenth and early nineteenth centuries. His works range from simple tableware to magnificent sculptural pieces made for royalty.',
                                'source': 'Wikipedia', 'url':'https://en.wikipedia.org/wiki/Paul_Storr'},
                        'Ashbee Robert': {'description': ' (17 May 1863 – 23 May 1942) was an English architect and designer who was a prime mover of the Arts and Crafts movement, which took its craft ethic from the works of John Ruskin and its co-operative structure from the socialism of William Morris. Ashbee was defined by one source as "designer, architect, entrepreneur, and social reformer". His disciplines included metalwork, textile design, furniture, jewellery and other objects in the Modern Style (British Art Nouveau style) and Arts and Crafts genres.',
                                    'source': 'Wikipedia', 'url':'https://en.wikipedia.org/wiki/Charles_Robert_Ashbee'},
                        'Garrard Robert': {'description': ' was part of an important and long-established firm of silversmiths (R. and S. Garrard and Co.), specialising in elaborate domestic silver and fine jewellery, during the last century Garrard produced some of the finest presentation plate. R. and S. Garrard and Co. produced a wide variety of useful and highly decorative silverware, frequently displayed at the national and international exhibitions; these provide an idea of Garrards range of items as well as stylistic design.',
                                            'source':'Richard Redding Antiques', 'url':'https://www.richardreddingantiques.com/artists/289-robert-garrard/biography/'},
                        'Hester Bateman': {'description': ' (bap. 1708 – 16 September 1794[1]) was an English silversmith, renowned for her high quality flatware and ornamental silverware. A craftswoman working within the family business, she was succeeded in turn by her sons, daughter-in-law, grandson and great-grandson. The Bateman family silversmithing company lasted until the middle of the nineteenth century.',
                                        'source': 'Wikipedia', 'url':'https://en.wikipedia.org/wiki/Hester_Bateman'},


                        'Joseph Wilmore': {'description':', Birmingham Silvermaker. Registered his mark at the Birmingham Assay Office as a snuff-box maker in 1806. In 1816 after his grandfather Thomas Willmor (a well known silversmith himself) died Joseph incorporated his grandfathers business into his own giving him more scope to expand the variety of silver wares he could make and sell. Joseph had a showroom in Bouverie street London. He continued to register marks untill 1843 and died in 1855.',
                                'source': 'Antiques Atlas', 'url': 'https://www.antiques-atlas.com/antiques/maker/joseph_willmore'},
}

time_period = ['16th century', '17th century', '18th century', '19th century', '20th century']


ceramic_subjects = ['Dish', 'Bowl', 'Cup', 'Teapot', 'Figure', 'Tile', 'Jug', 'Vase']

ceramic_materials = ['Earthenware', 'Porcelain','Stoneware', 'Gold metal', 'Glass', 'Marble']

ceramic_styles = ['Ottoman', 'Armorial', 'Kakiemon', 'Chinese export', 'Modernist',  'Arts and Crafts']

ceramic_artists = ['Delft', 'Lucie Rie', 'Johann Kandler', 'Martin Hunt', 'Iznik', 'Wedgwood', 'Keith Murray', 'Susie Cooper']

fashion_subjects = ['Costume', 'Suit', 'Hat', 'Jacket','Trousers', 'Evening', 'Shirt',
'Necklace', 'Dress', 'Shoes']

fashion_styles = ['High Fashion', 'East Asian', 'Theatrical']

fashion_materials = ['Cotton','Crystals', 'Silk', 'Pearls', 'Sequins', 'Leather',
'Straw', 'Snakeskin']

fashion_artists = ['William Morris','Balenciaga', 'Versace', 'Vivienne Westwood',  'Yves Saint Laurent', 'Yoruba Women' ]

furniture_subjects = ['Table', 'Chair', 'Candlestick', 'Carving', 'Clock']

furniture_styles = ['Rococo', 'Baroque', 'Art Nouveau', 'Art Deco']

furniture_materials = ['Wood', 'Metal', 'Glass', 'Silver']

furniture_artists = ['Ashbee Robert', 'Garrard Robert', 'Hester Bateman', 'Joseph Wilmore']

ceramic_materials.sort()
fashion_materials.sort()
furniture_materials.sort()

ceramic_material = widgets.SelectMultiple(options = ceramic_materials,layout=Layout(width='12%', height='80px'))
fashion_material = widgets.SelectMultiple(options = fashion_materials,layout=Layout(width='12%', height='80px'))
furniture_material = widgets.SelectMultiple(options = furniture_materials,layout=Layout(width='12%', height='80px'))


layout_big = widgets.Layout(width='400px', height='50px')

layout_small = widgets.Layout(width='200px', height='25px')

select_layout = Layout(width='12%', height='80px')

century = widgets.Dropdown(options = time_period, layout = Layout(width='15%', height='30px'))

from rudalle import get_rudalle_model, get_vae
import torch
from model.functions import generate, get_closest_training_images_by_clip

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model = get_rudalle_model("Malevich", pretrained=True, fp16=True, device=device)

vae = get_vae().to("cuda")

img_amount = widgets.IntSlider(value=2,min=1,max=8,step=1,description='<b>Image amount: </b>',style= {'description_width': 'initial'}, layout = layout_big)
img_amount.style.handle_color = 'lightblue'

collection = widgets.Dropdown(options = ['Ceramics', 'Fashion', 'Furniture & Metalwork'], layout = Layout(width='15%', height='30px'))
collection_and_century = widgets.HTML(value = "<b>Collection & Century: </b>", layout=Layout(width='11%', height='20px'))

space = widgets.HTML(value = "", layout=Layout(width='3%', height='40px'))
space1 = widgets.HTML(value = "", layout=Layout(width='9%', height='20px'))
header1 = widgets.HTML(value = "<font size=3><font color='black'>Ceramics", layout=Layout(width='15%', height='20px'))
header2 = widgets.HTML(value = "<font size=3><font color='black'>Fashion", layout=Layout(width='15%', height='20px'))
header3 = widgets.HTML(value = "<font size=3><font color='black'>Furniture", layout=Layout(width='15%', height='20px'))

object_text = widgets.HTML(value = "<font size=2><font color='black'>Object", layout=Layout(width='5%', height='80px'))

ceramic_subjects.sort()
fashion_subjects.sort()
furniture_subjects.sort()

ceramic_subject = widgets.SelectMultiple(options = ceramic_subjects,layout=Layout(width='12%', height='80px'))
fashion_subject = widgets.SelectMultiple(options = fashion_subjects,layout=Layout(width='12%', height='80px'))
furniture_subject = widgets.SelectMultiple(options = furniture_subjects,layout=Layout(width='12%', height='80px'))

ceramic_styles.sort()
fashion_styles.sort()
furniture_styles.sort()

style_text = widgets.HTML(value = "<font size=2><font color='black'>Style", layout=Layout(width='5%', height='80px'))
material_text = widgets.HTML(value = "<font size=2><font color='black'>Material", layout=Layout(width='5%', height='80px'))

ceramic_style = widgets.SelectMultiple(options = ceramic_styles,layout = select_layout)
fashion_style = widgets.SelectMultiple(options = fashion_styles,layout = select_layout)
furniture_style = widgets.SelectMultiple(options = furniture_styles,layout = select_layout)

ceramic_artists.sort()
fashion_artists.sort()
furniture_artists.sort()

artist_text = widgets.HTML(value = "<font size=2><font color='black'>Maker", layout=Layout(width='5%', height='80px'))

ceramic_artist = widgets.SelectMultiple(options = ceramic_artists, layout = select_layout)
fashion_artist = widgets.SelectMultiple(options = fashion_artists, layout = select_layout)
furniture_artist = widgets.SelectMultiple(options = furniture_artists, layout = select_layout)


def artist_description():
    if ceramic_artist.value is not None:
        for artist in ceramic_artist.value:
            description = ceramic_artist_desc[artist]['description']
            ceramic_artist_widget = widgets.HTML(value = f"<b><font size=3.5><font color='black'>{artist}</b>" + f"<font size=3><font color='black'>{description}" + '<hr>', placeholder = artist)
            display(ceramic_artist_widget)
    if fashion_artist.value is not None:
        for artist in fashion_artist.value:
            description = fashion_artist_desc[artist]['description']
            fashion_artist_widget = widgets.HTML(value = f"<b><font size=3.5><font color='black'>{artist}</b>" + f"<font size=3><font color='black'>{description}" + '<hr>', placeholder = artist)
            display(fashion_artist_widget)

    if furniture_artist.value is not None:
        for artist in furniture_artist.value:
            description = furniture_artist_desc[artist]['description']
            furniture_artist_widget = widgets.HTML(value = f"<b><font size=3.5><font color='black'>{artist}</b>" + f"<font size=3><font color='black'>{description}" + '<hr>', placeholder = artist)
            display(furniture_artist_widget)   

#Artist Descriptions 
output1 = widgets.Output()

button_description = widgets.Button(description = 'Artist / Maker Description', tooltip='Send',
                style={'description_width': 'initial'}, layout = layout_small)

button_description.style.button_color = 'lightgreen'

def on_button_description_clicked(event):
    clear_output()

    with output1:
        prompt = artist_description() 


button_description.on_click(on_button_description_clicked)

def get_closest_training_images_by_clip(artist, prompt, directory):
    from transformers import CLIPProcessor, CLIPModel
    from PIL import Image
    from tqdm import tqdm
    model = CLIPModel.from_pretrained('openai/clip-vit-base-patch32')
    processor = CLIPProcessor.from_pretrained('openai/clip-vit-base-patch32')
    filenames = os.listdir(directory)
    score = 0
    to_search = []
    if artist is not None:
        for f in filenames:
            if artist in f:
                to_search.append(f)
    else:
        to_search = filenames
    while len(to_search) > 500:
        to_search = to_search[::2]
    for i, f in enumerate(tqdm(to_search)):
        image = Image.open(f'{directory}/{f}')
        inputs = processor(text=[prompt], images = image, return_tensors = 'pt', padding=True)
        outputs = model(**inputs)
        logits_per_image = outputs.logits_per_image 
        s = logits_per_image.item()
        if s > score:
            score = s
            index = i
    return filenames[index]

def construct_prompt():
    prompt = ''
    if collection.value is not None:
        prompt += f'{collection.value}, '
    if century.value != 'Any':
        prompt += f'{century.value}, '
    styles = ceramic_style.value + fashion_style.value + furniture_style.value
    for st in styles:
        prompt += f'of style {st}, '

    if ceramic_artist.value is not None:
        for artist in ceramic_artist.value:
            prompt += f'by {artist}, '
    if fashion_artist.value is not None:
        for artist in fashion_artist.value:
            if artist == 'Rie Lucie':
                artist = 'Lucie Rie'
            if artist == 'Martin Hunt':
                artist = 'Hunt Martin'
            if artist == 'Iznik':
                artist = 'IZNIK'
            prompt += f'by {artist}, '
    if furniture_artist.value is not None:
        for artist in furniture_artist.value:
            prompt += f'by {artist}, '
    if ceramic_subject.value is not None:
        for subject in ceramic_subject.value:
            prompt += f'{subject}, '
    if fashion_subject.value is not None:
        for subject in fashion_subject.value:
            prompt += f'{subject}, '

    if furniture_subject.value is not None:
        for subject in furniture_subject.value:
            prompt += f'{subject}, '

    materials = ceramic_material.value + fashion_material.value + furniture_material.value
    for m in materials:
        prompt += f'{m}, '

    return prompt

output2 = widgets.Output()

#View prompt

view_prompt_button = widgets.Button(description = 'Construct prompt', tooltip='Send',
                style={'description_width': 'initial'}, layout = layout_small)

view_prompt_button.style.button_color = 'lightgreen'

def on_view_button_prompt_clicked(event):
    with output2:
        clear_output()
        prompt = construct_prompt() 
        constructed_prompt = widgets.HTML(value = f"<font size=3><font color='black'>Constructed prompt: {prompt}" + '<hr>')
        display(constructed_prompt)

view_prompt_button.on_click(on_view_button_prompt_clicked)

import os
output3 = widgets.Output()

def on_run_button_clicked(event):
    with output3:
        clear_output()
        model_path = 'model_file/lookingglass_dalle_90000.pt'

        if not os.path.exists('output/'):
            os.mkdir('output/')
        prompt = construct_prompt()

        if ('Iznik' in prompt or 'Kakiemon' in prompt) and 'Tile' not in prompt and 'Dish' not in prompt:
            prompt += ' Dish'
        if 'Tile' in prompt:
            prompt.replace('Tile', 'Panel')
        if 'Delft' in prompt and '17th' not in prompt:
            prompt += ' 17th century'

        if 'Morris' in prompt or 'Yoruba' in prompt:
            prompt += ' Textiles'
        if 'Morris' in prompt:
            prompt += ' 19th century'

        if 'Wood' in prompt:
            if 'Furniture' in prompt:
                prompt.replace('Metalwork', '')
        prompt += '.jpg'

        filepath = f'output/{prompt}'
        if not os.path.exists(filepath):
            os.mkdir(filepath)
        model.load_state_dict(torch.load(model_path))
        filenames = generate(vae, model, prompt, confidence = 'Low', variability = 'Ultra-High', rurealesrgan_multiplier="x1", output_filepath=filepath, num_filtered = img_amount.value, image_amount = int(img_amount.value*1.6))
        print(f'Images saved in {filepath}')
        for image in filenames:
            img = Image(image)
            display(img)
        return filenames

#Run model 
button_run = widgets.Button(description = 'Run model', tooltip='Send',
                style={'description_width': 'initial'}, layout = layout_big)
button_run.style.button_color = 'lightblue'
button_run.on_click(on_run_button_clicked)

vbox_result = widgets.VBox([button_run, output3])




from PyPDF2 import PdfWriter, PdfReader

reader = PdfReader("example.pdf")
writer = PdfWriter()

lowerLeft = 842/2

def crop_sides(page_to_crop, side='right'):

    if(side == 'right'):
        page_to_crop.cropbox.lower_left = (0, 0)
        page_to_crop.cropbox.upper_right = (595.22, lowerLeft)
        writer.add_page(page_to_crop)
    elif(side == 'left'):
        page_to_crop.cropbox.lower_left = (0, lowerLeft)
        page_to_crop.cropbox.upper_right = (595.22, 842)
        writer.add_page(page_to_crop)

for each_page in reader.pages:
    crop_sides(each_page, 'right')
    crop_sides(each_page, 'left')

# add some Javascript to launch the print window on opening this PDF.
# the password dialog may prevent the print dialog from being shown,
# comment the the encryption lines, if that's the case, to try this out:
writer.add_js("this.print({bUI:true,bSilent:false,bShrinkToFit:true});")

# write to document-output.pdf
with open("PyPDF2-output.pdf", "wb") as fp:
    writer.write(fp)

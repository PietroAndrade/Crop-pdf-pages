from PyPDF2 import PdfWriter, PdfReader

reader = PdfReader("example.pdf")
writer = PdfWriter()

#Variables
y_upper_right = 0
x_upper_right = 0
y0_lower_left = 0
x0_lower_left = 0

lowerLeft = 0

#Methods
def crop_sides(page_to_crop, side='right'):

    if(side == 'right'):
        page_to_crop.cropbox.lower_left = (y0_lower_left, x0_lower_left)
        page_to_crop.cropbox.upper_right = (y_upper_right, lowerLeft)
        writer.add_page(page_to_crop)
    elif(side == 'left'):
        page_to_crop.cropbox.lower_left = (y0_lower_left, lowerLeft)
        page_to_crop.cropbox.upper_right = (y_upper_right, x_upper_right)
        writer.add_page(page_to_crop)

def eval_sizes(page_to_eval):
    yx = page_to_eval.cropbox.upper_right
    y_upper_right = yx[0]
    x_upper_right = yx[1]
    print(f'{y_upper_right},{x_upper_right}')

    x0y = page_to_eval.cropbox.lower_right
    y_lower_right = x0y[0]
    x0_lower_right = x0y[1]
    print(f'{y_lower_right},{x0_lower_right}')

    xy0 = page_to_eval.cropbox.upper_left
    y0_upper_left = xy0[0]
    x_upper_left = xy0[1]
    print(f'{y0_upper_left},{x_upper_left}')

    xy00 = page_to_eval.cropbox.lower_left
    y0_lower_left = xy00[0]
    x0_lower_left = xy00[1]
    print(f'{y0_lower_left},{x0_lower_left}')

    lowerLeft = x_upper_right/2
    print(f'Half:{lowerLeft}')

#Executing
eval_sizes(reader.pages[1])

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

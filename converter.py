import os
import pdfkit as pdf
from os.path import join as pjoin


def pdf_converter():
    extension = ".html"
    # output file options
    pdf_option = {
        'page-size': 'Letter',
        'margin-top': '0.25in',
        'margin-right': '0.25in',
        'margin-bottom': '0.25in',
        'margin-left': '0.25in',
        'encoding': "UTF-8",
        'no-outline': None
    }
    # get current working directory
    cwd = os.getcwd()
    # file name and pdf name list
    filename = []
    pdf_name = []
    pdf_destination = []
    # walk to sub directories
    sub_dir = [x[0] for x in os.walk(cwd)]
    for subdir in sub_dir:
        files = next(os.walk(subdir))[2]
        if len(files) > 0:
            for file in files:
                if extension in file:
                    # get first name of the file ex test from test.html and add .pdf extension
                    t_fname = os.path.splitext(file)[0]+".pdf"
                    # store filename if necessary
                    filename.append(file)
                    # file path
                    f_path = subdir+"/"+file
                    with open(os.path.abspath(f_path)) as f:
                        pdf.from_file(f, t_fname, options=pdf_option)
                        pdf_name.append(t_fname)
                        pdf_destination.append(subdir)
                        # join dir
                    path = pjoin(subdir, t_fname)
                    open(path, "w")
    # delete the original path after moving files to respective directory
    for temp in pdf_name:
        os.remove(cwd+"/"+temp)


pdf_converter()

#!/usr/bin/python
#	 pip install requests
import requests
import os

input_dir = "HTML"              # Sub folder of webfiles
output_dir = "HTML_minified"

f_output = open("output_dir", "w")
URL_minify_js   = 'https://javascript-minifier.com/raw' # Website to minify javascript
URL_minify_html = 'https://html-minifier.com/raw'        # Website to minify html
URL_minify_css  = 'https://cssminifier.com/raw'         # Website to minify css

def write_to_file(file, data, dir=""):
    filename, file_extension = os.path.splitext(file)       # Split filename and file extension
    file_extension = file_extension.replace(".","")         # Remove puncuation in file extension

    dir = dir.replace(input_dir,"")                         # Remove the first directory(input_dir)
    dir = dir.replace("\\","/")                             # Chang to /
    f_output.write("// " + dir + "\n")                      # Print comment
    f_output.write("const char* data_" + filename + "_" + file_extension + "_path PROGMEM = \""+str(dir)+"\";\n")    # print path
    f_output.write("const char data_"+filename+"_"+file_extension+"[] PROGMEM = {"+data.upper()+"};\n\n")            # print binary data

    # f_output.write("#define data_" + filename + "_len " + str(data.count('0x')) +"\n")

def aschii2Hex(text):
    output_str = ""
    x = 1
    strLen = len(text)
    for character in text:
        output_str += hex(ord(character))

        if (x != strLen):
            output_str += ","
        x += 1
    return output_str

def minify_js(input_file):
    url = URL_minify_js
    data = {'input': open(input_file, 'rb').read()}
    response = requests.post(url, data=data)
    return response.text

def minify_html(input_file):
    url = URL_minify_html
    data = {'input': open(input_file, 'rb').read()}
    response = requests.post(url, data=data)
    return response.text

def minify_css(input_file):
    url = URL_minify_css
    data = {'input': open(input_file, 'rb').read()}
    response = requests.post(url, data=data)
    return response.text


for root, dirs, files in os.walk(input_dir, topdown=False):
    for name in files:   # for files
        if name.endswith(".js"):
            print(os.path.join(root, name))
            minified = minify_js(os.path.join(root, name))          # minify javascript
            hexified = aschii2Hex(minified)                         # convert to hex
            write_to_file(name, hexified, os.path.join(root, name)) # write to file

        elif name.endswith(".html"):
            print(os.path.join(root, name))
            minified = minify_html(os.path.join(root, name))        # minify html
            hexified = aschii2Hex(minified)                         # convert to hex
            write_to_file(name, hexified, os.path.join(root, name)) # write to file

        elif name.endswith(".css"):
            print(os.path.join(root, name))
            minified = minify_css(os.path.join(root, name))         # minify css
            hexified = aschii2Hex(minified)                         # convet to hex
            write_to_file(name, hexified, os.path.join(root, name)) # write to file


f_output.close()
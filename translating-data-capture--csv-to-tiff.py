#!/usr/bin/python

# csv2tiff.py 
# reads xyz data from csv, creates a tiff where z is the brightness. 

from csv import reader
import Image, ImageDraw

file_base = 'test'

# put the whole file into a list
# get some info about the file
# and ignore some heder/footer stuff
xyzs=[]
max_x,max_y,max_z=0,0,0
for xyz in reader(open(file_base + '.csv')):
    if len(xyz)<>3: continue # ignore [['header: 61445'], ['footer: 61440']]
    xyz = [int(s) for s in xyz]

    # add to the list we are building
    xyzs.append(xyz)

    # seperate vars are eayser for the analysis code
    x,y,z = xyz

    # is x,y divisible by 5?
    if x%5 or y%5: print xyz
    # find max x,y,z
    if x>max_x: max_x = x
    if y>max_y: max_y = y
    if z>max_z: max_z = z

print max_x,max_y,max_z
max_x,max_y = max_x/5+1, max_y/5+1
print max_x,max_y,max_z
    
# make tiff
# im = Image.new("RGBA", (max_x,max_y), )
im = Image.new("I", (max_x,max_y), )
pix=im.load()
for x,y,z in xyzs:
    # squish the number into 8bit space
    z1 = z * 256/max_z
    # or 10 bit
    z2 = z * 1024/max_z
    # or 16
    z3 = z * 65535/max_z
    # sung them up
    x,y = x/5, y/5
    # I have no idea which z to use
    # z3 is the most interesting.
    pix[x,y] = z3

im.save( open(file_base + '.tiff','wb'), format='TIFF' )
im.show()
 

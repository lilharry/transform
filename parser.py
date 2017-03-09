from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix - 
        takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
     ident: set the transform matrix to the identity matrix - 
     scale: create a scale matrix, 
        then multiply the transform matrix by the scale matrix - 
        takes 3 arguments (sx, sy, sz)
     translate: create a translation matrix, 
        then multiply the transform matrix by the translation matrix - 
        takes 3 arguments (tx, ty, tz)
     rotate: create a rotation matrix,
        then multiply the transform matrix by the rotation matrix -
        takes 2 arguments (axis, theta) axis should be x, y or z
     yrotate: create an y-axis rotation matrix,
        then multiply the transform matrix by the rotation matrix -
        takes 1 argument (theta)
     zrotate: create an z-axis rotation matrix,
        then multiply the transform matrix by the rotation matrix -
        takes 1 argument (theta)
     apply: apply the current transformation matrix to the 
        edge matrix
     display: draw the lines of the edge matrix to the screen
        display the screen
     save: draw the lines of the edge matrix to the screen
        save the screen to a file -
        takes 1 argument (file name)
     quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    f = open(fname,'r')
    lines = f.readlines()
    f.close()

    i = 0

    while i < len(lines):
        line = lines[i].strip("\n")
        print line
        if line == "ident":
            ident(transform)
        elif line == "line":
            i+=1
            line = lines[i].strip("\n").split(' ')

            x1 = float(line[0])
            y1 = float(line[1])
            z1 = float(line[2])
            x2 = float(line[3])
            y2 = float(line[4])
            z2 = float(line[5])
            add_edge(points,x1,y1,z1,x2,y2,z2)
            
        elif line == "scale":
            i+=1
            line = lines[i].strip("\n").split(' ')
            x = float(line[0])
            y = float(line[1])
            z = float(line[2])
            matrix_mult(make_scale(x,y,z),transform)
        elif line == "translate" or line == "move":
            i+=1
            line = lines[i].strip("\n").split(' ')
            x = float(line[0])
            y = float(line[1])
            z = float(line[2])
            matrix_mult(make_translate(x,y,z),transform)
        
        elif line == "rotate":
            i+=1
            line = lines[i].strip("\n").split(' ')
            axis = line[0].lower()
            theta = float(line[1])
            if axis == 'x':
                matrix_mult(make_rotX(theta),transform)
            elif axis == 'y':
                matrix_mult(make_rotY(theta),transform)
            elif axis == 'z':
                matrix_mult(make_rotZ(theta),transform)

        elif line == "xrotate":
            i+=1
            line = lines[i].strip("\n")
            theta = float(line)
            matrix_mult(make_rotX(theta),transform)
        elif line == "yrotate":
            i+=1
            line = lines[i].strip("\n")
            theta = float(line)
            matrix_mult(make_rotY(theta),transform)
        elif line == "zrotate":
            i+=1
            line = lines[i].strip("\n")
            theta = float(line)
            matrix_mult(make_rotZ(theta),transform)


        elif line == "apply":
            matrix_mult(transform,points)
        elif line == "display":
            draw_lines(points,screen,color)
            display(screen)
        elif line == "save":
            i+=1
            line = lines[i].strip("\n")
            draw_lines(points,screen,color)
            save_ppm(screen,line)

        elif line == "quit":
            print "done parsing"
            return
        else:
            print "invalid command on line %d: %s"%(i,line)
            return
        i+=1
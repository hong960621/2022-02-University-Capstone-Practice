import sys

def get_inputs():
    if len(sys.argv) != 2:
        print("Usage: {0} CAR_file \n".format(sys.argv[0]))
        sys.exit()
    else:
        file_name=sys.argv[1]
        return file_name

def get_file_string_arry(file_name):
    try:
        file=open(file_name,"r")
    except IOError:
        print("Error: {0} file is not found! \n".format(file_name))
        sys.exit()
    lines=file.readlines()
    file.close()
    array=[]
    tot_atom=0
    for i in range(len(lines)):
        array.append(lines[i].split())
        tot_atom += 1
    return array, tot_atom

print('array')
print('tot_atom')
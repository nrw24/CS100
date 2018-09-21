'''Navado Wray
CS100 Section 004 S18
March 24,2018'''
#1
def file_copy(in_file,out_file):
    open(in_file, 'r')
    open(out_file, 'w')
    out_file.write(in_file.read())
    out_file.close()
    in_file.close()


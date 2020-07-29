#!/usr/bin/python
import argparse
import configparser
import zoomermodule as zm

def main(option = None):
    config = configparser.ConfigParser()
    config.read('data.ini')
    joinposn = config['VALUES']['join'].split(', ') #list(coordinates of join button)
    joinposn = [int(x) for x in joinposn]
    if joinposn == [0,0]:
        print("Oops, it looks like you haven't set the positon of join button.")

    if option == None:
        zoomId,zoomPass = zm.get_id_pass(zm.get_subject())
    elif option == args.subject:
        zoomId,zoomPass = zm.get_idpass_by_subject(option)
    else:
        zoomId,zoomPass = option
    zm.zoom(zoomId,zoomPass,joinposn)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Command line interface for zoomer.py",formatter_class = argparse.RawTextHelpFormatter)
    parser.add_argument('-gmp','--getmousepos',action = 'store_true',help = "\ndescr:command to get mouse position \n")
    parser.add_argument('-m',dest = 'subject',metavar = 'subject',help = "\ndescr:manually enter the subject \n\n")
    parser.add_argument('-M',dest = 'ultramanual',nargs = 2,metavar = ('id','password'),help = "\ndescr:manually enter id and password \n\n")
    parser.add_argument('-a',dest = 'append',nargs = 3,metavar = ('subject', 'id', 'password'),help = "descr:append data to passwords.csv \n\n")
    parser.add_argument('-p','--passwd',dest = 'changepass',nargs = 2,metavar = ('subject','new_password'), help = 'descr:change the password corresponding to the subject \n\n') 
    parser.add_argument('-u','--updatepass',dest = 'updatepass',metavar = 'path',help = "descr:updates passwords.csv with data extracted from docx at path \n\n")
    args = parser.parse_args()
    
    if args.getmousepos:
        zm.getjoinposn()
    if args.updatepass != None:
        zm.updatepass(args.updatepass)
    if args.append != None:
        zm.append(args.append)
    if args.changepass != None:
        zm.changepass(args.changepass)

    if args.subject != None:
        main(args.subject)
    elif args.ultramanual != None:
        main(args.ultramanual)
    else:
        main()

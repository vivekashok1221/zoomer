import argparse
import configparser

import utils


def main(option=None):
    config = configparser.ConfigParser()
    config.read("data.ini")
    joinposn = config["VALUES"]["join"].split(", ")
    try:
        joinposn = [int(x) for x in joinposn]
    except ValueError:
        print("Oops, it looks like you haven't set the positon of join button.")

    if option is None:
        zoomId, zoomPass = utils.get_credentials(utils.get_subject())
    elif option == args.subject:
        zoomId, zoomPass = utils.get_credentials(option)

    utils.auto_type(zoomId, zoomPass, joinposn)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Command line interface for zoomer.py",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "-gmp",
        "--getmousepos",
        action="store_true",
        help="\ndescr:command to get mouse position \n",
    )
    parser.add_argument(
        "-m",
        dest="subject",
        metavar="subject",
        help="\ndescr:manually enter the subject \n\n",
    )

    parser.add_argument(
        "-a",
        dest="append",
        nargs=3,
        metavar=("subject", "id", "password"),
        help="descr:append data to passwords.csv \n\n",
    )
    parser.add_argument(
        "-p",
        "--passwd",
        dest="changepass",
        nargs=2,
        metavar=("subject", "new_password"),
        help="descr:change the password corresponding to the subject \n\n",
    )
    parser.add_argument(
        "-u",
        "--updatepass",
        dest="updatepass",
        metavar="path",
        help="descr:updates passwords.csv with data extracted from docx at path \n\n",
    )
    args = parser.parse_args()

    if args.getmousepos:
        utils.getjoinposn()
    elif args.updatepass is not None:
        utils.updatepass(args.updatepass)
    elif args.append is not None:
        utils.append(args.append)
    elif args.changepass is not None:
        utils.changepass(args.changepass)
    elif args.subject is not None:
        main(args.subject)
    else:
        main()

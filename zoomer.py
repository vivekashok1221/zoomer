import configparser
from cli import parse_arguments
import utils


def main():
    args = parse_arguments()

    if args.getmousepos:
        utils.getjoinposn()
    elif args.updatepass is not None:
        utils.update_pass(args.updatepass)
    elif args.append is not None:
        utils.append(args.append)
    elif args.changepass is not None:
        utils.change_pass(args.changepass)
    else:
        config = configparser.ConfigParser()
        config.read("data.ini")
        joinposn = config["VALUES"]["join"].split(", ")
        try:
            joinposn = [int(x) for x in joinposn]
        except ValueError:
            # fmt: off
            print(
                "Oops, it looks like you haven't"
                "set the positon of join button."
                )
            # fmt: on

        subject = utils.get_subject() if args.subject is None else args.subject
        zoom_id, zoom_pass = utils.get_credentials(subject)
        utils.auto_type(zoom_id, zoom_pass, joinposn)


if __name__ == "__main__":
    main()

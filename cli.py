import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Command line interface for zoomer.py",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument(
        "--setup",
        action="store_true",
        help="sets up zoomer.py",
    )

    parser.add_argument(
        "--reset",
        action="store_true",
        help="resets zoomer.py and clears the database.",
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
        # fmt: off
        help=(
            "descr:updates passwords.csv with"
            "data extracted from docx at path \n\n"
        ),
        # fmt: on
    )

    return parser.parse_args()

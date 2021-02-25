from page_loader.cli import arg_parse
from page_loader.loader import download


def main():
    parser = arg_parse()
    args = parser.parse_args()
    print(download(args.url, args.output))


if __name__ == "__main__":
    main()

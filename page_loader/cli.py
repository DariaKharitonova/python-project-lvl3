import os
import argparse


def arg_parse():
    parser = argparse.ArgumentParser(description='Page loader')
    parser.add_argument('url', type=str)
    parser.add_argument('--output',
                        type=str,
                        default=os.getcwd())
    return parser

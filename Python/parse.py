import argparse

parser = argparse.ArgumentParser('Program Description')
parser.add_argument('--foo', help='foo help')

args = parser.parse_args()

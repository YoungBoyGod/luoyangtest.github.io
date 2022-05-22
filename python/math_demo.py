#! /bin/python

import argparse
import math

parser = argparse.ArgumentParser(description='计算圆柱的体积')
parser.add_argument('-r', '--radius', metavar='', required=True, type=int, help='半径')
parser.add_argument('-H', '--height', metavar='', required=True, type=int, help='高')

group = parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quiet', action="store_true", help='简单打印')
group.add_argument('-v', '--verbose', action="store_true", help='详细信息')

args = parser.parse_args()


def cylinder_volume(radius, height):
    vol = math.pi * (radius ** 2) * height
    return vol


if __name__ == '__main__':
    volume = cylinder_volume(args.radius, args.height)
    if args.quiet:
        print(volume)
    elif args.verbose:
        print('圆柱的体积公式:半径是：%s,高度是:%s,体积是:%s' % (args.radius, args.height, volume))
    else:
        print('圆柱体积是：%s'% volume)
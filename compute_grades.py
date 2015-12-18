#! /usr/bin/env python

import grade

if __name__ == '__main__':
    import argparse as ap
    p = ap.ArgumentParser()
    p.add_argument('files', help = "Target fileNames", nargs = '+')
    args = p.parse_args()
    files = args.files
    # Use the function from module grade to compute all grades in the list of
    # files. The list is in the variable "files"
    


    




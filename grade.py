#! /usr/bin/env python



def compute_line_points(line):
    ''' (str) -> float

    Compute the point value of the given line. If the line is empty, returns 0.

    >>> compute_line_points("1   H   0.6 1")
    0.6
    >>> compute_line_points("2   AI  0.8 0.5")
    0.4
    >>> compute_line_points("")
    0
    '''



def sum_line_points(lines):
    ''' (list of str) -> float

    Compute the sum of the point values of the lines.
    This function must use the function compute_line_points.

    >>> sum_line_points(["1   H   0.6 1", "2   AI  0.8 0.5", ""])
    1.0
    >>> sum_line_points(["1   H   0.8 0.5", "2   AI  0.6 0.5", ""])
    0.7
    '''



def compute_grade(fileName):
    ''' (str) -> float

    Returns the total grade for the GRADE file with name 'fileName'.
    This function must use the function sum_line_points after having read
    the file into a list of strings using the method file.readlines.

    >>> compute_grade("GRADE_Chuck_Norris.txt") >= 22
    True
    '''





if __name__ == '__main__':
    import doctest
    res = doctest.testmod()
    print res
    if res.failed == 0:
        import argparse as ap
        p = ap.ArgumentParser()
        p.add_argument('file', help = "Target fileName")
        args = p.parse_args()
        print args.file, compute_grade(args.file)




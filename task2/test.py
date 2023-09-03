from . import solution
import pytest
import os
import csv


def test_parser_give_same_result():
    launchs = 2
    results = [None] * launchs
    
    prev = solution.get_letters_and_counts()
    
    for i in range(launchs - 1):
        curr = solution.get_letters_and_counts()
        assert curr == prev
        prev = curr
        
   
@pytest.mark.parametrize('args', [['./task2/test_out.csv', [[1,2,3], ['a', 'b', False],]],
                                              ['./testout.txt', [[0, 0, 0, 'a'], [1,2,3]],]])     
def test_csv_writer(args):
    out, rows = args
    solution.fill_file(out, rows)
    
    with open(out, 'r') as file:
        reader = csv.reader(file, escapechar='\n')
        i = 0
        
        for row in reader:
            assert row == [str(c) for c in rows[i]]
            i += 1
    
    os.remove(out)

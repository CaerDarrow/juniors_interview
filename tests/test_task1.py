from solution.task1 import strict

def test_sum_two():

    @strict
    def sum_two(a:int,b:int)->int:
        return a + b
    
    assert sum_two(1,2) == 3
    try:
        sum_two(1,2.4) != 3.4
    except TypeError as e:
        pass

def test_sum_two_str():    
    @strict
    def sum_two_str(a:str,b:str)->str:
        return a + b
    
    assert sum_two_str('1','2') == '12'

def test_pr_two():

    @strict
    def pr_two(a:int,b:str)->str:
        return a * b
    
    assert pr_two(3,'2') == '222'


    

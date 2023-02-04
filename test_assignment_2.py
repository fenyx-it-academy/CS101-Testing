from assignment_2 import alphaSort

def test_assigment_2():
    input_string = "yellow-red-blue"
    result = alphaSort(input_string)
    
    assert result == "blue-red-yellow"

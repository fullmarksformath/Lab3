from Lab2.bmi import calculate_bmi

def test_bmi_under_weight():
    result=calculate_bmi(weight=50,height=1.8)
    assert (result==-1)

def test_bmi_normal_weight():
    result=calculate_bmi(weight=55,height=1.7)
    assert (result==0)

def test_bmi_over_weight():
    result=calculate_bmi(weight=70,height=1.6)
    assert (result==1)
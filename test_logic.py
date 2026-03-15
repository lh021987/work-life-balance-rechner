from logic import calc_balance, trend_label

#def test_calc_balance():
        #result = calc_balance("training", 6.5, 0, 8, 2, 0.5)
        #assert round(result,3 == 1.161)


def test_calc_balance_no_load():
        result = calc_balance("general", 8, 1, 0, 0, 0)
        assert round(result,0) == 170

def test_calc_balance_profile_difference():
    result_general = calc_balance("general", 6, 1, 8, 2, 0)
    result_training = calc_balance("training", 6, 1, 8, 2, 0)

    assert round(result_general,3) == 1.605
    assert round(result_training,3) == 1.215

def test_trend_better():

    balances = [
        1.0,1.1,1.0,1.1,1.0,1.1,1.0,
        1.3,1.4,1.3,1.4,1.3,1.4,1.3
    ]

    label, w1, w2, delta = trend_label(balances)

    assert label == "better"
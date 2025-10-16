from ticket_maker import get_product_list, get_purchase_sum
import tkinter as tk 
from os import path

from pytest import approx
import pytest

def test_get_product_list():
    """
    This function verifies if the function to get the product list from a csv file works correctly
    """
    #path to the file with the products and calling function to get the dictionary 
    path.join(path.dirname(__file__), "products.csv")
    products_dict = get_product_list()

    # Verify that the dictionary that results from the function works as expected
    expected_results_dict = {'Milk': ['149098701', 'Milk', ' 1'], 'Bread': ['899087913', 'Bread', ' 0.5'], 'Honey': ['789093200', 'Honey', ' 1'], 'Dried Fruits': ['146890200', 'Dried Fruits', ' 1 '], 'Nuddles': ['133980890', 'Nuddles', ' 1.3'], 'Bottle of Water 2l': ['000135098', 'Bottle of Water 2l', ' 1.4'], 'Soda 1l': ['193490890', 'Soda 1l', ' 1.5'], 'Meat 1kg': ['134897010', 'Meat 1kg', ' 6'], 'Chicken 1kg': ['134907908', 'Chicken 1kg', ' 3']}

    assert products_dict == expected_results_dict


def test_purchase_sum():
    """
    This function evaluates product price * product amount with different parameters 
    """
    assert get_purchase_sum(1,5) == approx(5, 0.01)
    assert get_purchase_sum(1.5,3) == approx(4.5, 0.01)
    assert get_purchase_sum(0.3,8) == approx(2.4, 0.01)
    assert get_purchase_sum(6,5) == approx(30, 0.01)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
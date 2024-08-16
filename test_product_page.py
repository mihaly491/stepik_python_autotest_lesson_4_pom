import pytest
from .Pages.main_page import MainPage
from .Pages.product_page import ProductPage

LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

list_of_failed_num = [7]
tested_links = [f"{LINK}?promo=offer{i}" if i not in list_of_failed_num else
                pytest.param(f"{LINK}?promo=offer{i}",
                             marks=pytest.mark.xfail(reason="some bug", strict=True)
                             )
                for i in range(10)]


@pytest.mark.parametrize("link", tested_links)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()
    page.add_product_to_basket()
    page.should_be_success_message()
    page.product_name_in_success_alert_should_match_added_product_name()
    page.should_be_basket_cost()
    page.basket_cost_should_match_product_price()


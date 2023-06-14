from selenium.webdriver.common.by import By


class Locators:
    """Locators for loginpage"""
    USER_NAME = (By.CSS_SELECTOR, "#user-name")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    LOGIN_BTN = (By.CSS_SELECTOR, "#login-button")


    """Locator all words"""
    PRODUCTS = (By.CSS_SELECTOR, ".title")
    ERROR_MSD_INCOR_POWORD = (By.CSS_SELECTOR, "h3[data-test='error']")
    ERROR_MSD_INCOR_USER_NAME = (By.CSS_SELECTOR, "h3[data-test='error']")
    REMOVE_TEXT_IN_BUTTON = (By.CSS_SELECTOR, "#remove-sauce-labs-backpack")
    CART_ICON = (By.CSS_SELECTOR, ".shopping_cart_link")
    CART_ICON_QUANTITY = (By.CSS_SELECTOR, ".cart_quantity")
    CHACOUNT_YOUR_INFI = (By.CSS_SELECTOR, ".title")
    ERROR_LAST_NAME  = (By.CSS_SELECTOR, "h3[data-test='error']")
    ZIP_CODE_ERROR = (By.CSS_SELECTOR, ".error-message-container.error")
    ERROR_MSD_FIRST_NAME = (By.CSS_SELECTOR, ".error-message-container.error")
    OVERVIEW = (By.CSS_SELECTOR, ".title")
    PAYINFO = (By.CSS_SELECTOR, "div[class='summary_info'] div:nth-child(1)")
    BACK_TO_PRODUCT_TEXT = (By.CSS_SELECTOR ,"#back-to-products")
    YOUR_CART = (By.CSS_SELECTOR, "and_back_and_back_to_cart")
    YOUR_CART_BACK_INFO = (By.CSS_SELECTOR, ".title")
    THK_YOU_ORDER = (By.CSS_SELECTOR, ".complete-header")
    CART_PAGE_INFO = (By.CSS_SELECTOR, ".title")
    LOGIN_PAGE_LOCATOR = (By.CSS_SELECTOR,"div[id='login_credentials'] h4")



    """Problem user"""
    ADD_TO_CART  = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
    REMOVE_PROBLEM_USER = (By.CSS_SELECTOR, "#remove-sauce-labs-backpack")


    """Add to card"""
    ADD_TO_CART = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
    ADD_TO_CART_TWO_ITEM = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bike-light")
    REMOVE_BTN = (By.CSS_SELECTOR, "#remove-sauce-labs-backpack")

    """Cart page"""
    CART_PAGE = (By.CSS_SELECTOR, ".title")
    REMOVE_BTN_IN_CART = (By.CSS_SELECTOR, "#remove-sauce-labs-backpack")
    CONTINE_SHOP = (By.CSS_SELECTOR, "#continue-shopping")
    CHECOUNT_BTN = (By.CSS_SELECTOR, "#checkout")

    """Checkout: Your Information"""
    FIRST_NAME = (By.CSS_SELECTOR, "#first-name")
    CONTINE_CHECKOUNT_BTN = (By.CSS_SELECTOR, "#continue")
    LAST_NAME = (By.CSS_SELECTOR, "#last-name")
    ZIP_CODE = (By.CSS_SELECTOR, "#postal-code")
    CONTINE_INFO_BTN = (By.CSS_SELECTOR, "#continue")

    """Overview page"""
    LINK_PDP_PEGE = (By.CSS_SELECTOR, ".inventory_item_name")
    FINISH_BTN = (By.CSS_SELECTOR, "#finish")


    """Finish page"""
    GO_HOME_BTN = (By.CSS_SELECTOR, "#back-to-products")
    GO_CART_BTN = (By.CSS_SELECTOR, ".shopping_cart_link")


    """Critical patch case"""
    ITEM_1 = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
    ITEM_2 = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bike-light")
    ITEM_3 = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
    ITEM_4 = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-fleece-jacket")
    ITEM_5 = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")
    ITEM_6 = (By.XPATH, "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")


    """burger menu"""
    MENU_BTN = (By.CSS_SELECTOR, "#react-burger-menu-btn")
    CLOSE_BTN = (By.CSS_SELECTOR, "#react-burger-cross-btn")
    ABOUT_LINK = (By.CSS_SELECTOR, "#about_sidebar_link")
    LOGOUT_LINK = (By.CSS_SELECTOR, "#logout_sidebar_link")

    """Problem user"""

    ADD_TO_BAG_PROBLEM = (By.CSS_SELECTOR,"#add-to-cart-sauce-labs-backpack")
    REMOVE_TO_BAG_PROBLEM = (By.CSS_SELECTOR, "#remove-sauce-labs-backpack")










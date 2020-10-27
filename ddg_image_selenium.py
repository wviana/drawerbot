from urllib.parse import unquote
from selenium import webdriver

def search(query):
    options = webdriver.FirefoxOptions()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    # Clipart Monochrome Pictures
    driver.get(f'https://duckduckgo.com/?q={query}&t=ffab&iar=images&iax=images&ia=images&iaf=color%3AMonochrome%2Ctype%3Aclipart')

    img_tags = driver.find_elements_by_class_name('tile--img__img')

    try:
        for tag in img_tags:
            src = tag.get_attribute('data-src')
            src = unquote(src)
            src = src.split('=', maxsplit=1)
            src = src[1]
            yield src
    finally:
        driver.close()

if __name__ == '__main__':
    from pprint import pprint
    imgs_urls = list(search('sun'))
    pprint(imgs_urls)



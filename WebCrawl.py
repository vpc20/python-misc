import urllib

STRING_NOT_FOUND = -1


def get_url(page, start_pos):
    href_pos = page.find('<a href=', start_pos)
    if href_pos == STRING_NOT_FOUND:
        return None, STRING_NOT_FOUND
    str_quote_pos = page.find('"', href_pos)
    end_quote_pos = page.find('"', str_quote_pos + 1)
    url = page[str_quote_pos + 1:end_quote_pos]
    return url, end_quote_pos


def get_all_url(page):
    pos = 0
    url_list = []
    while True:
        url, last_pos = get_url(page, pos)
        if last_pos == -1:
            break
        url_list.append(url)
        pos = last_pos + 1
    return url_list


def crawl_web(seed_page):
    pages_to_crawl = [seed_page]
    crawled_pages = []
    while pages_to_crawl:
        curr_page = pages_to_crawl.pop()
        if curr_page not in crawled_pages:
            f = urllib.urlopen(curr_page)
            html_file = f.read()
            url_list = get_all_url(html_file)
            pages_to_crawl = pages_to_crawl + list(set(url_list) - set(crawled_pages))
            crawled_pages.append(curr_page)
            print (crawled_pages)
    return crawled_pages


x = crawl_web("https://www.udacity.com/cs101x/index.html")

from parsel import Selector

def get_opponents(html):
    selector = Selector(text=html)

    matches = selector.xpath('//table[@class="wikitable"]')[0]
    trs = matches.xpath('.//tr')

    opponents = []
    for tr in trs[1:]:
        opponent = {
            'link': None,
            'name': None,
            'outcome': None
        }

        opponent['outcome'] = tr.xpath('./td[1]/text()').get().strip('\n')
        opponent_node = tr.xpath('./td[3]')
        anchors = opponent_node.xpath('a')
        if len(anchors) == 1:
            a = anchors[0]
            href = a.xpath('@href').get()
            opponent['link'] = f"https://en.wikipedia.org{href}"
            opponent_name = a.xpath('text()').get()
        else:
            opponent_name = opponent_node.xpath('text()').get()
        
        opponent['name'] = opponent_name.strip('\n')
        opponents.append(opponent)
    
    return opponents


def get_fighter_info(html):
    selector = Selector(text=html)
    trs = selector.xpath('//table[@class="infobox vcard"]/tbody/tr')

    fighter_info = {
        'name': None,
        'image': None,
        'nickname': None,
        'nationality': None
    }
    fighter_info['name'] = trs[0].xpath('.//span/text()').get()
    fighter_info['image'] = f"https://en.wikipedia.org{trs[1].xpath('.//a/@href').get()}"
    for tr in trs[2:]:
        key : str = tr.xpath('./th/text()').get()
        value = tr.xpath('./td/text()').get()

        if key is None or value is None:
            continue

        if (key.startswith('Nickname')):
            fighter_info['nickname'] = value
        elif (key.startswith('Nationality')):
            fighter_info['nationality'] = value
        
    return fighter_info






def zhuye(requests=None):
    url1 = 'https://www.zhihu.com/people/qi-hang-46-15/collections'
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }
    res = requests.get(url1, headers=head)
    name=re.findall(r'"noreferrer noopener">(.*?)</a>',res.text)    #正则切割
    href=re.findall(r'href="/collection(.*?)"',res.text)            #正则切割
    for i in range(0,len(name)):
        print("收藏夹："+name[i])
        url2 = 'https://www.zhihu.com/api/v4/collections'           #网页头
        url2=url2+href[i]+'/items?offset=0&limit=20'                #组成新网址
        ziye(url2)

def ziye(url2):
    try:
        head = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
        }
        res = requests.get(url2, headers=head)
        strs = re.findall(r'NORMAL",(.*?)","question', res.text)    #正则切割
        for i in range(0,len(strs)):
            url=re.findall(r'rl":"(.*?)","created_time',strs[i])    #正则切割
            title = re.findall(r'title":"(.*)', strs[i])
            print(title+url)
    except:
        return 0

if __name__ == '__main__':
    zhuye()
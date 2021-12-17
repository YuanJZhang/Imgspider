import scrapy
# 添加刚才创建的数据结构
from imgspider.items import ImgspiderItem

class MeinvSpider(scrapy.Spider):
    name = 'meinv'
    # 设置域名 可以注释掉
    allowed_domains = ['223rou.com']
    # 设置起始url
    #start_urls = ['http://jandan.net/girl']
    start_urls = ['http://223rou.com/htm/2021/11/28/yazhousetu/531428.html']

    def parse(self, response):

        # 创建数据结构
        item = ImgspiderItem()
        # 获取每个页面上的图片地址 图片名称 存放文件目录名
        # item['imgurl'] = response.xpath("/html/body/section/article//img/@data-src").getall()
        # item['imgname'] = response.xpath("/html/body/section/article//img/@data-src").getall()
        # item['dirname'] = response.xpath("/html/body/div[1]/div/h1/text()").get()
        item['imgurl'] = response.xpath("/html/body/div[5]/div/div[1]/img/@src").getall()
        item['imgname'] = response.xpath("/html/body/div[5]/div/div[1]/img/@src").getall()
        item['dirname'] = response.xpath("/html/body/div[5]/div/h1/text()").get()

        # 将数据给管道
        yield item

        # 翻页处理
        #next_page = response.xpath("(//div[@class='comments']//a[@class='previous-comment-page'])[last()]/@href").get()
        next_page = 'http://223rou.com' + response.xpath("/html/body/div[5]/div/div[2]/a[2]/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        pass

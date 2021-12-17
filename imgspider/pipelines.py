# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy
from scrapy.pipelines.images import ImagesPipeline

class ImgspiderPipeline(ImagesPipeline):
    #def process_item(self, item, spider):
    #    return item
    def get_media_requests(self, item, info):
        for i in range(len(item['imgurl'])):
            # 爬取的图片地址并不是完整的，需要加上协议和域名
            # imgurl = "https://hwenhai-vpn01.eastasia.cloudapp.azure.com" + item['imgurl'][i]
            imgurl = item['imgurl'][i]


            # meta 传参给self.file_path()
            # yield scrapy.Request(imgurl, meta={'imgname': item['imgname'][i], 'dirname': item['dirname']})
            yield scrapy.Request(imgurl, meta={'imgname': item['imgname'][i], 'dirname': item['dirname']})


    # 给图片定义存放位置和图片名
    def file_path(self, request, response=None, info=None, *, item=None):
        # imgname = request.meta['imgname'].strip() + '.jpg'
        # imgname = request.meta['imgname'].split('/')[-1]
        # dirname = request.meta['dirname']
        # filename = u"{}/{}".format(dirname, imgname)

        imgname = request.meta['imgname'].split('/')[-1]
        dirname = request.meta['dirname']

        filename = u"{}/{}".format(dirname, imgname)

        return filename
    #
    # def item_completed(self, results, item, info):
    #     return item
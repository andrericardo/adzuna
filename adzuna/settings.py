# Scrapy settings for adzuna project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'adzuna'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['adzuna.spiders']
NEWSPIDER_MODULE = 'adzuna.spiders'
DEFAULT_ITEM_CLASS = 'adzuna.items.AdzunaItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)


BOT_NAME = 'beasts'

SPIDER_MODULES = ['beasts.spiders']
NEWSPIDER_MODULE = 'beasts.spiders'

ROBOTSTXT_OBEY = False
LOG_LEVEL = 'CRITICAL'
# LOG_LEVEL = 'INFO'

REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
FEED_EXPORT_ENCODING = 'utf-8'

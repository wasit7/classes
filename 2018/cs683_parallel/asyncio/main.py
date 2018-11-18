
url = 'https://www.theguardian.com'
crawler = GuardianCrawler(url, 3)
future = asyncio.Task(crawler.crawl_async())
loop = asyncio.get_event_loop()
loop.run_until_complete(future)
loop.close()
result = future.result()
print(len(result))

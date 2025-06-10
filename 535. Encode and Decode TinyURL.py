class Codec:
    def encode(self, longUrl: str) -> str:
        self.url_list = []
        self.url_list.append(longUrl)
        return str(len(self.url_list) - 1)

    def decode(self, shortUrl: str) -> str:
        index = int(shortUrl)
        return self.url_list[index]

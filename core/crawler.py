import requests
import json

# url = "https://drogasil.com.br"
# query = "query tradeByParams($id: String, $store: String, $name: String, $pages: [String!], $platforms: [String!], $sizes: [String!], $slot: String, $enabled: String, $position: String, $type: String) {\n tradeByParams(\n params: {id: $id, store: $store, name: $name, pages: $pages, platforms: $platforms, sizes: $sizes, slot: $slot, enabled: $enabled, position: $position, type: $type}\n ) {\n id\n store\n name\n pages\n platforms\n sizes\n slot\n enabled\n position\n type\n createdAt\n updatedAt\n __typename\n }\n}\n"

def return_info():
    print('digite o seu termo de busca')
    busca = input()
    url = "https://api-gateway-prod.drogasil.com.br/search/v2/store/DROGASIL/channel/SITE/product/search/live?term="+str(busca)+"&tokenCart=JORH5eyXMF9F7mqV2SDV1K9ZiHJeWrGY&limit=4&sort_by=relevance:desc&origin=searchSuggestion"
    
    response = requests.get(url = url)
    print(response.url)
    print(json.dumps(response.json(), indent = 4))
    print(50*'*')

if __name__ == '__main__':
    return_info()
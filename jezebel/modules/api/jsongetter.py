# PATTERN = 'INVALID_MARKET\|Unknown symbol'

"""Should treat text response to validade if have any errors or no umatch pattern in json"""
def get_json(response):
    # if res.text.find(PATTERN)
    if (response.text != None) or (response.text != ''):
        return response.json()

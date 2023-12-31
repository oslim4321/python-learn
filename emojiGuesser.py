

def emoji_converter(msg):
    words = msg.split(' ')
    emojies = {
        ':)': '😃',
        '):': '😔'
    }
    output = ''
    for word in words:
        output += emojies.get(word, word) + ' '
    return output


message = input('>')
result = emoji_converter(message)
print(result)
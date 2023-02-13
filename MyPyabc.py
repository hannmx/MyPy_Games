query = 'привет как абврв длываб лдыывабп вба дждабв'
stopword = ['абв']
querywords = query.split()
print(querywords)
querywords.remove('абврв')
print(querywords)
resultwords  = [word for word in querywords if word.lower() not in stopword]
result = ' '.join(resultwords)

print(result)
query = 'aбв как фып уба вба абв абв'
stopword = ['абв']
querywords = query.split()
print(querywords)

resultwords  = [word for word in querywords if word.lower() not in stopword]
result = ' '.join(resultwords)

print(result)
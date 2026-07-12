from snownlp import SnowNLP
while True:
    line = input()
    result = SnowNLP(line).sentiments
    if result <= 0.33:
        print("贬义")
    elif result <= 0.66:
        print("中性")
    else:
        print("褒义")
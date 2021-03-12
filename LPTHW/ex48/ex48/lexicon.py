lexicon = {'north': 'direction', 'south': 'direction','east': 'direction',
'go':'verb', 'kill':'verb','eat':'verb',
'the': 'stop', 'in': 'stop', 'of': 'stop',
'bear': 'noun', 'princess': 'noun',
'number': 1234567890 }



def scan(sen):
    try:
        results = []
        words = sen.split()
        for w in words:
            word_type = lexicon.get(w)
            results.append((word_type, w))
            return results

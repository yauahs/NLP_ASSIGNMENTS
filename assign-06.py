'''Name:Tejas Gunjal
Batch:B
Roll no:24
Pract no 6: Dependency Parsing  '''
import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")
piano_text = "Tejas is learning python He is now working on NLP project"
piano_doc = nlp(piano_text)
for token in piano_doc:
    print(
        f"""
TOKEN: {token.text}
=====
{token.tag_ = }
{token.head.text = }
{token.dep_ = }"""
    )
    
displacy.serve(piano_doc, style="dep")
    
# Output:
# TOKEN: Tejas
# =====
# token.tag_ = 'NNP'
# token.head.text = 'learning'
# token.dep_ = 'nsubj'

# TOKEN: is
# =====
# token.tag_ = 'VBZ'
# token.head.text = 'learning'
# token.dep_ = 'aux'

# TOKEN: learning
# =====
# token.tag_ = 'VBG'
# token.head.text = 'learning'
# token.dep_ = 'ROOT'

# TOKEN: piano
# =====
# token.tag_ = 'NN'
# token.head.text = 'learning'
# token.dep_ = 'dobj'
    
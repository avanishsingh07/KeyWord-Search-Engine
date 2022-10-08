import spacy
import enchant
import en_core_web_sm
from spacy.matcher import PhraseMatcher
from scipy import spatial
import time
from spacy.tokens import DocBin
from spacy.tokens import Doc
from spacy.vocab import Vocab

def search_for_keyword(keyword):
    nlp=en_core_web_sm.load()
    doc_obj=spacy_to_doc("spacydoc5.spacy")
    phrase_matcher = PhraseMatcher(nlp.vocab)
    phrase_list = [nlp(keyword)]
    phrase_matcher.add("Text Extractor", None, *phrase_list)

    matched_items = phrase_matcher(doc_obj)

    matched_text = []
    for match_id, start, end in matched_items:
        text = nlp.vocab.strings[match_id]
        span = doc_obj[start: end]
        matched_text.append(span.sent.text)
    return matched_text

start_time = time.time()
def main():
    input_keyword=input("Input keyword.......\n")#'mvanzijl79@gmail.com'
    print(search_for_keyword(input_keyword))
    print("--- %s seconds ---" % (time.time() - start_time))
    
if __name__ == "__main__":
    main()
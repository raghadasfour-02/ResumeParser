
import os
from . import utils
import spacy
import pprint
from spacy.matcher import Matcher
import multiprocessing as mp

class ResumeParser(object):
    def __init__(self, resume):
        nlp = spacy.load('en_core_web_sm')
        self.__matcher = Matcher(nlp.vocab)
        self.__details = {
            'name'              : None,
            'email'             : None,
            'phone_number'      : None,
            'skills'            : None,
            'education'         : None,
            'experience'        : None,
        }
        self.__resume      = resume
        self.__text_raw    = utils.extract_text(self.__resume, os.path.splitext(self.__resume)[1])
        self.__text        = ' '.join(self.__text_raw.split())
        self.__nlp         = nlp(self.__text)
        self.__noun_chunks = list(self.__nlp.noun_chunks)
        self.__get_basic_details()

    def get_extracted_data(self):
        return self.__details

    def __get_basic_details(self):
        name       = utils.extract_name(self.__nlp, matcher=self.__matcher)
        email      = utils.extract_email(self.__text)
        phone      = utils.extract_phone_number(self.__text)
        skills     = utils.extract_skills(self.__nlp, self.__noun_chunks)
        education  = utils.extract_education([sent.string.strip() for sent in self.__nlp.sents])
        experience = utils.extract_experience(self.__text)
        self.__details['name'] = name
        self.__details['email'] = email
        self.__details['phone_number'] = phone
        self.__details['skills'] = skills
        self.__details['education'] = education
        self.__details['experience'] = experience
        return

def resume_result_wrapper(resume):
        parser = ResumeParser(resume)
        return parser.get_extracted_data()

if __name__ == '__main__':
    pool = mp.Pool(mp.cpu_count())

    resumes = []
    data = []
    for root, directories, filenames in os.walk('resumes'):
        for filename in filenames:
            file = os.path.join(root, filename)
            resumes.append(file)

    results = [pool.apply_async(resume_result_wrapper, args=(x,)) for x in resumes]

    results = [p.get() for p in results]

    pprint.pprint(results)
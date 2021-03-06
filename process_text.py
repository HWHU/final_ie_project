import os
import re
import nltk

def save_chapters(chapters):
    """
    Save each chapter in a list to its own separate file.
    """
    path = os.getcwd() + '/data/chapters/chapter_'
    for i, chapter in enumerate(chapters):
        with open(path + str(i) + '.txt', 'w') as outfile:
            for paragraph in chapter:
                outfile.write(paragraph + '\n')

def preprocess_text(chapter):
    """
    Perform sentence tokenization, word tokenization, and part-of-speech tagging
    on a chapter.
    """
    chapter = [[nltk.pos_tag(nltk.word_tokenize(sent)) for sent in
                nltk.sent_tokenize(paragraph)]
               for paragraph in chapter]
    return chapter

def write_to_file(chapter, i):
    """
    Given a processed (tokenized and tagged) chapter and its corresponding
    number, save it as a file.
    """
    path = os.getcwd() + '/data/pos_tagged/chapter_'
    with open(path + str(i) + '.pos', 'w') as outfile:
        for paragraph in chapter:
            string = ''
            for sentence in paragraph:
                string += ' '.join([t[0] + '_' + t[1] for t in sentence]) + '\n'
            outfile.write(string + '\n')

def read_file():
    """
    Read raw text file, and split it up into paragraphs.
    """
    with open(os.getcwd() + '/data/game_of_thrones.txt', 'r') as infile:
        raw_text = infile.read()

    paragraphs = raw_text.split(' \n\n')
    paragraphs = [para for para in paragraphs if para]
    paragraphs = [re.sub('\n', '', para) for para in paragraphs]
    return paras_to_chapters(paragraphs)

def paras_to_chapters(paragraphs):
    """
    Take paragraphs from raw text file and organize them into distinct chapters.
    """
    chapters = []
    chapter = [paragraphs[0]]
    for paragraph in paragraphs[1:]:
        if paragraph.isupper() and paragraph.isalpha():
            chapters.append(chapter)
            chapter = [paragraph]
        else:
            chapter.append(paragraph)
    chapters.append(chapter)
    return chapters

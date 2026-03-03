class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
    def __str__(self):
        return self.sentence
    def get_word(self, index):
        return self.sentence.split()[index]
    def num_words(self):
        return len(self.sentence.split())
    def add_word(self, new_word):
        self.sentence += " " + new_word
    def replace(self, index, new_word):
        sentence_array = self.sentence.split()
        sentence_array[index] = new_word
        self.sentence = " ".join(sentence_array)
    def concat_sentence(self, other_sentence):
        self.sentence += ' ' + str(other_sentence)
        
s1 = Sentence("apa kabar semuanya")
print(s1.get_word(0))
print(s1.get_word(2))

s1.replace(2, "mahasiswa")
print(s1)

print(s1.num_words())

s2 = Sentence("tetap semangat")
s1.concat_sentence(s2)

s1.add_word("ya")

print(s1)
print(s1.get_word(4))
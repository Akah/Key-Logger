from operator import itemgetter, attrgetter, methodcaller
##################################################
##################################################
class new_file:
    def __init__(self, file_path):
        self.datei = open(file_path,'r')
        self.array = []
        for line in self.datei:
            self.array.extend(line.split(' '))
        self.datei.close()

    #returns number of times item appears in array
    def number_of(self, item):
        #copy = self.array
        counter = 0
        while item in self.array:
            counter = counter+1
            del self.array[self.array.index(item)]
        return counter

    def results(self):
        letters = []
        for item in range(len(self.array)):
            try:
                current = self.array[item]
            #if len(current) == 1:
            #   print(current+": "+str(a.number_of(current)))
                temp = [current,self.number_of(current)]
                letters.append(temp)

            except IndexError:
                current = 'null';

        letters = sorted(letters, key=itemgetter(1), reverse=True)
        return letters


##################################################
##################################################


chars = new_file('chars_log.txt')
words = new_file('words_log.txt')
print('chars_log.txt:')
print(chars.results())
print('')
print('words_log.txt:')
print(words.results())
print('')

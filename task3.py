from itertools import zip_longest
import sys

def sourse():
    tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Алена', 'Данила', 'Маша']
    klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
        
    # iterator = zip_longest(tutors, klasses[:len(tutors)])
    iterator = ((a,b) for a,b in zip_longest(tutors,klasses))
    print(list(iterator))
    print(sys.getsizeof(iterator))
        
    
if __name__ == "__main__":
    sourse()
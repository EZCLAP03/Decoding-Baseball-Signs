
def get_signs():
    first_sign = list(input('Enter your first sign here(Just give the the starting letter of the signs): '))
    second_sign = list(input('Enter your second sign here(Just give the the starting letter of the signs): '))
    third_sign = list(input('Enter your third sign here(Just give the the starting letter of the signs): '))
    return first_sign, second_sign, third_sign

class DecodeSigns:
    def __init__(self, first_sign, second_sign, third_sign):
        self.first_sign = first_sign
        self.second_sign = second_sign
        self.third_sign = third_sign
    
    def compare(self):
        for letter in self.first_sign:
            for letter1 in self.second_sign:
                for letter2 in self.third_sign:
                    if letter == letter1 == letter2:
                        print('indicator has been found')
                        print(letter)
            

                          
x  = get_signs()

decoder = DecodeSigns(x[0], x[1], x[2])
decoder.compare()




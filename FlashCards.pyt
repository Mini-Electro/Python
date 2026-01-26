class FlashCard:
    def __init__(self, word, meaning):
        self.Word = word
        self.Meaning = meaning
    def __str__(self):

        #we will return a string
        return self.Word+'('+self.Meaning+')'

flash = []
print("Welcome to flashcard application")

# the following loop will be repeated until user stops to add the flashcards

while(True):
    word = input("Enter the name you want to add to the flashcard: ")
    meaning = input("Enter the meaning of the word: ")

    flash.append(FlashCard(word, meaning))
    option = int(input("Enter 0, if you want to add another flashcard otherwise enter 1: "))

    if(option):
        break


# printing all the flashcards#
print("\nYour Flashcards")
for i in flash:
    print(">", i)
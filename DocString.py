class DocString:
    'This is a docstring. Creating a new class'

    welcome = 'Welcome to the DocString in the Class definitions'
    def message(self):
        return print('This message is about DocStrings Class')

print(DocString.__doc__)
print(DocString.welcome)
print(DocString.message(''))


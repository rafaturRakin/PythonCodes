def isPalindrome(number):
    givenNumber = number
    reversedNumber = 0
    while number > 0:
        currentDigit = number % 10
        number = number // 10
        reversedNumber = (reversedNumber * 10) + currentDigit

    if (givenNumber == reversedNumber):
        return True
    else:
        return False


userInput = int(input("Enter a number : "))

if(isPalindrome(userInput)):
    print(f"{userInput} is a Palindrome Number")
else:
    print(f"{userInput} is not a Plaindrome Number")

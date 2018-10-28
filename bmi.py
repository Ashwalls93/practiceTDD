def get_user_stats(age, height, weight):
    user_stats = [age, height, weight]
    return user_stats

def calc_user_bmi(height, weight):
    user_bmi = weight / ((height / 100) * (height / 100))
    return int(user_bmi)

def user_birth_year(age):
    return 2018 - age

def main():

    age = int(input('Please enter your age (years): '))
    height = int(input('Please enter your height (cm): '))
    weight = int(input('Please enter your weight (kg): '))

    print("Your BMI is: " + str(calc_user_bmi(height, weight)))

if __name__ == '__main__':
    main()




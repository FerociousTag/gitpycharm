#zachary blackwell 1941472

def fat_burning_heart_rate(user_age):
    heart_rate = 0.7 * (220 - user_age)
    return heart_rate


def get_age():
    user_age = int(input())
    if not 18 <= user_age <= 75:
        raise ValueError("Invalid age.")
    else:
        return user_age


if __name__ == "__main__":
    #tests that the get age function returned user_age
    try:
        user_age = get_age()
        heart_rate = float(fat_burning_heart_rate(user_age))
        print('Fat burning heart rate for a 35 year-old:', '{:.1f}'.format(heart_rate), 'bpm')
    #if the value was invalid it out puts a message
    except ValueError as error_message:
        print(error_message)
        print('Could not calculate heart rate info.\n')


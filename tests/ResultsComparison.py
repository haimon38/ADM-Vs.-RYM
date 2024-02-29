
class ResultsComparison():

    def find_highest_value(critics_rating, users_rating):
        value_1 = float(critics_rating)
        value_2 = users_rating
        if(value_1 > value_2):
            print("\n" + "\033[1m" + "Critics ratings are higher than users ratings" + "\033[0m")
        elif(value_1 == value_2):
            print("\n" + "\033[1m" + "Critics ratings are equal to users ratings" + "\033[0m")
        else:
            print("\n" + '\033[1m' + "Users ratings are higher than critics ratings" + "\033[0m")
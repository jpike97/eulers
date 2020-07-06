import re

hand_one = []
hand_two = []
line_count = 0

straight_track = [0] * 15
flush_track = { 
    'H': 0,
    'C': 0,
    'D': 0,
    'S': 0
}

hand1count = 0
hand2count = 0

class Hand:
    def __init__(self):
        self.RFlush = 0
        self.SFlush = 0
        self.FourKind = 0
        self.FullHouse = 0
        self.Flush = 0
        self.Straight = 1
        self.ThreeKind = 0
        self.TwoPair = 0
        self.OnePair = 0
        self.HighCard = 0
        self.SecondHighest = 0
        self.ThirdHighest = 0
        self.FourthHighest = 0
        self.FifthHighest = 0
        self.LowCard = 14

def parse_card(value):
    try: 
        int(value)
        return int(value)
    except ValueError: 
        return {
            'T': 10,
            'J': 11,
            'Q': 12,
            'K': 13,
            'A': 14
        }[value]

def card_calc(hand_one):
            flush_track_hand = flush_track.copy()
            straight_track_hand = straight_track.copy()
            temp_one = Hand()
            highest_values = []
            for x in range(0, len(hand_one)):
                #store high card
                 value = (parse_card(hand_one[x][0]))
                 highest_values.append(value)
                 suit = (hand_one[x][1])
                 if value > temp_one.HighCard:
                     temp_one.HighCard = value
                 if value < temp_one.LowCard:
                     temp_one.LowCard = value
                ##straight tracker
                 straight_track_hand[value] += 1

                 ##checking for flush
                 flush_track_hand[suit] += 1
                 if flush_track_hand[suit] == 5:
                     temp_one.Flush = 1

                ##checking for one pair
                 if straight_track_hand[value] == 2:
                      if temp_one.OnePair == 0:
                          temp_one.OnePair = value
                      else:
                          if value > temp_one.OnePair:
                            temp_one.TwoPair = value
                          else: 
                            temp_one.TwoPair = temp_one.OnePair
                        
                ##checking for 3kind
                 if straight_track_hand[value] == 3 and value > temp_one.ThreeKind:
                     temp_one.ThreeKind = value
                
                ##checking for 4kind
                 if straight_track_hand[value] == 4 and value > temp_one.FourKind:
                     temp_one.FourKind = value
                     temp_one.ThreeKind = 0

            ##checking for fullhouse
            if temp_one.ThreeKind !=0 and temp_one.OnePair != 0:
                temp_one.FullHouse = temp_one.ThreeKind

            ##checking for straight
            count = 0
            for j in range(0, len(straight_track_hand)):
                count = count + straight_track_hand[j]
                if straight_track_hand[j] > 1:
                    temp_one.Straight = 0
                    break
                if count > 4:
                    break
                if straight_track_hand[j] == 0 and count != 0:
                    temp_one.Straight = 0
                    break    
            if temp_one.Straight != 0:
                temp_one.Straight = temp_one.LowCard
            
            ##check for SFlush
            if temp_one.Straight != 0 and temp_one.Flush !=0:
                temp_one.SFlush = temp_one.LowCard

            ##check for RFlush
            if temp_one.SFlush and temp_one.LowCard == 10:
                temp_one.RFlush = 1
            
            ##value assignment
            highest_values.sort()
            temp_one.SecondHighest = highest_values[1]
            temp_one.ThirdHighest = highest_values[2]
            temp_one.FourthHighest = highest_values[3]
            temp_one.FifthHighest = highest_values[4]
            return(temp_one)

def hand_deconstruct(hand1):
    hand_values = []
    for attr, value in hand1.__dict__.items():
        hand_values.append(value)

    return hand_values


with open("poker.txt") as f:
        for line in f:
            string_line = line.strip(("\n"))
            no_space = re.sub(r'\s+', '', string_line)
            hand_one = re.findall('..', no_space)[0:5]
            hand_two = re.findall('..', no_space)[5:10]
            line_count += 1
            
            HAND1 = card_calc(hand_one)
            HAND2 = card_calc(hand_two)

            hand1_deconstructed = (hand_deconstruct(HAND1))
            hand2_deconstructed = (hand_deconstruct(HAND2))
            for x in range(0, len(hand1_deconstructed)):
                
                if hand1_deconstructed[x] > hand2_deconstructed[x]:
                    print("hand1 wins")
                    hand1count += 1
                    break
                if hand2_deconstructed[x] > hand1_deconstructed[x]:
                    print("hand2 wins")
                    hand2count += 1
                    break   
                if hand2_deconstructed[x] == hand1_deconstructed[x]:
                    continue

print(hand1count)
            




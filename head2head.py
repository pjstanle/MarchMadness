import numpy as np

def get_head2head():
    # column one is 1 seed
    records = np.array([
                        [50.0 ,  45.5,  36.6,  29.5,  20.3,  29.4,  14.3,  21.5,   9.4,  12.5,  44.4,   0.0,   0.0,   0.0,   0.0,   1.3],  
                        [54.5 ,  50.0,  39.4,  50.0,  75.0,  27.8,  30.4,  60.0,  33.3,  35.9,  15.8,   0.0,   0.0,   0.0,   7.2,   0.0],  
                        [63.4 ,  60.6,  50.0,  44.4,  50.0,  41.7,  36.8,   0.0,  25.0,  30.8,  33.3,   0.0,   0.0,  14.5,  33.3,   0.0],  
                        [70.5 ,  50.0,  55.6,  50.0,  42.7,  66.7,  66.7,  61.5,  60.0,   0.0,   0.0,  29.5,  21.1,   0.0,   0.0,   0.0],  
                        [79.7 ,  25.0,  50.0,  57.3,  50.0,   0.0,   0.0,  75.0,  60.0,   0.0,   0.0,  32.6,  15.0,   0.0,   0.0,   0.0],  
                        [70.6 ,  72.2,  58.3,  33.3, 100.0,   0.0,  33.3,  75.0,   0.0,  40.0,  37.2,   0.0,   0.0,  12.5,   0.0,   0.0],  
                        [85.7 ,  69.6,  63.2,  33.3,   0.0,  66.7,   0.0,  50.0,   0.0,  39.4, 100.0,   0.0,   0.0,   0.0,  66.7,   0.0],  
                        [78.5 ,  40.0, 100.0,  38.5,  25.0,  25.0,  50.0,   0.0,  48.9,   0.0,   0.0, 100.0,   0.0,   0.0,   0.0,   0.0],  
                        [90.6 ,  66.7,  75.0,  40.0,  40.0,   0.0,   0.0,  51.1,   0.0,   0.0, 100.0,   0.0,   0.0,   0.0,   0.0,   0.0],  
                        [87.5 ,  64.1,  69.2, 100.0, 100.0,  60.0,  60.6,   0.0, 100.0,   0.0,  50.0,   0.0,   0.0,   0.0,   0.0,   0.0],  
                        [55.6 ,  84.2,  66.7,   0.0,   0.0,  62.8,   0.0, 100.0,   0.0,  50.0,  50.0,   0.0,   0.0,   0.0,   0.0,   0.0],  
                        [100.0, 100.0,   0.0,  70.5,  67.4,   0.0,   0.0,   0.0,   0.0,   0.0,   0.0,  50.0,  25.0,   0.0,   0.0,   0.0],  
                        [100.0,   0.0,   0.0,  78.9,  85.0,   0.0,   0.0, 100.0, 100.0,   0.0,   0.0,  75.0,  50.0,   0.0,   0.0,   0.0],  
                        [0.0  ,   0.0,  85.5,   0.0,   0.0,  87.5, 100.0,   0.0,   0.0, 100.0, 100.0,   0.0,   0.0,  50.0,   0.0,   0.0],  
                        [0.0  ,  92.8,  66.7,   0.0,   0.0, 100.0,  33.3, 100.0,   0.0, 100.0,   0.0,   0.0,   0.0,   0.0,   0.0,   0.0],  
                        [98.7 ,   0.0,   0.0,   0.0,   0.0,   0.0,   0.0,   0.0, 100.0,   0.0,   0.0,   0.0,   0.0,   0.0,   0.0,  50.0]
                        ]) / 100.0
                        
    return records


def get_starting_bracket():
    # EAST, WEST, SOUTH, MIDWEST
    seeds = np.array([1, 16, 8, 9, 5, 12, 4, 13, 6, 11, 3, 14, 7, 10, 2, 15,
               1, 16, 8, 9, 5, 12, 4, 13, 6, 11, 3, 14, 7, 10, 2, 15,
               1, 16, 8, 9, 5, 12, 4, 13, 6, 11, 3, 14, 7, 10, 2, 15,
               1, 16, 8, 9, 5, 12, 4, 13, 6, 11, 3, 14, 7, 10, 2, 15])

    teams = np.array(["UConn", "Stetson", "FAU", "Northwestern", "San Diego St",
                      "UAB", "Auburn", "Yale", "BYU", "Duquense", "Illinois",
                      "Morehead St", "Washington St", "Drake", "Iowa State",
                      "S Dakota St", "North Carolina", "HOW/WAG", "Mississippi St",
                      "Michigan St", "Saint Mary's", "Grand Canyon", "Alabama", "Charleston",
                      "Clemson", "New Mexico", "Baylor", "Colgate", "Dayton", "Nevada",
                      "Arizona", "Long Beach St", "Houston", "Longwood", "Nebraska", "Texas A&M",
                      "Wisconsin", "James Madison", "Duke", "Vermont", "Texas Tech", "NC State",
                      "Kentucky", "Oakland", "Florida", "BOIS/COL", "Marquette", "Western KY",
                      "Purdue", "MTST/GRAM", "Utah State", "TCU", "Gonzaga", "McNeese", "Kansas",
                      "Samford", "South Carolina", "Oregon", "Creighton", "Akron", "Texas",
                      "UVA/CSU", "Tennessee", "Saint Peter's"])
    return seeds, teams


def simulate_tournamet():
    probabilities = get_head2head()
    seeds, teams = get_starting_bracket()
    current_round_indices = np.arange(64, dtype=int)

    round = 1
    while len(current_round_indices) > 1:
        winners_indices = []
        for i in range(int(len(current_round_indices) / 2)):
            seed1 = seeds[current_round_indices[2*i]]
            seed2 = seeds[current_round_indices[2*i + 1]]
            prob = probabilities[seed2 - 1, seed1 - 1]
            num = np.random.rand()
            if num < prob:
                winners_indices.append(int(current_round_indices[2*i]))
            else:
                winners_indices.append(int(current_round_indices[2*i + 1]))
        
        print("Round %s"%round)
        # print(winners_indices)
        # print("Winning seeds: ", seeds[winners_indices])
        if len(winners_indices) > 4:
            n = int(len(winners_indices) / 4)
            print("Winning teams: ", teams[winners_indices[:n]])
            print("Winning teams: ", teams[winners_indices[n:2*n]])
            print("Winning teams: ", teams[winners_indices[2*n:3*n]])
            print("Winning teams: ", teams[winners_indices[3*n:]])
        else:
            print("Winning teams: ", teams[winners_indices])
        current_round_indices = winners_indices
        round += 1
            


if __name__=="__main__":
    simulate_tournamet()
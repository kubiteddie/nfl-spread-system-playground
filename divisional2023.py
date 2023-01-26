import pandas as pd
import numpy as np

def weightedSideRatings(side, weightDict):
    weightedSum = 0
    for player in side:
        weightedSum += weightDict[player[0]]* player[1]
    return weightedSum/len(side)


def ratingDiff(homeRating, awayRating, coef):
    return coef * (homeRating - awayRating)


def main():
    offPosWeights = {"C":0.8, "G":1.1, "T":1.2, "WR":1.2, "TE": .9, "RB": 0.8}
    defPosWeights = {"IDL": 1.05, "EDGE": 1.5, "ILB": 1.1, "OLB": 1, "CB": 1.5,  "S": 0.8}

    homeField = 2.64
    fieldPos = 0.655
    qbRating = 0.143
    offRating = 0.147
    defRating = 0.547
    offDVOA = 34.63
    defDVOA = -21.18
    bye = 0.969

    qbs = [("Cheifs", 98), ("Jaguars", 82), ("Eagles", 85), ("Giants", 75), ("Bills", 94), ("Bengals", 93), ("49ers", 71), ("Cowboys", 91)]
    offDVOAs = [("Cheifs", .252), ("Jaguars", .077), ("Eagles", .151), ("Giants", .102), ("Bills", .19), ("Bengals", .142), ("49ers", .132), ("Cowboys", .029)]
    defDVOAs = [("Cheifs", .014), ("Jaguars", .061), ("Eagles", -.097), ("Giants", .102), ("Bills", -.11), ("Bengals", -.044), ("49ers", -.141), ("Cowboys", -.133)]
    avgFieldPositions = [("Cheifs", (24.2+27.7)/2), ("Jaguars", (26.1+25.9)/2), ("Eagles", (24+25.5)/2), ("Giants", (25.5+25.4)/2), ("Bills", (26.2+27.4)/2), ("Bengals", (24+26.6)/2), ("49ers", (27.4+25.6)/2), ("Cowboys", (28+25)/2)]

    chiefsOffense = [("T", 82), ("T", 68), ("G", 82), ("G", 89), ("C", 89), ("TE", 68), ("TE", 99), ("WR", 82), ("WR", 79), ("WR", 77), ("WR", 71), ("RB", 79), ("RB", 77)]
    chiefsOffenseAvg = weightedSideRatings(chiefsOffense, offPosWeights)
    jagsOffense = [("T", 78), ("T", 67), ("G", 71), ("G", 89), ("C", 69), ("TE", 84), ("WR", 85), ("WR", 81), ("WR", 78), ("WR", 75), ("RB", 83)]
    jagsOffensiveAvg = weightedSideRatings(jagsOffense, offPosWeights)

    eaglesOffense = [("T", 95), ("T", 84), ("G", 79), ("G", 78), ("C", 93), ("TE", 88), ("TE", 63), ("WR", 92), ("WR", 75), ("WR", 77), ("WR", 71), ("RB", 86), ("RB", 74)]
    eaglesOffenseAvg = weightedSideRatings(eaglesOffense, offPosWeights)
    giantsOffense = [("T", 91), ("T", 73), ("G", 75), ("G", 68), ("C", 74), ("TE", 70), ("TE", 99), ("WR", 77), ("WR", 76), ("WR", 76), ("WR", 73), ("RB", 93), ("RB", 72)]
    giantsOffenseAvg = weightedSideRatings(giantsOffense, offPosWeights)



    eaglesDefense = [("S", 85), ("S", 75), ("CB", 93), ("CB", 85), ("S", 67), ("ILB", 84), ("EDGE", 88), ("OLB", 74), ("IDL", 84), ("IDL", 82), ("IDL", 82), ("IDL", 81)]
    eaglesDefenseAvg = weightedSideRatings(eaglesDefense, defPosWeights)
    giantsDefense = [("S", 82), ("S", 80), ("CB", 82), ("CB", 73), ("CB", 66), ("ILB", 71), ("ILB", 68), ("EDGE", 80), ("EDGE", 72), ("IDL", 94), ("IDL", 82), ("IDL", 68) ]
    giantsDefenseAvg = weightedSideRatings(giantsDefense, defPosWeights)


    chiefsJagsDiff = homeField
    eaglesGiantsDiff = homeField
    billsBengalsDiff = homeField
    ninersCowboysDiff = homeField

    chiefsJagsDiff += ratingDiff(qbs[0][1], qbs[1][1], qbRating)
    eaglesGiantsDiff += ratingDiff(qbs[2][1], qbs[3][1], qbRating)
    billsBengalsDiff += ratingDiff(qbs[4][1], qbs[5][1], qbRating)
    ninersCowboysDiff += ratingDiff(qbs[6][1], qbs[7][1], qbRating)

    chiefsJagsDiff += ratingDiff(offDVOAs[0][1], offDVOAs[1][1], offDVOA)
    eaglesGiantsDiff += ratingDiff(offDVOAs[2][1], offDVOAs[3][1], offDVOA)
    billsBengalsDiff += ratingDiff(offDVOAs[4][1], offDVOAs[5][1], offDVOA)
    ninersCowboysDiff += ratingDiff(offDVOAs[6][1], offDVOAs[7][1], offDVOA)

    chiefsJagsDiff += ratingDiff(defDVOAs[0][1], defDVOAs[1][1], defDVOA)
    eaglesGiantsDiff += ratingDiff(defDVOAs[2][1], defDVOAs[3][1], defDVOA)
    billsBengalsDiff += ratingDiff(defDVOAs[4][1], defDVOAs[5][1], defDVOA)
    ninersCowboysDiff += ratingDiff(defDVOAs[6][1], defDVOAs[7][1], defDVOA)

    chiefsJagsDiff += ratingDiff(avgFieldPositions[0][1], avgFieldPositions[1][1], fieldPos)
    eaglesGiantsDiff += ratingDiff(avgFieldPositions[2][1], avgFieldPositions[3][1], fieldPos)
    billsBengalsDiff += ratingDiff(avgFieldPositions[4][1], avgFieldPositions[5][1], fieldPos)
    ninersCowboysDiff += ratingDiff(avgFieldPositions[6][1], avgFieldPositions[7][1], fieldPos)

    chiefsJagsDiff += ratingDiff(chiefsOffenseAvg, jagsOffensiveAvg, offRating) - 3
    eaglesGiantsDiff += ratingDiff(eaglesOffenseAvg, giantsOffenseAvg, offRating)

    eaglesGiantsDiff += ratingDiff(eaglesDefenseAvg, giantsDefenseAvg, defRating)

    chiefsJagsDiff += homeField
    eaglesGiantsDiff += homeField

    print(f"Model favors the Cheifs by {chiefsJagsDiff} points")
    print(f"Model favors the Eagles by {eaglesGiantsDiff} points")
    print(f"Model favors the Bills by {billsBengalsDiff} points")
    print(f"Model favors the 49ers by {ninersCowboysDiff} points")

if __name__ == "__main__":
    main()


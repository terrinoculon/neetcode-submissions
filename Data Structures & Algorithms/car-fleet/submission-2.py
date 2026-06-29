class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        triplets =[(pos, vel, (target - pos)/ vel) for pos, vel in zip(position, speed)]
        triplets = sorted(triplets, reverse = True )
        fleets = [triplets[0]]
        for car in triplets[1:]:
            if car[2]>fleets[-1][2]:
                fleets.append(car)
        return len(fleets)
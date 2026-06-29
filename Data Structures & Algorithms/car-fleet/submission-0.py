class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        triplets =[(pos, vel, (target - pos)/ vel) for pos, vel in zip(position, speed)]
        triplets = sorted(triplets, reverse = True )
        fleets = []
        for car in triplets:
            if not fleets:
                fleets.append(car)
            if fleets and car[2]>fleets[-1][2]:
                fleets.append(car)
        return len(fleets)
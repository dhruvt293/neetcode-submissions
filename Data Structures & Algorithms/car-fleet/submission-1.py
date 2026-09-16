class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position,speed))
        cars.sort(reverse=True)
        fleet_count = 1

        prev_time = (target-cars[0][0]) / cars[0][1]
        for curr_pos,curr_speed in cars[1:]:
            curr_time = (target-curr_pos) / curr_speed
            if curr_time > prev_time:
                fleet_count +=1
                prev_time = curr_time
        return fleet_count

        
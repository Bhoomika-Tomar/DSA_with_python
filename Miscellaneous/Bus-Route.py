from collections import defaultdict, deque
class Solution:
    def numBusesToDestination(self, routes: list[list[int]], source: int, target: int) -> int:
        
        #USING BFS

        if target == source:
            return 0

        #Map routes along with indices
        stop_to_buses = defaultdict (set)
        for i, route in enumerate (routes):
            for stop in route:
                stop_to_buses[stop].add(i)

        visited_buses = set()
        visited_stops = set([source])
        queue = deque([(source,0)])   #current stop and buses taken

        while queue:
            stop, buses_taken = queue.popleft()
            for bus in stop_to_buses[stop]:
                if bus in visited_buses:
                    continue
                visited_buses.add (bus)
                for next_stop in routes[bus]:
                    if next_stop == target:
                        return buses_taken + 1

                    if next_stop not in visited_stops:
                        visited_stops.add(next_stop)
                        queue.append((next_stop, buses_taken+1))

        return -1


routes = [[1,2,7],[3,6,7]]
source = 1
target = 6

sol = Solution()
print(sol.numBusesToDestination(routes, source, target))  






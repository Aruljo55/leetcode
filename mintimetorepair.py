class Solution:
    def repairCars(self, ranks, cars):
        left, right = 1, 10**14
        
        while left < right:
            mid = (left + right) // 2
            
            total_cars_repaired = 0
            for rank in ranks:
                cars_repaired = int((mid / rank) ** 0.5)
                total_cars_repaired += cars_repaired
            
            if total_cars_repaired >= cars:
                right = mid
            else:
                left = mid + 1
        
        return left
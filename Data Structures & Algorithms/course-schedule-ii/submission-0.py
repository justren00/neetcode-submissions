class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjSet = defaultdict(list)

        for course, prereq in prerequisites:
            adjSet[course].append(prereq) 

        output = []
        visit, cycle = set(), set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True 

            cycle.add(course)
            for prereq in adjSet[course]:
                if not dfs(prereq):
                    return False 
            cycle.remove(course)
            visit.add(course)
            output.append(course)
            return True 

        for c in range(numCourses):
            if dfs(c) == False:
                return []

        return output

        
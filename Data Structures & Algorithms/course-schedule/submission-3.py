class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjSet = defaultdict(list)

        for course, prereq in prerequisites:
            adjSet[course].append(prereq)  

        path = set()

        def dfs(course):
            if course in path:
                return False 

            if not adjSet[course]:
                return True

            path.add(course) 

            for prereq in adjSet[course]: 
                if not dfs(prereq):
                    return False 

            path.remove(course)
            adjSet[course] = []
            return True  

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

        
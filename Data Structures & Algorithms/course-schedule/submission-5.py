class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        You can turn this into a graph problem: 
            - For every [u, v], add an edge connecting v to u 

        Once you add edges for every course combination in prerequeisites
        Check if there is a cycle, if there is the schedule sucks 
        """
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

        
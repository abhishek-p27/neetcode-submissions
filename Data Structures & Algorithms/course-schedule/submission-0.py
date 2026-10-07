class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites: 
            graph[a].append(b)

        path = set()
        done = set()
        
        def dfs(course):
            #todo 
            if course in path: 
                return False
            if course in done: 
                return True
            path.add(course)
            for nxt in graph[course]: 
                if dfs(nxt) == False: 
                    return False 
            path.remove(course)
            done.add(course)
            return True


        for course in range(numCourses): 
            if dfs(course) == False: 
                return False
        return True
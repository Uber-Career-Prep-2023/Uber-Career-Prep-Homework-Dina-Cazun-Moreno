from collections import deque

def prerequisiteCourses(courses, map):
    order = []
    queue = deque()
    inDegree = {course: 0 for course in courses}
    for course in map:
        for prereq in map[course]:
            inDegree[course] += 1
    for course in inDegree:
        if inDegree[course] == 0:
            queue.append(course)
    while queue:
        course = queue.popleft()
        order.append(course)
        for prereq in map:
            if course in map[prereq]:
                inDegree[prereq] -= 1
                if inDegree[prereq] == 0:
                    queue.append(prereq)
    return order

print(prerequisiteCourses(["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"], { "Data Structures": ["Intro to Programming"], "Advanced Algorithms": ["Data Structures"], "Operating Systems": ["Advanced Algorithms"], "Databases": ["Advanced Algorithms"] }))

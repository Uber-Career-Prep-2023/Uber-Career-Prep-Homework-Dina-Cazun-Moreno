#Question 10: Prerequisite Courses

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
#output: ['Intro to Programming', 'Data Structures', 'Advanced Algorithms', 'Operating Systems', 'Databases']
print(prerequisiteCourses(["Intro to Writing", "Contemporary Literature", "Ancient Literature", "Comparative Literature", "Plays & Screenplays"], { "Contemporary Literature": ["Intro to Writing"], "Ancient Literature": ["Intro to Writing"], "Comparative Literature": ["Ancient Literature", "Contemporary Literature"], "Plays & Screenplays": ["Intro to Writing"] }
))
#output: ['Intro to Writing', 'Contemporary Literature', 'Ancient Literature', 'Plays & Screenplays', 'Comparative Literature']

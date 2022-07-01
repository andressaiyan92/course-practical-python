num_set = {1, 2, 3, 4, 5}
print(3 in num_set)
print("***************************************")
nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums)
nums.add(-7)
nums.remove(3)
print(nums)
print(len(nums))
print("***************************************")
"""
Sets can be combined using mathematical operations.
The union operator | combines two sets to form a new one containing items in either.
The intersection operator & gets items only in both.
The difference operator - gets items in the first set but not in the second.
The symmetric difference operator ^ gets items in either set, but not both.
"""
first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}
print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)
print("***************************************")
"""
Sets
You are working on a recruitment platform, which should match the available jobs and the candidates based on their skills.
The skills required for the job, and the candidate's skills are stored in sets.
Complete the program to output the matched skill.
"""
skills = {'Python', 'HTML', 'SQL', 'C++', 'Java', 'Scala'}
job_skills = {'HTML', 'CSS', 'JS', 'C#', 'NodeJS'}
print(list(skills & job_skills)[0])